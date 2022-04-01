import time
from .pages.register_page import RegisterPage
import pytest

link = 'http://demowebshop.tricentis.com/register'


@pytest.mark.smoke
def test_successful_registration_of_a_new_user(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.verification_of_successful_registration()


@pytest.mark.regression
@pytest.mark.parametrize('email', [str(time.time()) + "@fakemail.org",
                                  str(time.time()) + "@gmail.org",
                                  str(time.time()) + "ashfur" + "@fakemail.org"])
def test_successful_registration_of_a_new_user_different_email(browser, email):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_female()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.verification_of_successful_registration()


@pytest.mark.regression
@pytest.mark.parametrize('password', ['Super@!21',
                                  '12345fhga',
                                  'ny_naprimer_takoi_12'])
def test_successful_registration_of_a_new_user_different_password(browser, password):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.verification_of_successful_registration()


def test_to_check_the_suggestions_to_fill_in(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
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


def test_user_registration_without_first_name(browser):
    browser.implicitly_wait(5)
    f_name = ""
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.verification_not_entered_first_name()
    page.should_not_be_verification_of_successful_registration()


def test_user_registration_without_last_name(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = ""
    email = str(time.time()) + "@fakemail.org"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.verification_not_entered_last_name()
    page.should_not_be_verification_of_successful_registration()


def test_user_registration_without_email(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "@fakemail.org"
    email = ""
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.verification_not_entered_email()
    page.should_not_be_verification_of_successful_registration()


def test_user_registration_without_password(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    password = ""
    confirm_password = "Ivaasdn"
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.verification_not_entered_password()
    page.should_not_be_verification_of_successful_registration()


def test_user_registration_without_confirm_password(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    password = "Ivaasdn"
    confirm_password = ""
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.verification_not_entered_confirm_password()
    page.should_not_be_verification_of_successful_registration()


def test_user_registration_from_password_mismatch_and_confirm_password(browser):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    password = "ggga!Q24"
    confirm_password = "password"
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_be_a_message_about_a_password_mismatch_and_confirm_password()


@pytest.mark.regression
@pytest.mark.parametrize('email', [pytest.param("Кирилица" + "@fakemail.org", marks=pytest.mark.xfail),
                                  pytest.param(str(time.time()) + "@нучто.нибудь", marks=pytest.mark.xfail),
                                  'prostotak'
                                  'jfjdk jh@fakemail.org'])
def test_registration_of_a_new_user_different_not_valid_email(browser, email):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    password = "ggga!Q24"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_female()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.verification_wrong_email()


@pytest.mark.regression
@pytest.mark.parametrize('password', [pytest.param('Кирилицфаа', marks=pytest.mark.xfail),
                                  pytest.param('123  45fhga', marks=pytest.mark.xfail),
                                  pytest.param('jdsfjt#usdfj@t', marks=pytest.mark.xfail), '123d'])
def test_registration_of_a_new_user_different_not_valid_password(browser, password):
    browser.implicitly_wait(5)
    f_name = "Ivan"
    l_name = "Zasyadko"
    email = str(time.time()) + "@fakemail.org"
    confirm_password = password
    page = RegisterPage(browser, link)
    page.open()
    page.choose_gender_male()
    page.fill_in_the_main_registration_fields(f_name, l_name, email, password, confirm_password)
    page.click_button_register()
    page.should_not_be_verification_not_entered_email_already_exists()
    page.should_not_be_verification_of_successful_registration()









