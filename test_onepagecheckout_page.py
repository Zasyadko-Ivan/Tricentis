import time
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.product_list_page import ProductListPage
from .pages.cart_page import CartPage
from .pages.onepagecheckout_page import OnepagecheckoutPage

import pytest

link_book = 'http://demowebshop.tricentis.com/books'
link_log = "http://demowebshop.tricentis.com/login"
link_reg = 'http://demowebshop.tricentis.com/register'
link_cart = 'http://demowebshop.tricentis.com/cart'
link_one = 'http://demowebshop.tricentis.com/onepagecheckout'

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

        class TestLoginUser():
            @pytest.fixture(scope="function", autouse=True)
            def test_verification_added_product_logged_in(self, browser):
                page = ProductListPage(browser, link_book)
                page.open()
                page.availability_check_button_add_to_cart()
                page.verification_added_correct_product()

            class Test():
                @pytest.fixture(scope="function", autouse=True)
                def test_change_the_quantity_0_not_login_in(self, browser):
                    page = CartPage(browser, link_cart)
                    page.open()
                    page.click_checkbox_i_agree()
                    page.click_button_checkout()

                def test_1(self, browser):
                    page = OnepagecheckoutPage(browser, link_one)
                    page.open()
                    page.enter_company_field('OOO Checkout')
                    page.enter_country_field('66')
                    page.enter_city_field("Saint Petersburg")
                    page.enter_address_1_field("Newa №1")
                    page.enter_address_2_field("Newa №2")
                    page.enter_zip_code_field('01204756')
                    page.enter_phone_number_field('8800555355')
                    page.enter_fax_number_field('82735968')
                    time.sleep(2)
                    page.click_button_continue()
                    time.sleep(3)





