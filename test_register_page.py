import time
from .pages.register_page import RegisterPage

link = 'http://demowebshop.tricentis.com/register'

#pytest -v test_register_page.py



def test_guest_cant_see_success_message(browser):
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
    page.verification_of_successful_registration()


