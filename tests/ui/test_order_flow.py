import pytest
from playwright.sync_api import expect
from pages.login import LoginPage
from conftest import user_cred


@pytest.mark.parametrize("user_credentials", user_cred, indirect=True)
def test_order_flow_end_to_end(browser_instance, user_credentials):
    """
    End to end UI test using Page Object Model.

    Flow:
    1. Login via LoginPage
    2. Navigate to Orders via Dashboard
    3. Select first order via OrderHistoryPage
    4. Confirm order details via DetailPage

    Each step returns the next page object — this is method chaining in POM.
    """
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    # ── POM chain ─────────────────────────────────────────────────────────
    login_page = LoginPage(browser_instance)
    dashboard = login_page.login(user_email, user_password)
    orders_page = dashboard.navigate_to_orders()
    detail_page = orders_page.get_first_order(user_email)
    detail_page.confirm_order_placed()

