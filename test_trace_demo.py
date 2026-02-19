def test_with_page_fixture(page):
    """Simple test using page fixture"""
    page.goto("https://www.google.com")
    assert "Google" in page.title()
