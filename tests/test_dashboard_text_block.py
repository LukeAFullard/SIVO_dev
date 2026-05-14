from src.sivo.core.dashboard import SivoDashboard

def test_add_text_block():
    dashboard = SivoDashboard()
    dashboard.add_text_block(
        block_id="test_block",
        text="Hello World",
        url="https://example.com"
    )
    assert "test_block" in dashboard.html_blocks
    assert "Hello World" in dashboard.html_blocks["test_block"]["html_content"]
    assert "https://example.com" in dashboard.html_blocks["test_block"]["html_content"]
