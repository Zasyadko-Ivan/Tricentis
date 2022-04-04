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

    def first_name_registration_field(self, f_name):
        first_name_field = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_LINK)
        first_name_field.send_keys(f_name)

    def last_name_registration_field(self, l_name):
        last_name_field = self.browser.find_element(*RegisterPageLocators.LAST_NAME_LINK)
        last_name_field.send_keys(l_name)

    def email_registration_field(self, email):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_LINK)
        email_field.send_keys(email)

    def password_registration_field(self, password):
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_LINK)
        password_field.send_keys(password)

    def confirm_password_registration_field(self, confirm_password):
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_LINK)
        password_field.send_keys(confirm_password)

    def choose_gender_male(self):
        radio_male = self.browser.find_element(*RegisterPageLocators.GENDER_MAIL_LINK)
        radio_male.click()

    def choose_gender_female(self):
        radio_buttons_female = self.browser.find_element(*RegisterPageLocators.GENDER_FEMALE_LINK)
        radio_buttons_female.click()

    def click_button_register(self):
        button_register = self.browser.find_element(*RegisterPageLocators.BUTTON_REGISTER_LINK)
        button_register.click()

    def click_button_log_out(self):
        button_log_out = self.browser.find_element(*RegisterPageLocators.BUTTON_LOG_OUT_LINK)
        button_log_out.click()

    def verification_of_successful_registration(self):
        messages_of_successful_registration = self.browser.find_element(*RegisterPageLocators.NOTIFICATION_OF_SUCCESSFUL_REGISTRATION).text
        assert messages_of_successful_registration == "Your registration completed", "Your registration not complete"

    def should_not_be_verification_of_successful_registration(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOTIFICATION_OF_SUCCESSFUL_REGISTRATION), \
            "'Your registration complete' message is presented, but should not be"

    def should_not_be_verification_not_entered_email_already_exists(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOTIFICATION_OF_EMAIL_ALREADY_EXISTS), \
            "'The specified email already exists' message is presented, but should not be"

    def verification_not_entered_first_name(self):
        messages_of_not_entered_first_name = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_FIRST_NAME_LINK).text
        assert messages_of_not_entered_first_name == "First name is required.", "Not messages 'First name is required.'"

    def should_not_be_verification_not_entered_first_name(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOT_ENTERED_FIRST_NAME_LINK), \
            "'First name is required.' message is presented, but should not be"

    def verification_not_entered_last_name(self):
        messages_of_not_entered_last_name = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_LAST_NAME_LINK).text
        assert messages_of_not_entered_last_name == "Last name is required.", "Not messages 'Last name is required.'"

    def should_not_be_verification_not_entered_last_name(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOT_ENTERED_LAST_NAME_LINK), \
            "'Last name is required.' message is presented, but should not be"

    def verification_not_entered_email(self):
        messages_of_not_entered_email = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_EMAIL_LINK).text
        assert messages_of_not_entered_email == "Email is required.", "Not messages 'Email is required.'"

    def verification_wrong_email(self):
        messages_of_not_entered_email = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_EMAIL_LINK).text
        assert messages_of_not_entered_email == "Wrong email", "Not messages 'Wrong email'"

    def should_not_be_verification_not_entered_email(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOT_ENTERED_EMAIL_LINK), \
            "'Email is required.' message is presented, but should not be"

    def verification_not_entered_password(self):
        messages_of_not_entered_password = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_PASSWORD_LINK).text
        assert messages_of_not_entered_password == "Password is required.", "Not messages 'Password is required.'"

    def should_not_be_verification_not_entered_password(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOT_ENTERED_PASSWORD_LINK), \
            "'Password is required.' message is presented, but should not be"

    def verification_not_entered_confirm_password(self):
        messages_of_not_entered_confirm_password = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_CONFIRM_PASSWORD_LINK).text
        assert messages_of_not_entered_confirm_password == "Password is required.", "Not messages 'Password is required.'"

    def should_not_be_verification_not_entered_confirm_password(self):
        assert self.is_not_element_present(*RegisterPageLocators.NOT_ENTERED_CONFIRM_PASSWORD_LINK), \
            "'Password is required.' message is presented, but should not be"

    def should_be_a_message_about_a_password_mismatch_and_confirm_password(self):
        messages_about_a_password_mismatch_and_confirm_password = self.browser.find_element(*RegisterPageLocators.NOT_ENTERED_CONFIRM_PASSWORD_LINK).text
        assert messages_about_a_password_mismatch_and_confirm_password == "The password and confirmation password do not match.", "Not messages 'The password and confirmation password do not match'"

    def verification_register_completed(self):
        messages_register_completed = self.browser.find_element(
            *RegisterPageLocators.REGISTER_COMPLETED_LINK).text
        assert messages_register_completed == "Your registration completed", "Not messages 'No customer account found'"

    def should_not_verification_register_completed(self):
        assert self.is_not_element_present(*RegisterPageLocators.REGISTER_COMPLETED_LINK), \
            "'Your registration completed' message is presented, but should not be"

    def verification_successful_login(self, email):
        email_login = email
        messages_email_login = self.browser.find_element(*RegisterPageLocators.LOGIN_COMPLETED_LINK).text
        assert messages_email_login == email_login, "Not login"

    def verification_not_successful_login(self):
        messages_not_login = self.browser.find_element(*RegisterPageLocators.LOGIN_COMPLETED_LINK).text
        assert messages_not_login == "Register", "Login"









