from playwright.sync_api import Page, expect

def test_ruff(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #step 1: get column list and the required index
    headers = page.get_by_role("columnheader").all_text_contents()
    print("Item List:",headers)

    #get the index of the required items
    price_column_index = headers.index("Price")
    veg_column_index = headers.index("Veg/fruit name")

    #step 2: get all table rows
    rows = page.locator("tbody tr")
    row_count = rows.count()
    print(f"total rows: {row_count}")

    #step 3 & 4: loop through rows to find rice
    for i in range(row_count):
        row = rows.nth(i)
        cells = row.locator("td").all_text_contents()

        if cells[veg_column_index] == "Rice":
            rice_price = cells[price_column_index]
            print(f"Found Rice! Price is {rice_price}")
            break

    #alternative method for nth using .all()
    #get all cells from all rows
    # all_rows = page.locator("tbody tr").all()
    # for row in all_rows:
    #     cells = row.locator("td").all_text_contents()
    #     print(cells)
    #
    #     if cells[veg_column_index] == "Rice"
    #     print(f"Price price:{cells[price_column_index]}")






