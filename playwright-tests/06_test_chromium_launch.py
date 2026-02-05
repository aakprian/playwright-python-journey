#Chromium Browser with Playwright

import pytest
from playwright.sync_api import sync_playwright



def test_basic_launch_headless():
  
    print("\n HEADLESS MODE: Browser runs in background")
    
    with sync_playwright() as p:
        browser = p.chromium.launch() 
        page = browser.new_page()
        page.goto("https://example.com")
        
        assert "Example Domain" in page.title()
        print(f"Title: {page.title()}")
        print("Test complete (you didn't see browser open!)")
        
        browser.close()


def test_launch_headed():
    
    print("\nHEADED MODE: Browser window visible")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        
        assert "Google" in page.title()
        print(f"Title: {page.title()}")
        print("You saw the browser open!")
        
        browser.close()


def test_launch_with_slow_mo():
    print("\n SLOW MOTION: Slowing down actions")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000  # Wait (1 second)
        )
        page = browser.new_page()
        
        print("Watch the browser navigate slowly")
        page.goto("https://example.com")
        page.click("text=More information")
        
        print("Actions completed in slow motion!")
        browser.close()


def test_launch_with_viewport():
    print("\n CUSTOM VIEWPORT: Mobile size simulation")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        #Create context with mobile viewport
        context = browser.new_context(
            viewport={'width': 375, 'height': 667},  # iPhone SE
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
        )
        page = context.new_page()
        
        page.goto("https://example.com")
        
        print(f" Viewport: 375x667 (mobile)")
        print(f" URL: {page.url}")
        
        browser.close()


#Advanced browser options
def test_launch_with_args():
    print("\n CHROME ARGS: Advanced browser settings")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--start-maximized',      
                '--disable-blink-features=AutomationControlled',
            ]
        )
        page = browser.new_page()
        page.goto("https://example.com")
        
        print("Browser started with custom arguments")
        browser.close()


#Set launch timeout
def test_launch_with_timeout():
    print("\n TIMEOUT: Custom launch timeout")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            timeout=60000  #60 seconds to launch
        )
        page = browser.new_page()
        page.goto("https://example.com")
        
        print(" Browser launched within timeout")
        browser.close()


def test_launch_chrome_channel():
    print("\n CHANNEL: Using Chrome stable")
    
    with sync_playwright() as p:
        try:
            #Use system Chrome instead of bundled Chromium
            browser = p.chromium.launch(
                headless=False,
                channel="chrome"
            )
            page = browser.new_page()
            page.goto("https://example.com")
            
            print(" Using system Chrome browser")
            browser.close()
        except Exception as e:
            print(f" System Chrome not available: {e}")


# COMPARISON
@pytest.mark.parametrize("mode,config", [
    ("headless", {"headless": True}),
    ("headed", {"headless": False}),
    ("slow_mo", {"headless": False, "slow_mo": 500}),
])
def test_launch_modes_comparison(mode, config):
    print(f"\n TESTING MODE: {mode}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(**config)
        page = browser.new_page()
        page.goto("https://example.com")
        
        assert "Example" in page.title()
        print(f" {mode} mode works!")
        
        browser.close()


def test_best_config_for_learning():
    print("\n LEARNING CONFIG:settings for beginners")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,    
            slow_mo=500,       
        )
        
        page = browser.new_page()
        
        # Navigate and interact
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        # Verify
        page.wait_for_url("**/inventory.html")
        assert "inventory" in page.url
        
        print(" Perfect config for learning!")
        browser.close()


#config for CI/CD
def test_best_config_for_cicd():
    print("\n CI/CD CONFIG: Best for automation")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,           
        )
        
        page = browser.new_page()
        page.goto("https://example.com")
        
        assert "Example" in page.title()
        print("Fast and efficient for CI/CD!")
        
        browser.close()