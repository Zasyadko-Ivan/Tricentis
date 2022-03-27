from .locators import RegisterPageLocators
from .base_page import BasePage


class RegisterPage(BasePage):
    def fill_in_the_main_registration_fields(self, f_name, l_name, email, password, confirm_password):
        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_LINK)
        first_name_field.send_keys(f_name)
        last_name_field = self.browser.find_element(*RegisterPageLocators.LAST_NAME_LINK)
        last_name_field.send_keys(l_name)
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_LINK)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_LINK)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_LINK)
        confirm_password_field.send_keys(confirm_password)

    def choose_gender_male(self):
        radio_male = self.browser.find_element(*RegisterPageLocators.GENDER_MAIL_LINK)
        radio_male.click()

    def choose_gender_female(self):
        radio_buttons_female = self.browser.find_element(*RegisterPageLocators.GENDER_FEMALE_LINK)
        radio_buttons_female.click()

    def click_button_register(self):
        button_register = self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER_LINK)
        button_register.click()

    def verification_of_successful_registration(self):
        messages_of_successful_registration = self.browser.find_element(*RegisterPageLocators.NOTIFICATION_OF_SUCCESSFUL_REGISTRATION).text
        assert messages_of_successful_registration == "Your registration completed", "Your registration not complete"












