
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    print("\n🔧 SETUP: Launching browser")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)

    yield browser

    print("🧹 TEARDOWN: Closing browser")
    browser.close()
    playwright.stop()


def test_open_google(browser):
    page = browser.new_page()
    page.goto("https://google.com")
    print("✅ Opened Google!")

def test_open_youtube(browser):
    page = browser.new_page()
    page.goto("https://youtube.com")
    print("✅ Opened Youtube!")

def test_open_facebook(browser):
    page = browser.new_page()
    page.goto("https://facebook.com")
    print("✅ Opened Facebook!")

