from page_objects import PageObject, PageElement
from selenium.webdriver import ActionChains
from phptravels_pages.BigBusTourPage import BigBusTourPage


class ToursListingPage(PageObject):
    """This class resolves elements for Dubai search"""

    # to click for element to make a search
    vacation_place_element1 = PageElement(css="a.select2-choice.select2-default")
    # To send text "Dubai"
    vacation_place_element2 = PageElement(css="div.select2-drop-active > div > input.select2-input")
    # To select Big Bus Tour of Dubai from menu
    choose_tour_element = PageElement(css="ul > li > ul > li > div.select2-result-label")
    # To provision date
    date_element = PageElement(css="input[name = 'date']")
    # Submit element
    submit_elemnt = PageElement(css="button.btn-danger.btn.btn-lg.btn-block.pfb0.loader[type='submit']")


    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_ToursListingPage{}.png".format(test_name))

    def send_dubai_data(self, place="Dubai", start_date="02/08/2018"):
        """This function populates search data and finally returns new page object"""

        """To DO: Add tour type: minor"""

        # Put Dubai as vacation place
        self.vacation_place_element1.click()
        self.vacation_place_element2.send_keys(place)

        # select tour Big Bus Tour of Dubai
        self.w.implicitly_wait(2)
        action = ActionChains(self.w)
        action.move_to_element(self.choose_tour_element)
        action.click()
        action.perform()
        # Set date arrival date
        self.date_element.clear()
        self.date_element.send_keys(start_date)

        # press submit button
        self.submit_elemnt.click()

        return BigBusTourPage(self.w, root_uri='https://www.phptravels.net/tours/united-arab-emirates/dubai/ \
                                               Big-Bus-Tour-of-Dubai?date=02/08/2018&adults=2')



