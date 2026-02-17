from playwright.async_api import Page
import time

fakePayLoadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrderResponse
    )


def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.locator("#userPassword").fill("Limelight@420")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="ORDERS").click()

    page.pause()


    no_orders_text = page.locator(".mt-4").text_content()
    print(no_orders_text)
