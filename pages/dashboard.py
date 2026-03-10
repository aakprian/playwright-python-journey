from pages.orders_history import OrderHistoryPage


class Dashboard:

    def __init__(self, page):
        self.page = page

    def navigate_to_orders(self):
        """
        Clicks the ORDERS nav button and returns OrderHistoryPage.
        """
        self.page.get_by_role("button", name="ORDERS").click()
        return OrderHistoryPage(self.page)