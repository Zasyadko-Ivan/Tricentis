import time
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.changepassword_page import ChangepasswordPage

import pytest

link_chang = 'http://demowebshop.tricentis.com/customer/changepassword'
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

        @pytest.mark.smoke
        def test_successful_change_password_new_user(self, browser, setup):
            page = ChangepasswordPage(browser, link_chang)
            page.open()
            password = "Heznai1"
            page.enter_old_password_field(setup[1])
            page.enter_new_password_field(password)
            page.enter_confirm_password_field(password)
            page.click_button_change_password()
            page.verification_password_changed()

        @pytest.mark.parametrize('password', ["",
                                              pytest.param('123  45  fhg', marks=pytest.mark.xfail), '12fg',
                                              pytest.param('??????_????_????????_????????????_????????_??????', marks=pytest.mark.xfail)])
        def test_not_valid_change_password_new_user(self, browser, setup,password):
            page = ChangepasswordPage(browser, link_chang)
            page.open()
            page.enter_old_password_field(setup[1])
            page.enter_new_password_field(password)
            page.enter_confirm_password_field(password)
            page.click_button_change_password()
            page.verification_not_password_changed()

        def test_enter_the_wrong_old_password(self, browser):
            page = ChangepasswordPage(browser, link_chang)
            page.open()
            password = "Heznai1"
            page.enter_old_password_field(password)
            page.enter_new_password_field(password)
            page.enter_confirm_password_field(password)
            page.click_button_change_password()
            page.verification_not_password_changed()

        def test_enter_different_passwords(self, browser, setup):
            page = ChangepasswordPage(browser, link_chang)
            page.open()
            page.enter_old_password_field(setup[1])
            page.enter_new_password_field("password")
            page.enter_confirm_password_field("password1")
            page.click_button_change_password()
            page.verification_enter_different_passwords()
            page.verification_not_password_changed()

        def test_message_fields_password_empty_ones(self, browser, setup):
            page = ChangepasswordPage(browser, link_chang)
            page.open()
            page.enter_old_password_field('')
            page.enter_new_password_field('')
            page.enter_confirm_password_field('')
            page.click_button_change_password()
            page.verification_fields_old_password_empty_ones()
            page.verification_fields_new_password_empty_ones()
            page.verification_fields_confirm_password_empty_ones()
            page.verification_not_password_changed()

