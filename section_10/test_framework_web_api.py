import json
import pytest
from playwright.sync_api import Playwright
#create a json file ->


#json file -> utils -> access to test
with open('section_10/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]


# for user in test_data["user_credentials"]:
#     #each 'user' is one dictionary from the list
#     email = user["user_email"]
#     password = user["user_password"]

@pytest.mark.parametrize("user_details", user_credentials_list)
def test_framework1(playwright:Playwright, user_details):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    page.get_by_placeholder("email@example.com").fill(user_details["user_email"])
    page.locator("#userPassword").fill(user_details["user_password"])

    page.get_by_role("button", name="Login").click()
    #page.wait_for_load_state("networkidle")

