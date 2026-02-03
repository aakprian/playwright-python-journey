"""
My First Playwright Test
Day 1 - Basic navigation and assertions
"""
from playwright.sync_api import sync_playwright


def test_example_site():
    """Test basic navigation to example.com"""
    with sync_playwright() as p:
        # Launch browser (headless=False lets you see it)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to website
        page.goto("https://example.com")

        # Verify the title
        assert "Example Domain" in page.title()
        print(f"✅ Title verified: {page.title()}")

        # Verify heading text
        heading = page.inner_text("h1")
        assert heading == "Example Domain"
        print(f"✅ Heading verified: {heading}")

        # Get and verify paragraph text
        paragraph = page.inner_text("p")
        print(f"📝 Paragraph found: {paragraph[:50]}...")

        print("\n🎉 Test passed successfully!")

        browser.close()


if __name__ == "__main__":
    test_example_site()