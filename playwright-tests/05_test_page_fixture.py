#Page Fixture

import pytest
from playwright.sync_api import sync_playwright


#Manual browser
@pytest.fixture(scope="module")
def manual_browser():
    print("\n MANUAL: Launching browser")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    
    yield browser
    
    print("🔧 MANUAL: Closing browser")
    browser.close()
    playwright.stop()


def test_with_manual_browser(manual_browser):
    print("TEST: Creating page manually")
    page = manual_browser.new_page()
    page.goto("https://example.com")
    
    assert "Example Domain" in page.title()
    print(f" Title: {page.title()}")
    
    page.close()


#Using Playwright's built-in fixtures
def test_with_playwright_fixture(playwright):
    print("\n BUILT-IN: Using playwright fixture")
    
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://google.com")
    
    assert "Google" in page.title()
    print(f" Title: {page.title()}")
    
    browser.close()


def test_with_browser_fixture(browser):
    print("\n BUILT-IN: Using browser fixture")
    
    page = browser.new_page()
    page.goto("https://youtube.com")
    
    assert "YouTube" in page.title()
    print(f" Title: {page.title()}")
    
    page.close()


def test_with_page_fixture(page):
    print("\n BUILT-IN: Using page fixture (easiest!)")
    
    page.goto("https://github.com")
    
    assert "github.com" in page.url
    print(f" URL: {page.url}")
    


# UNDERSTANDING FIXTURES
def test_playwright_fixture_details(playwright):
    print("\n🔍 EXPLORING: playwright fixture")
    
    print(f"Type: {type(playwright)}")
    print(f"Available browsers: chromium, firefox, webkit")
    
    # Launch different browsers
    chromium = playwright.chromium.launch(headless=False)
    print("Chromium launched")
    
    page = chromium.new_page()
    page.goto("https://example.com")
    
    chromium.close()


def test_browser_fixture_details(browser):
    print("\n EXPLORING: browser fixture")
    
    print(f"Browser type: {type(browser)}")
    print(f"Browser is already launched!")
    
    # Create multiple pages in same browser
    page1 = browser.new_page()
    page2 = browser.new_page()
    
    page1.goto("https://google.com")
    page2.goto("https://github.com")
    
    print(f" Page 1: {page1.title()}")
    print(f" Page 2: {page2.title()}")
    
    page1.close()
    page2.close()


def test_page_fixture_details(page):
    print("\n EXPLORING: page fixture")
    
    print(f"Page type: {type(page)}")
    print(f"Browser and page already launched!")
    
    page.goto("https://playwright.dev")
    
    # page info
    print(f"URL: {page.url}")
    print(f"Title: {page.title()}")


# COMPARISON
def test_comparison_manual():
    print("\n COMPARISON: Manual")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://example.com")
    assert "Example" in page.title()
    
    browser.close()
    playwright.stop()


def test_comparison_browser_fixture(browser):
    print("\n COMPARISON: Browser fixture")
    page = browser.new_page()
    
    page.goto("https://example.com")
    assert "Example" in page.title()
    
    page.close()


def test_comparison_page_fixture(page):
    print("\n COMPARISON: Page fixture (winner!)")
    
    page.goto("https://example.com")
    assert "Example" in page.title()
    


# Real test using page fixture
def test_real_scenario_login(page):
    print("\n REAL SCENARIO: Login test")
    
    # Navigate to login page
    page.goto("https://www.saucedemo.com")
    
    # Fill login form
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    
    # Click login
    page.click("#login-button")
    
    # Verify login success
    page.wait_for_url("**/inventory.html")
    assert "inventory.html" in page.url
    
    print(" Login successful!")


def test_real_scenario_search(page):
    print("\n REAL SCENARIO: Search test")
    
    page.goto("https://www.google.com")
    
    #Handle cookie consent
    try:
        page.click("text=Accept all", timeout=2000)
    except:
        pass
    
    # Search
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    
    # Wait for results
    page.wait_for_selector("#search")
    
    print("Search completed!")