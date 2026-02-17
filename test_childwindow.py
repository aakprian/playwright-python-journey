import time

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import playwright


def test_child_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page:
        page.locator(".blinkingText").click()

    child_page = new_page.value
    text = child_page.locator(".red").text_content()
    print(text)

    result = text.split()

    capture = ""
    for element in result:
        if "@" in element:  # Notice the quotes!
            capture = element

    print(capture.strip("."))
    assert capture == "mentor@rahulshettyacademy.com"
