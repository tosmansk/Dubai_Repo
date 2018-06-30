import configparser
from selenium import webdriver
import unittest
import logging
from phptravels_pages.MainPage import MainPage


class DubaiFightReservationTest(unittest.TestCase):
    """This class tests vacation reservation"""

    def setUp(self):
        """This function makes test setup"""

        # obtain configuration data from config.ini
        config = configparser.ConfigParser()
        config.read('../phptravels_utils/config.ini')
        self.url = config['Selenium']['url']
        self.browser = config['Selenium']['browser']

        # Obtain flight data from ini file
        config.read('../phptravels_utils/flight_data.ini')

        self.flight_data = {}

        self.flight_data['from_airport'] = config['FlightData']['from_airport']
        self.flight_data['to_airport'] = config['FlightData']['to_airport']
        self.flight_data['start_date'] = config['FlightData']['flight_start_date']
        self.flight_data['return_date'] = config['FlightData']['flight_return_date']
        self.flight_data['apassengers'] = config['FlightData']['adult_passengers']
        self.flight_data['cpassengers'] = config['FlightData']['child_passengers']
        self.flight_data['ipassengers'] = config['FlightData']['infant_passengers']

        # setup webdriver:
        if self.browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "Chrome":
            self.driver = webdriver.Chrome()

        # Set basic logging
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='../phptravels_utils/flight_reservation.log', level=logging.DEBUG,
                            format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_make_flight_reserved(self):
        """This function makes call PO pages and performs some action and checks on them"""

        # Set local veriables
        driver = self.driver
        url = self.url
        browser = self.browser
        log = self.log

        # Login MainPage
        driver.get(url)
        mainpage = MainPage(driver, url)

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the MainPage
        mainpage.make_screenshot(self._testMethodName)
        # Search the flight
        mainpage.select_flight(self.flight_data)

    def tearDown(self):
        self.driver.get_screenshot_as_file("../phptravels_utils/screen_{}.png".format(self._testMethodName))
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()