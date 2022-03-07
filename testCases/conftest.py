import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )




@pytest.fixture(scope = "class")
def setup(request):
    #   request is like an instance for the fixture
    browser = request.config.getoption("browser_name")
    if browser == 'chrome':
        driver = webdriver.Chrome(r"C:\Python\browserDrivers\chromedriver.exe")
        baseUrl = "https://mail.rediff.com/cgi-bin/login.cgi"
        driver.get(baseUrl)
        driver.maximize_window()
        time.sleep(5)
    elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=r"C:\Python\browserDrivers\geckodriver.exe")
            baseUrl = "https://mail.rediff.com/cgi-bin/login.cgi"
            driver.get(baseUrl)
            driver.maximize_window()
            time.sleep(5)

    #   we initialize our driver variable to the class driver i.e. cls.driver
    request.cls.driver = driver
    yield
    driver.close()