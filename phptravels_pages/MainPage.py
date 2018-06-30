from page_objects import PageObject, PageElement
from selenium.webdriver import ActionChains

from phptravels_pages.LoginPage import LoginPage


class MainPage(PageObject):
    """This class resolves elements and makes actions on https://www.phptravels.net/ main page"""

    # Page elements section
    # The elements below are needed for login purpose

    # MY ACCOUNT element
    myaccount_element = PageElement(css="ul > ul > li[id='li_myaccount'] > a")

    # Login element
    login_element = PageElement(css="ul > ul > li > ul > li > a[href='https://www.phptravels.net/login']")

    # Flight page elements
    flights_button_element = PageElement(css="a[href='#flights']")

    RoundTrip_element = PageElement(xpath='/html/body/div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[9]/div[2]')

    flights_from_text_box_element = PageElement(css="div#s2id_location_from > a.select2-choice.select2-default")

    flight_from_text_input_element = PageElement(css="div.select2-drop-active > div.select2-search > "
                                                     "input.select2-input.select2-focused")
    flight_choose_element = PageElement(css="div.select2-result-label")

    flights_to_text_box_element = PageElement(css="div#s2id_location_to > a.select2-choice.select2-default")

    flight_to_text_input_element = PageElement(css="div#select2-drop > div.select2-search > "
                                                   "input.select2-input[type='text']")
    departure_date_element = PageElement(css="input.departureTime")

    return_date_element = PageElement(css="input.arrivalTime")

    total_passengers_element = PageElement(css="div.col-md-1.form-group.go-right.col-xs-12 > div.row")

    adult_passengers_element = PageElement(xpath="//div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[7]/div/div"
                                                 "/div[2]/section/div/div[1]/div[1]")
    apassengers_amount_element = PageElement(css="select.travellercount.form-control[name='madult']")

    child_passengers_element = PageElement(xpath="//div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[7]/div/div"
                                                 "/div[2]/section/div/div[2]/div[1]")
    cpassengers_amount_element = PageElement(css="select.travellercount.form-control[name='mchildren']")

    infant_passengers_element = PageElement(xpath="//div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[7]/div/div"
                                                  "/div[2]/section/div/div[3]/div[1]")
    ipassengers_amount_element = PageElement(css="select.travellercount.form-control[name='minfant']")

    passengers_done_button_element = PageElement(xpath="//div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[7]/div"
                                                       "/div/div[3]")
    search_button_element = PageElement(xpath="//div[4]/section/div[2]/div/div[2]/div/div[4]/form/div[6]/div")

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_MainPage.{}.png".format(test_name))

    def return_phptravels_page(self):
        """This function returns its page object"""

        return self

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def select_flight(self, flight_data):
        """This function selects flight data"""

        # Click on FLIGHTS
        self.flights_button_element.click()

        # Click on Round Trip
        self.RoundTrip_element.click()

        # Provide departure airport
        self.flights_from_text_box_element.click()
        self.flight_from_text_input_element.send_keys(flight_data['from_airport'])
        self.w.implicitly_wait(1)
        self.flight_choose_element.click()

        # Provide destination airport
        self.flights_to_text_box_element.click()
        self.flight_to_text_input_element.send_keys(flight_data['to_airport'])
        self.w.implicitly_wait(1)
        self.flight_choose_element.click()

        # Provide departure date
        self.departure_date_element.click()
        self.departure_date_element.send_keys(flight_data['start_date'])

        # Provide return date
        self.return_date_element.click()
        self.return_date_element.send_keys(flight_data['return_date'])

        # Select passangers
        self.total_passengers_element.click()

        # select amounts from config
        if flight_data['apassengers'] != "0":
            self.selct_element(self.adult_passengers_element)
            self.apassengers_amount_element.send_keys(flight_data['apassengers'])

        if flight_data['cpassengers'] != "0":
            self.selct_element(self.child_passengers_element)
            self.cpassengers_amount_element.send_keys(flight_data['cpassengers'])

        if flight_data['ipassengers'] != "0":
            self.selct_element(self.infant_passengers_element)
            self.ipassengers_amount_element.send_keys(flight_data['ipassengers'])

            # Just press to hide selection window
            self.selct_element(self.infant_passengers_element)

        # Press DONE button
        self.passengers_done_button_element.click()

        # Press SEARCH button
        self.selct_element(self.search_button_element)

    def selct_element(self, choose_passengers_element):
        """This function selects passengers amount"""

        action = ActionChains(self.w)
        action.move_to_element(choose_passengers_element)
        action.click()
        action.perform()

    def click_loging(self):
        """This function makes logging"""

        # Click on MY ACCOUNT
        self.myaccount_element.click()
        # Click on Login
        self.login_element.click()
        # Return LoginPage object
        self.w.implicitly_wait(2)

        return LoginPage(self.w, root_uri='https://www.phptravels.net/login')
