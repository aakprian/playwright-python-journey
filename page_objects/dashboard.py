from page_objects.orders_history import order_history_page


class Dashboard:

    def __init__(self,page):
        self.page = page


    def select_orders_nav_link(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orders_page = order_history_page(self.page)
        return orders_page