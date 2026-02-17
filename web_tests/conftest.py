import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_session():
    print("🚀 Opening browser ONCE for ALL tests in ALL files!")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    yield browser
    print("🚀 Closing browser ONCE after ALL tests!")
    browser.close()
    playwright.stop()