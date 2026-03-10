import pytest
from playwright.sync_api import Page, expect

FAKE_EMPTY_ORDERS = {"data": [], "message": "No Orders"}


def intercept_and_mock_empty_orders(route):
    """
    Intercepts the orders API call and returns a fake empty response.
    Use case: test how the UI behaves when a user has no orders.
    """
    route.fulfill(json=FAKE_EMPTY_ORDERS)


def test_mock_empty_orders(page: Page):
    """
    Uses route.fulfill() to intercept the orders API response
    and replace it with a mocked empty payload.

    This tests an edge case without needing a real account with no orders.
    """
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # ── Register the intercept BEFORE the action that triggers the call ──
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_and_mock_empty_orders
    )

    page.get_by_placeholder("email@example.com").fill("asen8203@alumni.sydney.edu.au")
    page.locator("#userPassword").fill("Limelight@420")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="ORDERS").click()
    page.wait_for_load_state("networkidle")

    no_orders_text = page.locator(".mt-4").text_content()
    print(f"UI message displayed: {no_orders_text}")
    assert "No Orders" in no_orders_text