#web tables
from playwright.sync_api import Page, expect

def test_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    headers = page.get_by_role("columnheader").all_text_contents()

    print(headers)

    #option 2 for loop
    for i in range(page.locator("th").count()):
        #page.locator("th").nth(i).text_content()
        if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
            price_colValue = index
            print(f"price column value is {price_colValue}")
            break

    row = page.locator("tr").filter(has_text = "Rice")






