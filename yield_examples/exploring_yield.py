import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    print("🔧 SETUP: Starting Playwright and opening browser")

    # SETUP (happens BEFORE test)
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)

    yield browser  # ← PAUSE! Give browser to test

    # TEARDOWN (happens AFTER test)
    print("🧹 TEARDOWN: Closing browser and stopping Playwright")
    browser.close()
    playwright.stop()


def test_visit_google(browser):
    print("🧪 TEST: Opening Google")
    page = browser.new_page()
    page.goto("https://google.com")
    assert "Google" in page.title()
    print("✅ TEST: Done!")

