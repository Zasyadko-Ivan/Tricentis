import time
from .pages.login_page import LoginPage
import pytest

link = "http://demowebshop.tricentis.com/login"


def test_successful_login(browser):
    email = "привет234@g1mail.com"
    password = "привет234@g1mail.com"
    page = LoginPage(browser, link)
    page.open()
    page.enter_email_field(email)
    page.enter_password_field(password)
    page.click_button_log_in()
    page.verification_email()
    page.verification_log_in()
    page.verification_login_failed()
