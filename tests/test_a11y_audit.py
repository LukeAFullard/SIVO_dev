import pytest
import tempfile
import os
import logging
from src.sivo import Sivo
from src.sivo.core.a11y_audit import calculate_contrast_ratio

def test_contrast_ratio_calculation():
    # White vs Black should be exactly 21.0
    assert abs(calculate_contrast_ratio("#ffffff", "#000000") - 21.0) < 0.1
    # White vs White should be exactly 1.0
    assert abs(calculate_contrast_ratio("#ffffff", "#ffffff") - 1.0) < 0.1

def test_a11y_audit_warnings(caplog):
    caplog.set_level(logging.WARNING, logger="sivo.a11y")

    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- Small tap target -->
        <rect id="btn1" x="10" y="10" width="10" height="10" fill="#ffffff" />

        <!-- Good tap target, bad contrast against white background -->
        <rect id="btn2" x="10" y="30" width="30" height="30" fill="#f0f0f0" />

        <!-- Good target, good contrast -->
        <rect id="btn3" x="10" y="70" width="30" height="30" fill="#000000" />
    </svg>"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as f:
        f.write(svg_content)
        tmp_path = f.name

    try:
        app = Sivo.from_svg(tmp_path, enable_a11y=True)
        app.map("btn1", url="https://example.com")
        app.map("btn2", url="https://example.com")
        app.map("btn3", url="https://example.com")

        # This should trigger the audit warnings
        app.audit_a11y()

        warnings = caplog.text

        # Assert specific warnings are present
        assert "btn1' is 10.0x10.0px" in warnings
        assert "btn1' color '#ffffff' against background '#ffffff' has a contrast ratio of 1.00:1" in warnings
        assert "btn2' color '#f0f0f0' against background '#ffffff' has a contrast ratio of 1.14:1" in warnings
        assert "btn3" not in warnings  # btn3 should have no warnings

    finally:
        os.remove(tmp_path)
