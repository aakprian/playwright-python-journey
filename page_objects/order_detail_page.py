from playwright.sync_api import expect


class detail_page():

    def __init__(self, page):
        self.page = page

    def confirm_order_placement(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    def get_delivery_details(self):
        address = self.page.locator(".address").first
        all_delivery_details = address.locator(".text")
        for i in range(all_delivery_details.count()):
            print(f"{all_delivery_details.nth(i).text_content()}")
