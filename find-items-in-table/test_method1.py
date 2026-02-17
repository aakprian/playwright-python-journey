#web table finding content in a dynamic setup
#not dynamic enough
from playwright.sync_api import Page, expect

def test_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #get column headers
    headers = page.get_by_role("columnheader").all_text_contents()
    print("Headers:", headers)

    #find which column has price
    price_column_index = headers.index("Price")
    print(f"Price is at column index: {price_column_index}")

    # Step 2: Get all table rows (data rows, not header)
    rows = page.locator("tbody tr")  # tbody contains the data rows
    row_count = rows.count()
    print(f"Total rows: {row_count}")

    #Step 3 & 4 : Loop through rows to find Rice
    for i in range(row_count):
        row = rows.nth(i)
        cells = row.locator("td").all_text_contents()
        print(f"Row {i}: {cells}")

        #check if the row contains rice
        if cells[0] == "Rice":
            rice_price = cells[price_column_index]
            print(f"Found Rice! Price is: {rice_price}")
            break

