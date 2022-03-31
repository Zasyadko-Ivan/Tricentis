from selenium.webdriver.common.by import By


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


class LoginPageLocators():
    EMAIL_LINK = (By.XPATH, '//*[@id="Email"]')
    PASSWORD_LINK = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input')
    MESSAGE_DOES_NOT_LOG_IN_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/ul/li')
    MESSAGE_LOGIN_FAILED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]/div/span')
    MESSAGE_NOT_VALID_EMAIL_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[2]/span/span')

class ChangepasswordPageLocators():
    OLD_PASSWORD_LINK = (By.XPATH, '//*[@id="OldPassword"]')
    NEW_PASSWORD_LINK = (By.XPATH, '//*[@id="NewPassword"]')
    CONFIRM_PASSWORD_LINK = (By.XPATH, '//*[@id="ConfirmNewPassword"]')
    CHANGE_PASSWORD_BUTTON_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/input')
    MESSAGE_OLD_PASSWORD_DONT_MATCH_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[1]/div/ul/li')
    PASSWORD_CHANGE_MESSAGE_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]')
    MESSAGE_OLD_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div/div[1]/span[2]/span')
    MESSAGE_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div/div[2]/span[2]/span')
    MESSAGE_CONFIRM_PASSWORD_IS_REQUIRED_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div/div[3]/span[2]/span')

