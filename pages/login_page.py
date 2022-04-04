from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def click_button_log_in(self):
        button_register = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_LINK)
        button_register.click()

    def enter_email_field(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        email_field.send_keys(email)

    def enter_password_field(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK)
        password_field.send_keys(password)

    def verification_log_in(self):
        assert self.is_not_element_present(*LoginPageLocators.MESSAGE_DOES_NOT_LOG_IN_LINK), \
            f"'{self.browser.find_element(*LoginPageLocators.MESSAGE_DOES_NOT_LOG_IN_LINK).text}' message is presented, but should not be"

    def verification_login_failed(self):
        assert self.is_not_element_present(*LoginPageLocators.MESSAGE_LOGIN_FAILED_LINK), \
            f"'{self.browser.find_element(*LoginPageLocators.MESSAGE_LOGIN_FAILED_LINK).text}' message is presented, but should not be"

    def verification_non_existent_login(self):
        messages_about_a_password_mismatch_and_confirm_password = self.browser.find_element(*LoginPageLocators.MESSAGE_LOGIN_FAILED_LINK).text
        assert messages_about_a_password_mismatch_and_confirm_password != "No customer account found", "Not messages 'No customer account found'"

    def verification_non_existent_password(self):
        messages_about_a_password_mismatch_and_confirm_password = self.browser.find_element(*LoginPageLocators.MESSAGE_LOGIN_FAILED_LINK).text
        assert messages_about_a_password_mismatch_and_confirm_password != "The credentials provided are incorrect", "Not messages 'The credentials provided are incorrect'"

    def verification_email(self):
        assert self.is_not_element_present(*LoginPageLocators.MESSAGE_NOT_VALID_EMAIL_LINK), \
            "Please enter a valid email address."

    def verification_successful_login(self, email):
        email_login = email
        messages_email_login = self.browser.find_element(*LoginPageLocators.LOGIN_COMPLETED_LINK).text
        assert messages_email_login == email_login, "Not login"

    def verification_not_successful_login(self):
        messages_not_login = self.browser.find_element(*LoginPageLocators.LOGIN_COMPLETED_LINK).text
        assert messages_not_login == "Register", "Login"

