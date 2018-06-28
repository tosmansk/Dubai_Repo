from page_objects import PageObject, PageElement

from phptravels_pages.ToursListing import ToursListing


class AccountPage(PageObject):
    """This class resolves elements from https://www.phptravels.net/account/"""

    # Page elements section

    # TOURS navbar element
    tours_element = PageElement(xpath="//a[@href='https://www.phptravels.net/tours']")

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def click_tours(self):
        self.tours_element.click()

        return ToursListing(self.w, root_uri='https://www.phptravels.net/tours')

