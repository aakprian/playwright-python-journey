import pytest
from playwright.sync_api import Playwright, expect

from conftest import user_cred
from utils.apiBase import APIUtils


#launch and get to the website
@pytest.mark.parametrize("user_credentials",user_cred,indirect=True)
def test_web_api(playwright:Playwright,user_credentials):
    # Extract the email and password
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]


    # create order -> orderID
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_email, user_password)
    print(f"Order created with ID: {order_id}")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")


    #step1 login
    page.get_by_placeholder("email@example.com").fill(user_email)
    page.locator("#userPassword").fill(user_password)

    page.get_by_role("button",name="Login").click()
    page.wait_for_load_state("networkidle")

    #orders history page -> order is present.
    page.get_by_role("button", name= "ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()
    browser.close()
