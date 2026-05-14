from src.sivo.core.dashboard import SivoDashboard

def test_add_text_block():
    dashboard = SivoDashboard()
    dashboard.add_text_block(
        block_id="test_block",
        text="Hello World",
        url="https://example.com"
    )
    assert "test_block" in dashboard.html_blocks
    html_content = dashboard.html_blocks["test_block"].get("html_content", "")
    assert "Hello World" in html_content
    assert "https://example.com" in html_content
