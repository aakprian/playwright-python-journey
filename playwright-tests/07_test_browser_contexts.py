#Browser Contexts

import pytest
from playwright.sync_api import sync_playwright



def test_understand_context():
    print("\n UNDERSTANDING CONTEXTS")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        #One browser can have multiple contexts
        context1 = browser.new_context()
        context2 = browser.new_context()
        
        print(" Created 2 contexts (like 2 incognito windows)")
        
        #context is isolated
        page1 = context1.new_page()
        page2 = context2.new_page()
        
        page1.goto("https://example.com")
        page2.goto("https://example.com")
        
        print("Both pages on example.com, but isolated!")
        
        context1.close()
        context2.close()
        browser.close()


#Testing with different users
def test_multiple_users_simulation():
    print("\n MULTIPLE USERS: Simulating 2 users")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        
        # User 1 context
        context_user1 = browser.new_context()
        page_user1 = context_user1.new_page()
        
        #User 2 context
        context_user2 = browser.new_context()
        page_user2 = context_user2.new_page()
        
        #User 1 logs in
        print("User 1: Logging in...")
        page_user1.goto("https://www.saucedemo.com")
        page_user1.fill("#user-name", "standard_user")
        page_user1.fill("#password", "secret_sauce")
        page_user1.click("#login-button")
        page_user1.wait_for_url("**/inventory.html")
        print("User 1 logged in!")
        
        #User 2 logs in (different user)
        print("User 2: Logging in...")
        page_user2.goto("https://www.saucedemo.com")
        page_user2.fill("#user-name", "problem_user")
        page_user2.fill("#password", "secret_sauce")
        page_user2.click("#login-button")
        page_user2.wait_for_url("**/inventory.html")
        print("User 2 logged in!")
        
        # Both users are logged in simultaneously!
        assert "inventory" in page_user1.url
        assert "inventory" in page_user2.url
        
        print("2 users logged in at same time!")
        
        context_user1.close()
        context_user2.close()
        browser.close()


#Testing different permissions
def test_different_permissions():
    print("\n PERMISSIONS: Admin vs Regular user")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        
        # Admin context
        admin_context = browser.new_context(
            extra_http_headers={
                'X-Role': 'admin'
            }
        )
        admin_page = admin_context.new_page()
        
        # Regular user context
        user_context = browser.new_context(
            extra_http_headers={
                'X-Role': 'user'  # Simulating regular user
            }
        )
        user_page = user_context.new_page()
        
        # navigate to same site
        admin_page.goto("https://example.com")
        user_page.goto("https://example.com")
        
        print(" Admin and user sessions running separately")
        
        admin_context.close()
        user_context.close()
        browser.close()


#Testing different device types
def test_different_devices():
    print("\n DEVICES: Desktop and Mobile")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # Desktop context
        desktop_context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        )
        desktop_page = desktop_context.new_page()
        
        # Mobile context
        mobile_context = browser.new_context(
            viewport={'width': 375, 'height': 667},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
            is_mobile=True
        )
        mobile_page = mobile_context.new_page()
        
        desktop_page.goto("https://example.com")
        mobile_page.goto("https://example.com")
        
        print(" Desktop viewport: 1920x1080")
        print(" Mobile viewport: 375x667")
        
        desktop_context.close()
        mobile_context.close()
        browser.close()


#Testing different locales
def test_different_locales():
    print("\n LOCALES: English and Spanish")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # English context
        english_context = browser.new_context(
            locale='en-US',
            timezone_id='America/New_York'
        )
        english_page = english_context.new_page()
        
        # Spanish context
        spanish_context = browser.new_context(
            locale='es-ES',
            timezone_id='Europe/Madrid'
        )
        spanish_page = spanish_context.new_page()
        
        english_page.goto("https://example.com")
        spanish_page.goto("https://example.com")
        
        print(" English locale (US)")
        print(" Spanish locale (Spain)")
        
        english_context.close()
        spanish_context.close()
        browser.close()


# CONTEXT WITH STATE SAVING
def test_context_with_storage():
    print("\n STATE SAVING: Login once, reuse later")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        
        # First context - do login
        context1 = browser.new_context()
        page1 = context1.new_page()
        
        print("First visit: Logging in...")
        page1.goto("https://www.saucedemo.com")
        page1.fill("#user-name", "standard_user")
        page1.fill("#password", "secret_sauce")
        page1.click("#login-button")
        page1.wait_for_url("**/inventory.html")
        
        # Save the state
        context1.storage_state(path="auth_state.json")
        print(" Saved login state to file")
        
        context1.close()
        
        # Second context - reuse saved state
        context2 = browser.new_context(storage_state="auth_state.json")
        page2 = context2.new_page()
        
        print("Second visit: Using saved state...")
        page2.goto("https://www.saucedemo.com/inventory.html")
        
        # Already logged in!
        assert "inventory" in page2.url
        print(" Already logged in (reused state)!")
        
        context2.close()
        browser.close()
        
        # Cleanup
        import os
        if os.path.exists("auth_state.json"):
            os.remove("auth_state.json")


# PRACTICAL
def test_why_contexts_matter():
    print("\n WHY CONTEXTS MATTER")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # Without contexts (sharing same session)
        page1 = browser.new_page()  
        page2 = browser.new_page()  
        
        page1.goto("https://example.com")
        page1.context.add_cookies([{
            'name': 'test_cookie',
            'value': 'shared_value',
            'domain': 'example.com',
            'path': '/'
        }])
        
        page2.goto("https://example.com")
        
        print(" Without separate contexts: cookies are shared")
        
        page1.close()
        page2.close()
        
        # With contexts (isolated)
        context1 = browser.new_context()
        context2 = browser.new_context()
        
        page1 = context1.new_page()
        page2 = context2.new_page()
        
        page1.goto("https://example.com")
        page1.context.add_cookies([{
            'name': 'test_cookie',
            'value': 'context1_value',
            'domain': 'example.com',
            'path': '/'
        }])
        
        page2.goto("https://example.com")
        
        print(" With separate contexts: cookies are isolated")
        
        context1.close()
        context2.close()
        browser.close()