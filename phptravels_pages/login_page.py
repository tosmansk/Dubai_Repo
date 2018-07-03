from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait

from phptravels_pages.account_page import AccountPage


class LoginPage(PageObject):
    """This class resolves elements and makes actions on https://www.phptravels.net/login login page"""

    # Page elements section
    # The elements below are needed for login action

    # Email text input element
    email_element = PageElement(xpath="//input[@placeholder='Email']")

    # Password text input element
    passwd_element = PageElement(xpath="//input[@placeholder='Password']")

    # Login button element
    login_button_element = PageElement(css="button.btn.btn-action.btn-lg.btn-block.loginbtn")

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_logs/screen_LoginPage{}.png".format(test_name))

    def make_login(self, credentials):
        """This function makes login action with credential usage"""

        _email = credentials['Email']
        _password = credentials['Password']

        email = self.email_element
        passwd = self.passwd_element
        login_button = self.login_button_element

        email.clear()
        email.send_keys(_email)
        passwd.clear()
        passwd.send_keys(_password)
        self.w.implicitly_wait(1)
        login_button.click()

        WebDriverWait(self.w, 30).until(lambda driver: driver.title != "Login")

        return AccountPage(self.w, root_uri='https://www.phptravels.net/account/')
