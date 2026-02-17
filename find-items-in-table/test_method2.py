#dynamic enough
from playwright.sync_api import Page

def test_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Step 1: Find column indices
    headers = page.get_by_role("columnheader").all_text_contents()
    price_column_index = headers.index("Price")
    veg_name_column_index = headers.index("Veg/fruit name")

    print(f"Veg/fruit name is at column index: {veg_name_column_index}")
    print(f"Price is at column index: {price_column_index}")

    # Step 2: Get all table rows
    rows = page.locator("tbody tr")
    row_count = rows.count()

    # Step 3 & 4: Loop through rows to find Rice
    for i in range(row_count):
        row = rows.nth(i)
        cells = row.locator("td").all_text_contents()

        #dynamic index instead of hard-coded 0
        if cells[veg_name_column_index] == "Rice":
            rice_price = cells[price_column_index]
            print(f"Found Rice! Price is: {rice_price}")
            break