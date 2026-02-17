def test_google_homepage(browser_session):
    page = browser_session.new_page()
    page.goto("https://google.com")
    print("✅ Visited Google")

def test_google_search(browser_session):
    page = browser_session.new_page()
    page.goto("https://google.com")
    print("✅ Searched on Google")

