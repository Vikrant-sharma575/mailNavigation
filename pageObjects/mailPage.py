from selenium.webdriver.common.by import By



class mainPage:
    vnew_mail = (By.XPATH, "//li[@title='Compose a new mail']")
    vsend_mail_to = (By.CSS_SELECTOR, ".rd_inp_to")
    vmail_subject = (By.CSS_SELECTOR, ".rd_inp_sub")
    vcontent_frame = (By.XPATH, "//iframe[@title='Rich Text Editor, rdMailEditorcmp2']")
    vmail_content = (By.CSS_SELECTOR, ".cke_editable")
    vsend_mail = (By.CSS_SELECTOR, "div[class='comps_fet'] [class*='rd_btn_cmp_send']")
    vsent_folder = (By.XPATH, "//li[@title='Sent']")
    vsent_mail_list = (By.CSS_SELECTOR, "ul[class='rd_ml'] li[class*='li_mail_item']")

    def __init__(self, driver):
        self.driver = driver


    def new_mail(self):
        return self.driver.find_element(*mainPage.vnew_mail)

    def send_mail_to(self):
        return self.driver.find_element(*mainPage.vsend_mail_to)

    def mail_subject(self):
        return self.driver.find_element(*mainPage.vmail_subject)

    def content_frame(self):
        return self.driver.find_element(*mainPage.vcontent_frame)

    def mail_content(self):
        return self.driver.find_element(*mainPage.vmail_content)

    def send_mail(self):
        return self.driver.find_element(*mainPage.vsend_mail)

    def sent_folder(self):
        return self.driver.find_element(*mainPage.vsent_folder)

    def sent_mail_list(self):
        return self.driver.find_elements(*mainPage.vsent_mail_list)

