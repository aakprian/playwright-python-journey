from playwright.sync_api import Page
import time

def test_hover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    time.sleep(2)
    page.get_by_role("link",name="Top").click()
    time.sleep(3)