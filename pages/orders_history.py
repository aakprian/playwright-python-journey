from pages.order_detail_page import DetailPage


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def get_first_order(self, user_name):
        """
        Waits for orders table to load, grabs the first order ID,
        finds its row and clicks View — returns DetailPage.
        """
        self.page.wait_for_selector("tbody")

        all_order_ids = self.page.locator("th[scope='row']")
        if all_order_ids.count() == 0:
            print(f"No orders found for user: {user_name}")
            return None

        first_order_id = all_order_ids.first.text_content()
        print(f"Order ID found: {first_order_id}")

        row = self.page.locator("tr").filter(has_text=first_order_id)
        row.get_by_role("button", name="View").click()

        return DetailPage(self.page)