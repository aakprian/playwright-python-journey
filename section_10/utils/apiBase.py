from playwright.sync_api import Playwright

orders_payload = '{"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}'

class APIUtils:

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        login_response = api_request_context.post(
            "/api/ecom/auth/login",
            data='{"userEmail": "asen8203@alumni.sydney.edu.au", "userPassword": "Limelight@420"}',
            headers={"Content-Type": "application/json"}  # <-- HYPHEN!
        )

        # DEBUG LINES:
        print(f"Status Code: {login_response.status}")
        print(f"Response: {login_response.text()}")

        assert login_response.ok
        print(login_response.json())
        response_body = login_response.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        new_api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = new_api_context.post(
            "/api/ecom/order/create-order",
            data=orders_payload,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"  # <-- HYPHEN!
            }
        )

        response_body = response.json()
        print(response.json())
        order_id = response_body["orders"][0]
        return order_id