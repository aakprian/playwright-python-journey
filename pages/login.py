from pages.dashboard import Dashboard


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        """
        Navigates to the application login page.
        """
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, user_email, user_password):
        """
        Fills in credentials and clicks Login.
        Returns Dashboard page object on success.
        """
        self.page.get_by_placeholder("email@example.com").fill(user_email)
        self.page.get_by_placeholder("enter your passsword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_load_state("networkidle")
        return Dashboard(self.page)