from .locators import ChangepasswordPageLocators
from .base_page import BasePage


class ChangepasswordPage(BasePage):
    def click_button_change_password(self):
        button_register = self.browser.find_element(*ChangepasswordPageLocators.CHANGE_PASSWORD_BUTTON_LINK)
        button_register.click()

    def verification_not_messange_old_password_not_true(self):
        assert self.is_not_element_present(*ChangepasswordPageLocators.MESSAGE_OLD_PASSWORD_DONT_MATCH_LINK), \
            "'Old password doesn't match' message is presented, but should not be"

    def verification_password_changed(self):
        messages_password_change = self.browser.find_element(*ChangepasswordPageLocators.PASSWORD_CHANGE_MESSAGE_LINK).text
        assert messages_password_change == "Password was changed", "Not messages 'Password was changed'"

    def enter_old_password_field(self, old_password):
        email_field = self.browser.find_element(*ChangepasswordPageLocators.OLD_PASSWORD_LINK)
        email_field.send_keys(old_password)

    def enter_new_password_field(self, new_password):
        email_field = self.browser.find_element(*ChangepasswordPageLocators.NEW_PASSWORD_LINK)
        email_field.send_keys(new_password)

    def enter_confirm_password_field(self, confirm_password):
        email_field = self.browser.find_element(*ChangepasswordPageLocators.CONFIRM_PASSWORD_LINK)
        email_field.send_keys(confirm_password)

        

