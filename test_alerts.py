from playwright.sync_api import Page
import time

def test_dialog(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #listner for dialog
    page.on("dialog", lambda dialog: dialog.accept())

    # def handle_dialog(dialog):
    #     time.sleep(2)  # Wait 2 seconds
    #     dialog.accept()
    #
    # page.on("dialog", handle_dialog)

    #option 1 fill by placeholder
    #page.get_by_placeholder("Enter Your Name").fill("Cake On")

    #option 2 fill by get_by_role
    #page.get_by_role("textbox", name="Enter Your Name").fill("Cake On")

    #option 3 fill by get_by_label not available

    #option 4 fill by get_by_locator
    page.locator("#name").fill("Cake On")
    time.sleep(2)

    ##option for confirm button
    #page.locator("#confirmbtn").click()
    #page.locator(".btn-style").click()
    #page.locator("[type='submit']").click()
    #page.locator("[value='Confirm']").click()

    #get_by_role
    page.get_by_role("button",name="Confirm").click()
    time.sleep(2)





