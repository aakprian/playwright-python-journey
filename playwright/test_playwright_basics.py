

def test_play_wright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() #
    page = context.new_page()
    page.goto("https://google.com")

    