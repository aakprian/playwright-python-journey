import json
import pytest
from pytest_bdd import given, when, then, scenario
from pages.login import LoginPage

# ── Load credentials from test_data.json ────────────────────────────────────
with open("data/test_data.json") as f:
    test_data = json.load(f)
    credentials = test_data["user_credentials"][0]


@scenario("../features/order_flow.feature", "Verify order confirmation message after login")
def test_order_flow():
    """BDD scenario: full order flow from login to confirmation."""
    pass


@given("the user is on the login page", target_fixture="login_page")
def user_on_login_page(page):
    """
    Uses pytest-playwright's built-in page fixture.
    Navigates to the login page and returns a LoginPage object.
    """
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    return LoginPage(page)


@when("I login with valid credentials", target_fixture="dashboard")
def login(login_page):
    """
    Logs in using credentials from test_data.json.
    Returns the Dashboard page object.
    """
    return login_page.login(
        credentials["user_email"],
        credentials["user_password"]
    )


@when("I navigate to the orders page", target_fixture="orders_page")
def navigate_to_orders(dashboard):
    """
    Clicks ORDERS nav and returns OrderHistoryPage.
    """
    return dashboard.navigate_to_orders()


@when("I select the first order", target_fixture="detail_page")
def select_first_order(orders_page):
    """
    Selects the first order from the orders table.
    Returns DetailPage.
    """
    return orders_page.get_first_order(credentials["user_email"])


@then("the order confirmation message is displayed")
def verify_confirmation(detail_page):
    """
    Asserts the thank you message is visible on the order detail page.
    """
    detail_page.confirm_order_placed()