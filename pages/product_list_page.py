import time

from .locators import ProductListPageLocators
from .locators import CartPageLocators
from .base_page import BasePage
import pytest


class ProductListPage(BasePage):
    def click_button_add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductListPageLocators.BUTTON_ADD_TO_CART_LINK)
        button_add_to_cart.click()

    def availability_check_button_add_to_cart(self):
        messages_fields_old_password_empty_ones = self.browser.find_element(*ProductListPageLocators.NAME_PRODUCT_LINK).text
        assert self.is_element_present(*ProductListPageLocators.BUTTON_ADD_TO_CART_LINK), \
            f"'Not button' {messages_fields_old_password_empty_ones}"

    def verification_added_product(self):
        message_added_cart = self.browser.find_element(*ProductListPageLocators.MESSAGE_ADDED_CART_LINK).text
        assert message_added_cart == 'The product has been added to your shopping cart', "Not message added cart"

    def verification_added_correct_product(self):
        name_product_in_product_page = self.browser.find_element(*ProductListPageLocators.NAME_PRODUCT_LINK).text
        price_product_in_product_page = self.browser.find_element(*ProductListPageLocators.PRICE_PRODUCT_LINK).text
        img_product_in_product_page = self.browser.find_element(*ProductListPageLocators.IMG_PRODUCT_LINK)
        img_src_product_page = img_product_in_product_page.get_attribute('src')
        button_add_to_cart = self.browser.find_element(*ProductListPageLocators.BUTTON_ADD_TO_CART_LINK)
        button_add_to_cart.click()
        button_shopping_cart = self.browser.find_element(*ProductListPageLocators.BUTTON_SHOPPING_CART_LINK)
        button_shopping_cart.click()
        time.sleep(3)
        name_product_in_cart_page = self.browser.find_element(*CartPageLocators.NAME_PRODUCT_IN_CART_LINK).text
        price_product_in_cart_page = self.browser.find_element(*CartPageLocators.PRICE_PRODUCT_IN_CART_LINK).text
        img_product_in_cart_page = self.browser.find_element(*CartPageLocators.IMG_PRODUCT_IN_CART_LINK)
        img_src_cart_page = img_product_in_cart_page.get_attribute('src')
        assert name_product_in_product_page == name_product_in_cart_page, f"Name various '{name_product_in_product_page}' and '{name_product_in_cart_page}'"
        assert price_product_in_product_page == price_product_in_cart_page, f"Price various '{price_product_in_product_page}' and '{price_product_in_cart_page}'"
        #assert img_src_product_page == img_src_cart_page, f"Img various '{name_product_in_product_page}'"

