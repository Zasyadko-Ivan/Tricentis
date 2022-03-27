import pytest
from selenium import webdriver

chrome_link = "/Users/ivanzasadko/PycharmProjects/pythonProject/Blol_3/chromedriver/chromedriver"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=chrome_link)
    yield browser
    print("\nquit browser..")
    browser.quit()
