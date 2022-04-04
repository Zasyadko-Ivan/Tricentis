import pytest
from selenium import webdriver

chrome_link = "driver/chromedriver/chromedriver"
firefox_link = "driver/geckodriver/geckodriver"


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default='no',
                     help="Choose headless mod")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    if browser_name == "chrome" and headless == "no":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path=chrome_link)
    elif browser_name == "firefox" and headless == "no":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=firefox_link)
    elif browser_name == "chrome" and headless == "no":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path=chrome_link)
    elif browser_name == "firefox" and headless == "yes":
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options, executable_path=firefox_link)
    yield browser
    print("\nquit browser..")
    browser.quit()