import sys

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Let's see what Sediment has in its TEMPLATE
    # We want Improving to be 3DB7E9, Indeterminate to be F0E442, Degrading to be E69F00

    # But wait, looking at Sediment/trend_placeholder_TEMPLATE.md
    # It has:
    # <th style="padding: 8px; border-bottom: 2px solid #ddd; background-color: #2abeff; color: black;">Improving</th>
    # <th style="padding: 8px; border-bottom: 2px solid #ddd; background-color: #e6e600; color: black;">Indeterminate</th>
    # <th style="padding: 8px; border-bottom: 2px solid #ddd; background-color: #ff6767; color: black;">Degrading</th>
    # And then for Whole Region:
    # <td style="padding: 8px; border-bottom: 1px solid #ddd; background-color: #3DB7E9; color: black;">|REGION_IMPROVING_PCT|% (|REGION_IMPROVING_COUNT|)</td>
    # <td style="padding: 8px; border-bottom: 1px solid #ddd; background-color: #F0E442; color: black;">|REGION_INDETERMINATE_PCT|% (|REGION_INDETERMINATE_COUNT|)</td>
    # <td style="padding: 8px; border-bottom: 1px solid #ddd; background-color: #E69F00; color: black;">|REGION_DEGRADING_PCT|% (|REGION_DEGRADING_COUNT|)</td>
    pass
