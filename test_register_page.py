import time
from .pages.register_page import RegisterPage

link = 'http://demowebshop.tricentis.com/register'

#pytest -v test_register_page.py


def test_successful_registration_of_a_new_user(browser):
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = "kjsfg123hse21312322@gmail.com"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.verification_of_successful_registration()


def test_to_check_the_suggestions_to_fill_in(browser):
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = "kjsfg123hse21311232322@gmail.com"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.click_button_register()
    page.verification_not_entered_first_name()
    page.verification_not_entered_last_name()
    page.verification_not_entered_email()
    page.verification_not_entered_password()
    page.verification_not_entered_confirm_password()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.should_not_be_verification_not_entered_first_name()
    page.should_not_be_verification_not_entered_last_name()
    page.should_not_be_verification_not_entered_email()
    page.should_not_be_verification_not_entered_password()
    page.should_not_be_verification_not_entered_confirm_password()








