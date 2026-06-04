from src.sivo.core.dashboard import SivoDashboard
import os

db = SivoDashboard(title="Test")
db.add_text_block(block_id="test", text="Test")
db.to_html(output_path="test_scroll.html")
