import time
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
import pytest

link_log = "http://demowebshop.tricentis.com/login"

@pytest.mark.smoke
def test_successful_login(browser):
    email = "привет234@g1mail.com"
    password = "привет234@g1mail.com"
    page = LoginPage(browser, link_log)
    page.open()
    page.enter_email_field(email)
    page.enter_password_field(password)
    page.click_button_log_in()
    page.verification_email()
    page.verification_log_in()
    page.verification_login_failed()

@pytest.mark.register_new
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f_name = "Ivan"
        l_name = "Zasyadko"
        email = str(time.time()) + "@fakemail.org"
        password = "ggga!Q24"
        confirm_password = password
        page = RegisterPage(browser, 'http://demowebshop.tricentis.com/register')
        page.open()
        page.choose_gender_male()
        page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
        page.click_button_register()
        return email, password

    def test_successful_login_new_user(self, browser, setup):
        page = LoginPage(browser, link_log)
        page.open()
        page.enter_email_field(setup[0])
        page.enter_password_field(setup[1])
        page.click_button_log_in()
        page.verification_email()
        page.verification_log_in()
        page.verification_login_failed()

    def test_login_not_non_existent_password(self, browser, setup):
        page = LoginPage(browser, link_log)
        page.open()
        email = setup[0]
        password = setup[1] + '124'
        page.enter_email_field(email)
        page.enter_password_field(password)
        page.click_button_log_in()
        page.verification_email()
        page.verification_non_existent_password()

def test_login_not_non_existent_email(browser):
    page = LoginPage(browser, link_log)
    page.open()
    email = "5приве13214т234@g1mail.com"
    password = "привет234@g1mail.com"
    page.enter_email_field(email)
    page.enter_password_field(password)
    page.click_button_log_in()
    page.verification_non_existent_login()

