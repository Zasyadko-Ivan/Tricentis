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

