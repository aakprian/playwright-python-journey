@pytest.fixture
def logged_in_user(browser):
    # SETUP: Login
    print("Logging in...")
    page = browser.new_page()
    page.goto("https://example.com/login")
    page.fill("#username", "testuser")
    page.fill("#password", "testpass")
    page.click("#login-button")

    yield page  # Give logged-in page to test

    # TEARDOWN: Logout
    print("Logging out...")
    page.click("#logout-button")
    page.close()


def test_dashboard(logged_in_user):
    # Test already logged in!
    assert "Dashboard" in logged_in_user.title()