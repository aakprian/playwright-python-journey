from playwright.async_api import Page
import time

fakePayLoadOrderResponse = {"data": [], "message": "No Orders"}

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)
    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.locator("#userPassword").fill("Limelight@420")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="ORDERS").click()
    #row = page.locator("tr").filter(has_text="6711e249ae2afd4c0b9f6fb0")
    page.get_by_role("button", name="View").first.click()
    #row.get_by_role("button",name="View").click()
    time.sleep(3)

    #
    message = page.locator(".blink_me").text_content()
    print(message)


