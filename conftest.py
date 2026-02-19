import pytest
import json

from playwright.sync_api import Playwright
from pygments.lexer import default

from yield_examples.exploring_yield import browser

with open('section_10/data/credentials.json') as f:
    test_data = json.load(f)
    user_cred = test_data["user_credentials"]


@pytest.fixture(scope="function")
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store",default="chrome"
    )

    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client"
    )


@pytest.fixture(scope="function")
def browser_instance(playwright:Playwright,request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name =="firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)


    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser.close()



#   browser= playwright.chromium.launch(headless=False)
#   context = browser.new_context()
#   page = context.new_page()
