
#Browser Fixture with Playwright

import pytest
from playwright.sync_api import sync_playwright


#BASIC BROWSER FIXTURE
@pytest.fixture
def browser():
    print("\n SETUP: Launching Chromium browser")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False, 
        slow_mo=500     
    )
    
    yield browser 
    
    print("TEARDOWN: Closing browser")
    browser.close()
    playwright.stop()


#Basic navigation
def test_navigate_to_google(browser):
    print("TEST: Navigating to Google")
    
    page = browser.new_page()
    page.goto("https://google.com")
    
    assert "Google" in page.title()
    print(f" Page title: {page.title()}")
    
    page.close()


#Navigate to multiple sites
def test_navigate_to_youtube(browser):
    print("TEST: Navigating to YouTube")
    
    page = browser.new_page()
    page.goto("https://youtube.com")
    
    assert "YouTube" in page.title()
    print(f"Page title: {page.title()}")
    
    page.close()


#Check URL
def test_navigate_to_github(browser):
    print("TEST: Navigating to GitHub")
    
    page = browser.new_page()
    page.goto("https://github.com")
    
    assert "github.com" in page.url
    print(f"Current URL: {page.url}")
    
    page.close()


#Browser fixture with options
@pytest.fixture
def browser_with_options():
    print("\nSETUP: Launching browser with custom options")
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000,  # Even slower for debugging
        args=[
            '--start-maximized',
        ]
    )
    
    yield browser
    
    print("TEARDOWN: Closing configured browser")
    browser.close()
    playwright.stop()


def test_with_custom_browser(browser_with_options):
    print("TEST: Using customized browser")
    
    page = browser_with_options.new_page()
    page.goto("https://example.com")
    
    assert "Example Domain" in page.content()
    print("Custom browser works!")
    
    page.close()


#Without fixture (messy!)
def test_without_fixture_messy():
    print("\n WITHOUT FIXTURE: Repeating all setup code")
   
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://example.com")
    assert "Example" in page.title()
    
    browser.close()
    playwright.stop()
    
    print("Test passed")