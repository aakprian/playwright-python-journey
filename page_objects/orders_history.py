from page_objects.order_detail_page import detail_page


class order_history_page:

    def __init__(self, page):
        self.page = page

    def right_order_view(self,user_name):
        # Step 1: Grab all order IDs from the page
        self.page.wait_for_selector("tbody")

        all_order_ids = self.page.locator("th[scope='row']")
        if all_order_ids.count() == 0:
            print(f"No orders found for this user{user_name}")
            return None

        # Step 2: Pick the first one
        first_order_id = all_order_ids.first.text_content()
        print(f"Order ID found: {first_order_id}")

        # Step 3: Find that row and click View
        row = self.page.locator("tr").filter(has_text=first_order_id)
        row.get_by_role("button", name="View").click()
        order_detail_page = detail_page(self.page)
        return order_detail_page