#web tables
from playwright.sync_api import Page

def test_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        #page.locator("th").nth(i).text_content()
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            price_column_value = i
            print(f"Price column value is {price_column_value}")
            break

    rice_row = page.locator("tr").filter(has_text= "Rice")
    rice_cells = rice_row.locator("td").all_text_contents()
    #rice_row.locator("td").nth(price_column_value)
    rice_price = rice_cells[price_column_value]
    print(f"Rice price: {rice_price}")

















