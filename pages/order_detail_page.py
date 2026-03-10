from playwright.sync_api import expect


class DetailPage:

    def __init__(self, page):
        self.page = page

    def confirm_order_placed(self):
        """
        Asserts the thank you message is visible after order placement.
        """
        expect(self.page.locator(".tagline")).to_contain_text(
            "Thank you for Shopping With Us"
        )

    def get_delivery_details(self):
        """
        Extracts and prints all delivery address details from the order.
        """
        address = self.page.locator(".address").first
        all_details = address.locator(".text")
        for i in range(all_details.count()):
            print(f"{all_details.nth(i).text_content()}")