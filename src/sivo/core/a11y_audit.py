import re
import logging
from typing import Optional, List, Dict, Any
from lxml import etree

logger = logging.getLogger("sivo.a11y")
if not logger.handlers:
    # Set up basic logging if not already configured
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)


def _hex_to_rgb(hex_color: str) -> Optional[List[int]]:
    """Convert hex string (e.g. #fff, #ffffff) to [R, G, B]."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c + c for c in hex_color)
    if len(hex_color) == 6:
        try:
            return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
        except ValueError:
            pass
    return None

def _get_rgb(color_str: str) -> Optional[List[int]]:
    """Try to parse a simple color string into RGB."""
    color_str = color_str.strip().lower()

    # Handle hex
    if color_str.startswith('#'):
        return _hex_to_rgb(color_str)

    # Handle rgb()
    rgb_match = re.match(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', color_str)
    if rgb_match:
        return [int(rgb_match.group(1)), int(rgb_match.group(2)), int(rgb_match.group(3))]

    # Hardcoded basic CSS colors mapping for simplicity
    basic_colors = {
        'black': [0, 0, 0], 'white': [255, 255, 255],
        'red': [255, 0, 0], 'green': [0, 128, 0],
        'blue': [0, 0, 255], 'yellow': [255, 255, 0],
        'cyan': [0, 255, 255], 'magenta': [255, 0, 255],
        'gray': [128, 128, 128], 'grey': [128, 128, 128],
        'transparent': None, 'none': None
    }
    return basic_colors.get(color_str, None)

def _relative_luminance(rgb: List[int]) -> float:
    """Calculate the relative luminance of a color based on WCAG 2.x formulas."""
    rsrgb = rgb[0] / 255.0
    gsrgb = rgb[1] / 255.0
    bsrgb = rgb[2] / 255.0

    r = rsrgb / 12.92 if rsrgb <= 0.03928 else ((rsrgb + 0.055) / 1.055) ** 2.4
    g = gsrgb / 12.92 if gsrgb <= 0.03928 else ((gsrgb + 0.055) / 1.055) ** 2.4
    b = bsrgb / 12.92 if bsrgb <= 0.03928 else ((bsrgb + 0.055) / 1.055) ** 2.4

    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def calculate_contrast_ratio(color1: str, color2: str) -> Optional[float]:
    """Calculate WCAG contrast ratio between two colors."""
    rgb1 = _get_rgb(color1)
    rgb2 = _get_rgb(color2)

    if not rgb1 or not rgb2:
        return None

    l1 = _relative_luminance(rgb1)
    l2 = _relative_luminance(rgb2)

    light = max(l1, l2)
    dark = min(l1, l2)

    return (light + 0.05) / (dark + 0.05)

def audit_tap_target(element_id: str, bbox: Optional[List[float]], min_size: float = 24.0) -> List[str]:
    """Check if the tap target meets the WCAG 2.2 recommendation of 24x24 px."""
    warnings = []
    if not bbox:
        warnings.append(f"A11Y [Tap Target]: Element '{element_id}' has no bounding box, could not verify tap target size.")
        return warnings

    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]

    # Use an approximation threshold. If both width and height are small, it's a concern.
    if width < min_size or height < min_size:
        warnings.append(f"A11Y [Tap Target]: Interactive element '{element_id}' is {width:.1f}x{height:.1f}px. WCAG 2.2 recommends at least {min_size}x{min_size}px for tap targets.")

    return warnings

def get_element_style(elem: etree._Element, prop: str) -> Optional[str]:
    """Extract a style property (like fill or stroke) from an element."""
    # Check direct attribute
    val = elem.get(prop)
    if val:
        return val

    # Check inline style string
    style_str = elem.get('style', '')
    if style_str:
        match = re.search(r"" + prop + r"\s*:\s*([^;]+)", style_str)
        if match:
            return match.group(1).strip()

    return None

def audit_contrast(element_id: str, elem: etree._Element, background_color: str = "#ffffff", min_ratio: float = 3.0) -> List[str]:
    """Check if the element's fill color has enough contrast against the background."""
    warnings = []
    fill = get_element_style(elem, 'fill')

    # If no fill or it's 'none', try stroke
    if not fill or fill.lower() == 'none':
        fill = get_element_style(elem, 'stroke')

    if not fill or fill.lower() == 'none' or fill.lower() == 'transparent':
        # Can't reliably check transparent or purely mapped elements without context
        return warnings

    ratio = calculate_contrast_ratio(fill, background_color)

    if ratio is not None:
        if ratio < min_ratio:
            warnings.append(f"A11Y [Contrast]: Element '{element_id}' color '{fill}' against background '{background_color}' has a contrast ratio of {ratio:.2f}:1. WCAG recommends at least {min_ratio}:1 for large text/UI components.")

    return warnings
