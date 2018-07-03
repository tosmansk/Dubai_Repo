from page_objects import PageObject, PageElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from phptravels_pages.flights_list import FlightsList
from phptravels_pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as ec


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

        self.w.get_screenshot_as_file("../phptravels_logs/screen_MainPage.{}.png".format(test_name))

    def return_phptravels_page(self):
        """This function returns its page object"""

        return self

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def selct_element(self, element):
        """This function selects passengers amount"""

        action = ActionChains(self.w)
        action.move_to_element(element)
        action.click()
        action.perform()

    def select_flight(self, flight_data_ini):
        """This function selects flight data"""

        # Click on FLIGHTS
        self.flights_button_element.click()

        # Click on Round Trip
        self.RoundTrip_element.click()

        # Provide departure airport
        self.flights_from_text_box_element.click()
        self.flight_from_text_input_element.send_keys(flight_data_ini['from_airport'])

        # During test wait is needed on the element
        flight_choose_element = WebDriverWait(self.w, 2).until(ec.element_to_be_clickable
                                                               ((By.CSS_SELECTOR, "div.select2-result-label")))
        flight_choose_element.click()


        # Provide destination airport
        self.flights_to_text_box_element.click()
        self.flight_to_text_input_element.send_keys(flight_data_ini['to_airport'])
        self.w.implicitly_wait(1)
        self.flight_choose_element.click()

        # Provide departure date
        self.departure_date_element.click()
        self.departure_date_element.send_keys(flight_data_ini['flight_start_date'])

        # Provide return date
        self.return_date_element.click()
        self.return_date_element.send_keys(flight_data_ini['flight_return_date'])

        # Select passangers
        self.total_passengers_element.click()

        # select amounts from config
        if flight_data_ini['adult_passengers'] != "0":
            self.selct_element(self.adult_passengers_element)
            self.apassengers_amount_element.send_keys(flight_data_ini['adult_passengers'])

        if flight_data_ini['child_passengers'] != "0":
            self.selct_element(self.child_passengers_element)
            self.cpassengers_amount_element.send_keys(flight_data_ini['child_passengers'])

        if flight_data_ini['infant_passengers'] != "0":
            self.selct_element(self.infant_passengers_element)
            self.ipassengers_amount_element.send_keys(flight_data_ini['infant_passengers'])

            # Just press to hide selection window
            self.selct_element(self.infant_passengers_element)

        # Press DONE button
        self.passengers_done_button_element.click()

        # Press SEARCH button
        self.selct_element(self.search_button_element)

        # Wait for next page element; Need to be delayed.
        WebDriverWait(self.w, 40).until(lambda driver: driver.title != "PHPTRAVELS | Travel Technology Partner")

        return FlightsList(self.w, root_uri=None)

    def click_loging(self):
        """This function makes logging"""

        # Click on MY ACCOUNT
        self.myaccount_element.click()
        # Click on Login
        self.login_element.click()
        # Return LoginPage object

        return LoginPage(self.w, root_uri='https://www.phptravels.net/login')
