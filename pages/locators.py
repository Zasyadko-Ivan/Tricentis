from selenium.webdriver.common.by import By
import random


class RegisterPageLocators():
    GENDER_MAIL_LINK = (By.XPATH, '//*[@id="gender-male"]')
    GENDER_FEMALE_LINK = (By.XPATH, '//*[@id="gender-female"]')
    FIRST_NAME_LINK = (By.XPATH, '//*[@id="FirstName"]')
    LAST_NAME_LINK = (By.XPATH, '//*[@id="LastName"]')
    EMAIL_LINK = (By.XPATH, '//*[@id="Email"]')
    PASSWORD_LINK = (By.XPATH, '//*[@id="Password"]')
    CONFIRM_PASSWORD_LINK = (By.XPATH, '//*[@id="ConfirmPassword"]')
    BUTTON_REGISTER_LINK = (By.XPATH, '//*[@id="register-button"]')
    NOTIFICATION_OF_SUCCESSFUL_REGISTRATION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]')
    NOTIFICATION_OF_EMAIL_ALREADY_EXISTS = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[1]/div/ul/li')
    NOT_ENTERED_FIRST_NAME_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/span[2]/span')
    NOT_ENTERED_LAST_NAME_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/span[2]/span')
    NOT_ENTERED_EMAIL_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/span[2]/span')
    NOT_ENTERED_PASSWORD_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/span[2]/span')
    NOT_ENTERED_CONFIRM_PASSWORD_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/span[2]/span')
    REGISTER_COMPLETED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]')
    BUTTON_LOG_OUT_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
    LOGIN_COMPLETED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a')


class LoginPageLocators():
    EMAIL_LINK = (By.XPATH, '//*[@id="Email"]')
    PASSWORD_LINK = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input')
    MESSAGE_DOES_NOT_LOG_IN_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/ul/li')
    MESSAGE_LOGIN_FAILED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/span')
    MESSAGE_NOT_VALID_EMAIL_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/span/span')
    LOGIN_COMPLETED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a')


class ChangepasswordPageLocators():
    OLD_PASSWORD_LINK = (By.XPATH, '//*[@id="OldPassword"]')
    NEW_PASSWORD_LINK = (By.XPATH, '//*[@id="NewPassword"]')
    CONFIRM_PASSWORD_LINK = (By.XPATH, '//*[@id="ConfirmNewPassword"]')
    CHANGE_PASSWORD_BUTTON_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/input')
    MESSAGE_OLD_PASSWORD_DONT_MATCH_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[1]/div/ul/li')
    PASSWORD_CHANGE_MESSAGE_LINK = (By.CSS_SELECTOR, 'body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > form > div > div.page-body > div.result')
    MESSAGE_OLD_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div/div[1]/span[2]/span')
    MESSAGE_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div/div[2]/span[2]/span')
    MESSAGE_CONFIRM_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div/div[3]/span[2]/span')


class ProductPageLocators():
    BUTTON_ADD_TO_CART_LINK = (By.XPATH, '//*[@class="button-1 add-to-cart-button"]')
    NAME_PRODUCT_LINK = (By.XPATH, '//*[@id="product-details-form"]/div/div[1]/div[2]/div[1]/h1')
    PRICE_PRODUCT_LINK = (By.XPATH, '//*[@id="product-details-form"]/div/div[1]/div[2]/div[6]/div[2]/span')
    IMG_PRODUCT_LINK = (By.XPATH, '//*[@id="main-product-img-13"]')
    MESSAGE_ADDED_CART_LINK = (By.XPATH, '//*[@id="bar-notification"]/p')



class ProductListPageLocators():
    r = "5"
    BUTTON_ADD_TO_CART_LINK = (By.XPATH, '//div[@class="item-box"][' + r + ']/div/div[2]/div[3]/div[2]/input[@class="button-2 product-box-add-to-cart-button"]')
    NAME_PRODUCT_LINK = (By.XPATH, '//div[@class="item-box"][' + r + ']/div/div[2]/h2/a')
    PRICE_PRODUCT_LINK = (By.XPATH, '//div[@class="item-box"][' + r + ']/div/div[2]/div[3]/div[1]/span[2]')
    IMG_PRODUCT_LINK = (By.XPATH, '//div[@class="item-box"][' + r + ']/div/div[1]/a/img')
    BUTTON_SHOPPING_CART_LINK = (By.XPATH, '//*[@id="topcartlink"]/a/span[1]')
    MESSAGE_ADDED_CART_LINK = (By.XPATH, '//*[@id="bar-notification"]/p')
    BUTTON_SHOPPING_CART_MESSAGE_ADDED_CART_LINK = (By.XPATH, '//*[@id="bar-notification"]/p/a')
    LINK_IN_PRODUCT_LINK = (By.XPATH, '//div[@class="item-box"][' + r + ']/div/div[1]/a')

class CartPageLocators():
    NAME_PRODUCT_IN_CART_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[3]/a')
    PRICE_PRODUCT_IN_CART_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[4]/span[2]')
    IMG_PRODUCT_IN_CART_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[2]/img')
    QTY_FIELD_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[5]/input')
    TOTAL_LINK = (By.XPATH,'/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[6]/span[2]')
    BUTTON_UPDATE_SHOPPING_CART = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[1]/div/input[1]')
    СHECKBOX_I_AGREE_TO_THE_TERMS_LINK = (By.XPATH, '//*[@id="termsofservice"]')
    BUTTON_CHECKOUT_LINK = (By.XPATH, '//*[@id="checkout"]/font/font')
    MESSAGE_YOU_CART_IS_EMPTY_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div[2]/div[2]/div')


