from selenium.webdriver.common.by import By


class loginPage:
    vusername = (By.XPATH, "//input[@name='login']")
    vpassword = (By.XPATH, "//input[@name='passwd']")
    vlogin_button = (By.XPATH, "//input[@name='proceed']")

    def __init__(self, driver):
        self.driver = driver


    def username(self):
        return self.driver.find_element(*loginPage.vusername)

    def password(self):
        return self.driver.find_element(*loginPage.vpassword)

    def login_button(self):
        return self.driver.find_element(*loginPage.vlogin_button)
