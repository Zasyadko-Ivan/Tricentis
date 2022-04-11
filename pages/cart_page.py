import time

from .locators import ProductPageLocators
from .locators import ProductListPageLocators
from .locators import CartPageLocators
from .base_page import BasePage


import pytest


class CartPage(BasePage):
    def click_button_update_shopping_cart(self):
        button_update_shopping_cart = self.browser.find_element(*CartPageLocators.BUTTON_UPDATE_SHOPPING_CART)
        button_update_shopping_cart.click()

    def click_button_checkout(self):
        button_checkout = self.browser.find_element(*CartPageLocators.BUTTON_CHECKOUT_LINK)
        button_checkout.click()

    def click_checkbox_i_agree(self):
        checkbox_i_agree = self.browser.find_element(*CartPageLocators.СHECKBOX_I_AGREE_TO_THE_TERMS_LINK)
        checkbox_i_agree.click()

    def enter_quantity(self, qty):
        quantity_field = self.browser.find_element(*CartPageLocators.QTY_FIELD_LINK)
        quantity_field.clear()
        quantity_field.send_keys(qty)

    def enter_quantity_with_return(self, qty):
        quantity_field = self.browser.find_element(*CartPageLocators.QTY_FIELD_LINK)
        quantity_field.clear()
        quantity_field.send_keys(qty, '\n')

    def verification_total_amount(self):
        price = self.browser.find_element(*CartPageLocators.PRICE_PRODUCT_IN_CART_LINK).text
        quantity_link = self.browser.find_element(*CartPageLocators.QTY_FIELD_LINK)
        quantity = quantity_link.get_attribute('value')
        total_amount = self.browser.find_element(*CartPageLocators.TOTAL_LINK).text
        total = format(float(price) * float(quantity), '.2f')
        assert total_amount == str(total), f"The amount on the page varies '{total_amount}' and '{total}'"

    def verification_message_you_cart_empty(self):
        message_you_cart_empty = self.browser.find_element(*CartPageLocators.MESSAGE_YOU_CART_IS_EMPTY_LINK).text
        assert message_you_cart_empty == "Your Shopping Cart is empty!", "Not messages 'Your Shopping Cart is empty!'"



