from .locators import OnepagecheckoutPageLocators
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class OnepagecheckoutPage(BasePage):
    def click_button_continue_billing_address(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONTINUE_BILLING_ADDRESS_LINK)
        button_continue.click()

    def click_button_continue_shipping_address(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONTINUE_SHIPPING_ADDRESS_LINK)
        button_continue.click()

    def click_button_continue_shipping_method(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONTINUE_SHIPPING_METHOD_LINK)
        button_continue.click()

    def click_button_continue_payment_method(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONTINUE_PAYMENT_METHOD_LINK)
        button_continue.click()

    def click_button_continue_payment_info(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONTINUE_PAYMENT_INFO_LINK)
        button_continue.click()

    def click_button_continue_confirm_order(self):
        button_continue = self.browser.find_element(*OnepagecheckoutPageLocators.BUTTON_CONFIRM_ORDER_LINK)
        button_continue.click()

    def enter_first_name_field(self, f_name):
        first_name_field = self.browser.find_element(*OnepagecheckoutPageLocators.FIRST_NAME_LINK)
        first_name_field.send_keys(f_name)

    def enter_last_name_field(self, l_name):
        last_name_field = self.browser.find_element(*OnepagecheckoutPageLocators.LAST_NAME_LINK)
        last_name_field.send_keys(l_name)

    def enter_email_field(self, email):
        email_field = self.browser.find_element(*OnepagecheckoutPageLocators.EMAIL_LINK)
        email_field.send_keys(email)

    def enter_company_field(self, company):
        company_field = self.browser.find_element(*OnepagecheckoutPageLocators.COMPANY_LINK)
        company_field.send_keys(company)

    def enter_country_field(self, number_country):
        select = Select(self.browser.find_element(*OnepagecheckoutPageLocators.COUNTRY_LINK))
        select.select_by_value(number_country)

    def enter_stay_field(self, stay):
        stay_field = self.browser.find_element(*OnepagecheckoutPageLocators.STATE_LINK)
        stay_field.send_keys(stay)

    def enter_city_field(self, city):
        city_field = self.browser.find_element(*OnepagecheckoutPageLocators.CITY_LINK)
        city_field.send_keys(city)

    def enter_address_1_field(self, address_1):
        address_1_field = self.browser.find_element(*OnepagecheckoutPageLocators.ADDRESS_1_LINK)
        address_1_field.send_keys(address_1)

    def enter_address_2_field(self, address_2):
        address_2_field = self.browser.find_element(*OnepagecheckoutPageLocators.ADDRESS_2_LINK)
        address_2_field.send_keys(address_2)

    def enter_zip_code_field(self, zip_code):
        zip_code_field = self.browser.find_element(*OnepagecheckoutPageLocators.ZIP_CODE_LINK)
        zip_code_field.send_keys(zip_code)

    def enter_phone_number_field(self, phone_number):
        phone_number_field = self.browser.find_element(*OnepagecheckoutPageLocators.PHONE_NUMBER_LINK)
        phone_number_field.send_keys(phone_number)

    def enter_fax_number_field(self, fax_number):
        fax_number_field = self.browser.find_element(*OnepagecheckoutPageLocators.FAX_NUMBER_LINK)
        fax_number_field.send_keys(fax_number)

    def verification_payment_method_cod(self):
        message_payment_method_cod = self.browser.find_element(*OnepagecheckoutPageLocators.MESSAGE_PAYMENT_INFO_LINK).text
        assert message_payment_method_cod == "You will pay by COD", "Not messages 'You will pay by COD'"

    def verification_order_has_been_placed(self):
        message_order_has_been_placed = self.browser.find_element(*OnepagecheckoutPageLocators.MASSAGE_ORDER_HAS_BEEN_PLACED_LINK).text
        assert message_order_has_been_placed == "Your order has been successfully processed!", "Not messages 'Your order has been successfully processed!'"


