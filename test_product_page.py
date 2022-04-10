import time
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.product_page import ProductPage

import pytest

link_book = 'http://demowebshop.tricentis.com/computing-and-internet'
link_log = "http://demowebshop.tricentis.com/login"
link_reg = 'http://demowebshop.tricentis.com/register'


class TestCreatedUserHeLoggedIn():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f_name = "Ivan"
        l_name = "Zasyadko"
        email = str(time.time()) + "@fakemail.org"
        password = "ggga!Q24"
        confirm_password = password
        page = RegisterPage(browser, link_reg)
        page.open()
        page.choose_gender_male()
        page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
        page.click_button_register()
        page.verification_register_completed()
        page.click_button_log_out()
        return email, password

    class TestLoginUser():
        @pytest.fixture(scope="function", autouse=True)
        def setup_2(self, browser, setup):
            page = LoginPage(browser, link_log)
            page.open()
            page.enter_email_field(setup[0])
            page.enter_password_field(setup[1])
            page.click_button_log_in()
            page.verification_email()
            page.verification_log_in()
            page.verification_login_failed()
            page.verification_successful_login(setup[0])

        def test_add_product_logged_in(self, browser):
            page = ProductPage(browser, link_book)
            page.open()
            page.availability_check_button_add_to_cart()
            page.click_button_add_to_cart()
            time.sleep(3)
            page.verification_added_product()


        def test_verification_added_product_logged_in(self, browser):
            page = ProductPage(browser, link_book)
            page.open()
            page.availability_check_button_add_to_cart()
            page.verification_added_correct_product()


def test_add_product_not_logged_in(browser):
    page = ProductPage(browser, link_book)
    page.open()
    page.availability_check_button_add_to_cart()
    page.click_button_add_to_cart()
    time.sleep(3)
    page.verification_added_product()



def test_verification_added_product_not_logged_in(browser):
    page = ProductPage(browser, link_book)
    page.open()
    page.availability_check_button_add_to_cart()
    page.verification_added_correct_product()