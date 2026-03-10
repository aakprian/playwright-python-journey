from playwright.sync_api import Page

TARGET_ORDER_ID = "6711e249ae2afd4c0b9f6fb0"


def redirect_to_specific_order(route):
    """
    Intercepts an order details API call and redirects it
    to a specific known order ID using route.continue_().

    Use case: force the UI to always load a specific order
    regardless of which order the user actually clicked.
    """
    route.continue_(
        url=f"https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id={TARGET_ORDER_ID}"
    )


def test_redirect_order_request(page: Page):
    """
    Uses route.continue_() to modify a request URL mid-flight.
    Demonstrates request interception beyond simple mocking —
    useful for testing specific order states without manual setup.
    """
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # ── Register intercept before navigation ─────────────────────────────
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
        redirect_to_specific_order
    )

    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.locator("#userPassword").fill("Limelight@420")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    message = page.locator(".blink_me").text_content()
    print(f"Order status message: {message}")
    assert message is not None