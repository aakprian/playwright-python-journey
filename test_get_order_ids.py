# test_get_order_ids.py

from playwright.sync_api import sync_playwright


def get_all_order_ids():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login first to get to orders page
        page.goto("https://rahulshettyacademy.com/client")
        page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
        page.get_by_placeholder("enter your passsword").fill("Limelight@420")
        page.get_by_role("button", name="Login").click()

        # Navigate to orders page
        page.get_by_role("button", name="ORDERS").click()

        page.wait_for_selector("tr")

        # Add this before grabbing order IDs
        all_th = page.locator("th")

        print(f"Total th elements found: {all_th.count()}")
        for i in range(all_th.count()):
            print(f"  th {i + 1}: {all_th.nth(i).text_content()}")

        # Grab all order IDs
        all_order_ids = page.locator("th[scope='row']")

        # Print all of them
        print(f"\nTotal orders found: {all_order_ids.count()}")
        print("Order IDs:")
        for i in range(all_order_ids.count()):
            order_id = all_order_ids.nth(i).text_content()
            print(f"  {i + 1}. {order_id}")

        browser.close()


if __name__ == "__main__":
    get_all_order_ids()