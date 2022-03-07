import time
import random as rnd
import string
import pytest

from pageObjects.loginPage import loginPage
from pageObjects.mailPage import mainPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class Test_mailing(BaseClass):
    def test_mail(self):

        self.driver.implicitly_wait(5)
        #   Enter the Login email ID here
        user = 'test.user3@rediffmail.com'
        #   Enter your password here
        pwd = 'TtttUuuu3#'
        #   Enter the recipient email ID here
        sendTo = 'rachi.shah@protonmail.com'

        # Create a unique and random string for verification
        letters = string.ascii_letters
        uniq_test = ''.join(rnd.choice(letters) for i in range(10))
        subject = "Test Subject" + uniq_test
        #   self.driver is needed as driver is the class variable (from conftest), and it can be accessed using self

        lggin_Page = loginPage(self.driver)
        lggin_Page.username().send_keys(user)
        lggin_Page.password().send_keys(pwd)
        lggin_Page.login_button().click()
        time.sleep(5)

        # Click on Create new mail
        main_page = mainPage(self.driver)
        main_page.new_mail().click()
        time.sleep(3)

        #   Give the mail address of the recipient
        main_page.send_mail_to().send_keys(sendTo)

        #   Give a unique subject for verification
        main_page.mail_subject().send_keys(subject)

        #   Write the content of the message
        frame = main_page.content_frame()
        self.driver.switch_to.frame(frame)
        main_page.mail_content().send_keys("Hello Test User, \n"
                                          "This is a test email. \n"
                                          "Please ignore. "
                                          "\n\n\n\n\n"
                                          "Regards,\n"
                                          "Test User3")
        time.sleep(5)
        self.driver.switch_to.default_content()
        #   Send mail
        main_page.send_mail().click()
        time.sleep(10)

        #   Verify mail sent
        #   1. Go to Sent folder
        main_page.sent_folder().click()
        time.sleep(5)

        #   2. Get a generic list of Items in Sent folder
        mail_count = main_page.sent_mail_list()
        print("Number of Sent mail are : {}\n ".format(len(mail_count)))

        #   3. Transform the iterable to a list
        mail_data = [mail.text for mail in mail_count]
        print("Below is the list of Mails with Timestamp, Subject and the Receiver in the Sent folder : \n{}".format(mail_data))

        #   4. Assert/ Verify that the mail is sent
        #   Index 0, since the latest sent mail will be on top based on timestamp
        assert subject in str(mail_data[0]), "Assertion failed as the recently sent mail isn't in Sent folder"