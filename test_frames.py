from playwright.sync_api import Page, expect
import time

def test_frames(page:Page):
    # page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # pageFrame = page.frame_locator("#course_iframe")
    # pageFrame.get_by_role("link", name="NEW All Access Plan").click()
    #
    # #assert text
    # expect(pageFrame.get_by_role("heading")).to_contain_text("Happy Subscibers")
    # time.sleep(3)


    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    pageFrame = page.frame_locator("#courses-iframe")

    pageFrame.get_by_role("link",name="NEW All Access Plan").click()



    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")