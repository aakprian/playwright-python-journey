def test_facebook_homepage(browser_session):
    page = browser_session.new_page()
    page.goto("https://facebook.com")
    print("✅ Visited Facebook")
