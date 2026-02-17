from playwright.sync_api import Playwright, expect

from section_10.utils.apiBase import APIUtils


def test_session(playwright:Playwright):
    api_utils = APIUtils()
    token_value = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{token_value}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()