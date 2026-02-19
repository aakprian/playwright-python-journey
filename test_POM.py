import pytest
from playwright.sync_api import Playwright
from conftest import user_credentials, user_cred, browser_instance
from page_objects.login import LoginPage



@pytest.mark.parametrize("user_credentials", user_cred, indirect=True)
def test_POM(playwright:Playwright, browser_instance, user_credentials):
    user_name = user_credentials["user_email"]
    user_password = user_credentials["user_password"]


    login_page = LoginPage(browser_instance)

    #login
    login_page.navigate()
    dashboard_page = login_page.login(user_name,user_password)

    #click orders link
    orders_page = dashboard_page.select_orders_nav_link()
    order_detail_page =orders_page.right_order_view(user_name)

    if order_detail_page is None:
        print(f"Skipping - no orders for {user_name}")
    else:
        order_detail_page.confirm_order_placement()
        order_detail_page.get_delivery_details()




