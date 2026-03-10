from playwright.sync_api import Playwright

BASE_URL = "https://rahulshettyacademy.com"

ORDERS_PAYLOAD = {
    "orders": [
        {"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}
    ]
}


class APIUtils:

    def get_token(self, playwright: Playwright, user_email: str, user_password: str) -> str:
        """
        Authenticates via the login API and returns a JWT token.
        Uses Playwright's API request context — no browser needed.
        """
        api_context = playwright.request.new_context(base_url=BASE_URL)
        login_payload = {
            "userEmail": user_email,
            "userPassword": user_password
        }
        response = api_context.post(
            "/api/ecom/auth/login",
            data=str(login_payload).replace("'", '"'),
            headers={"Content-Type": "application/json"}
        )
        assert response.ok, f"Login failed with status: {response.status}"
        token = response.json()["token"]
        print(f"Token retrieved successfully")
        return token

    def create_order(self, playwright: Playwright, user_email: str, user_password: str) -> str:
        """
        Creates an order via API using an authenticated token.
        Returns the order ID for use in UI validation tests.

        This pattern (API setup → UI validation) avoids slow UI-based
        test data creation and keeps tests fast and reliable.
        """
        token = self.get_token(playwright, user_email, user_password)
        api_context = playwright.request.new_context(base_url=BASE_URL)

        import json
        response = api_context.post(
            "/api/ecom/order/create-order",
            data=json.dumps(ORDERS_PAYLOAD),
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )
        assert response.ok, f"Order creation failed with status: {response.status}"
        order_id = response.json()["orders"][0]
        print(f"Order created: {order_id}")
        return order_id