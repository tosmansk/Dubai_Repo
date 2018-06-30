from page_objects import PageObject, PageElement

from phptravels_pages.ToursListingPage import ToursListingPage


class AccountPage(PageObject):
    """This class resolves elements from https://www.phptravels.net/account/"""

    # Page elements section

    # TOURS navbar element
    tours_element = PageElement(xpath="//a[@href='https://www.phptravels.net/tours']")

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_AccountPage{}.png".format(test_name))

    def click_tours(self):
        self.tours_element.click()

        return ToursListingPage(self.w, root_uri='https://www.phptravels.net/tours')

