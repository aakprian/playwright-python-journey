def test_youtube_homepage(browser_session):
    page = browser_session.new_page()
    page.goto("https://youtube.com")
    print("✅ Visited YouTube")

def test_youtube_trending(browser_session):
    page = browser_session.new_page()
    page.goto("https://youtube.com/trending")
    print("✅ Checked YouTube trending")