import pytest
import json
from playwright.sync_api import Playwright


# ── Load test data ──────────────────────────────────────────────────────────
with open("data/test_data.json") as f:
    test_data = json.load(f)
    user_cred = test_data["user_credentials"]


# ── CLI options ─────────────────────────────────────────────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Browser to run tests on: chrome | firefox | webkit"
    )
    parser.addoption(
        "--url", action="store", default="https://rahulshettyacademy.com/client",
        help="Base URL for the application under test"
    )


# ── Browser fixture (function scope = fresh browser per test) ────────────────
@pytest.fixture(scope="function")
def browser_instance(playwright: Playwright, request):
    """
    Launches a browser based on --browser_name CLI option.
    Yields a page object and tears down after each test.

    Scope: function — each test gets a clean isolated browser session.
    Use session scope only for read-only shared state (e.g. auth tokens).
    """
    browser_name = request.config.getoption("browser_name")
    url = request.config.getoption("url")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    yield page  # hand the page to the test

    # teardown — runs after every test automatically
    context.close()
    browser.close()


# ── Parametrized user credentials fixture ───────────────────────────────────
@pytest.fixture(scope="function")
def user_credentials(request):
    """
    Used with @pytest.mark.parametrize to inject user credentials
    from test_data.json into tests indirectly.
    """
    return request.param