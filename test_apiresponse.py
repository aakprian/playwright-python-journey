from playwright.sync_api import Playwright
import time

def test_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    #step1: login
    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.get_by_placeholder("enter your passsword").fill("Limelight@420")

    page.get_by_role("button",name="Login").click()
    time.sleep(3)

    #order submission api

