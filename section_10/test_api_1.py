from playwright.sync_api import Playwright, expect
import time

from utils.apiBase import APIUtils


#launch and get to the website
def test_web_api(playwright:Playwright):

    # create order -> orderID
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)
    print(f"Order created with ID: {order_id}")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")


    #step1 login
    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.locator("#userPassword").fill("Limelight@420")

    page.get_by_role("button",name="Login").click()
    page.wait_for_load_state("networkidle")

    #orders history page -> order is present.
    page.get_by_role("button", name= "ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()
    browser.close()
