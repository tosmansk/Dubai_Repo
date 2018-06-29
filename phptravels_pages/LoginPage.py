import time

from page_objects import PageObject, PageElement
from phptravels_pages.AccountPage import AccountPage


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
    def make_screenshot(self):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_LoginPage.png")

    def make_login(self):
        """This function makes login action with credential usage"""

        _email = 'user@phptravels.com'
        _password = 'demouser'

        email = self.email_element
        passwd = self.passwd_element
        login_button = self.login_button_element

        email.clear()
        email.send_keys(_email)
        passwd.clear()
        passwd.send_keys(_password)
        time.sleep(1)
        login_button.click()

        return AccountPage(self.w, root_uri='https://www.phptravels.net/account/')

        """TO DO: Element <button class="btn btn-action btn-lg btn-block loginbtn" type="submit"> is not clickable at point"""







