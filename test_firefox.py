from playwright.sync_api import Page, expect, Playwright


# def test_wrong_cred(page:Page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.get_by_label("Username:").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill("learnifdfd")
#     page.get_by_role("combobox").select_option("teach")
#     page.locator("#terms").check()
#     page.get_by_role("link",name="terms and conditions").click()
#     page.get_by_role("button",name="Sign In").click() #Incorrect username/password.
#     expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

# def test_firefox(playwright:Playwright):
#     browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://google.com")


def test_fox(playwright:Playwright):
    fire_browser = playwright.firefox
    browser = fire_browser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learnifdfd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()  # Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()