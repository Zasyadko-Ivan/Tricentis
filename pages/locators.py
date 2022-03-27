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
