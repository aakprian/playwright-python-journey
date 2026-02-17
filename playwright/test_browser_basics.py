import pytest
from playwright.sync_api import sync_playwright

def test_open_google():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")

    print("✅ Opened Google!")

    browser.close()
    playwright.stop()

def test_open_youtube():
    playwright = sync_playwright().start()  # Repeating same code!
    browser = playwright.chromium.launch(headless=False)  # Repeating!
    page = browser.new_page()  # Repeating!
    page.goto("https://youtube.com")
    print("✅ Opened YouTube!")
    browser.close()
    playwright.stop()

def test_open_facebook():
    playwright = sync_playwright().start()  # Repeating again!
    browser = playwright.chromium.launch(headless=False)  # Repeating again!
    page = browser.new_page()  # Repeating again!
    page.goto("https://facebook.com")
    print("✅ Opened Facebook!")
    browser.close()
    playwright.stop()