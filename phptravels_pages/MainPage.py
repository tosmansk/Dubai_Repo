from page_objects import PageObject, PageElement
from phptravels_pages.LoginPage import LoginPage


class MainPage(PageObject):
    """This class resolves elements and makes actions on https://www.phptravels.net/ main page"""

    # Page elements section
    # The elements below are needed for login purpose

    # MY ACCOUNT element
    myaccount_element = PageElement(css="ul > ul > li[id='li_myaccount'] > a")

    # Login element
    login_element = PageElement(css="ul > ul > li > ul > li > a[href='https://www.phptravels.net/login']")

    def make_screenshot(self):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_MainPage.png")

    def return_phptravels_page(self):
        """This function returns its page object"""

        return self

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def make_loging(self):
        """This function makes logging"""

        # Click on MY ACCOUNT
        self.myaccount_element.click()
        # Click on Login
        self.login_element.click()
        # Return LoginPage object
        return LoginPage(self.w, root_uri='https://www.phptravels.net/login')
