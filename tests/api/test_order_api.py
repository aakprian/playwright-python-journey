import pytest
from playwright.sync_api import Playwright, expect
from utils.api_utils import APIUtils
from conftest import user_cred


@pytest.mark.parametrize("user_credentials", user_cred, indirect=True)
def test_create_order_and_verify_in_ui(playwright: Playwright, user_credentials):
    """
    Hybrid test — creates an order via API then validates it in the UI.

    Why this pattern?
    - API call creates test data instantly (no slow UI form filling)
    - UI validation confirms the full stack is working end to end
    - This is the gold standard for modern SDET test design
    """
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    # ── Step 1: Create order via API ─────────────────────────────────────
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_email, user_password)
    print(f"Order created via API: {order_id}")

    # ── Step 2: Login via UI ──────────────────────────────────────────────
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill(user_email)
    page.locator("#userPassword").fill(user_password)
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")

    # ── Step 3: Navigate to orders and find the API-created order ─────────
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()

    # ── Step 4: Assert order confirmation ────────────────────────────────
    expect(page.locator(".tagline")).to_have_text(
        "Thank you for Shopping With Us"
    )
    print(f"Order {order_id} verified successfully in UI")

    context.close()
    browser.close()