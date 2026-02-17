from page_objects.dashboard import Dashboard


class LoginPage:

    def __init__(self,page):
        self.page = page



    def navigate(self,):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,user_email,user_password):
        self.page.get_by_placeholder("email@example.com").fill(user_email)
        self.page.get_by_placeholder("enter your passsword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = Dashboard(self.page)
        return dashboard_page

