

from playwright.sync_api import Page, expect

# we can write a css selector with an id, class name and tag-name
def test_ui_validation_dynamic_script(page:Page):
    #need to pick two products
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    iphone_Product = page.locator("app-card").filter(has_text="iphone x")
    iphone_Product.get_by_role("button").click()
    nokia_Product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_Product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

