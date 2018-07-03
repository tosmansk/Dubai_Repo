from selenium import webdriver
import unittest
import logging
from phptravels_pages.main_page import MainPage
from phptravels_tests.read_config_data import ReadConfigData


class DubaiFightReservationTest(unittest.TestCase):
    """This class tests vacation reservation"""

    def setUp(self):
        """This function makes test setup"""

        # obtain configuration data
        config = ReadConfigData()

        # config_ini['url'] config_ini['credential_url'] config_ini['browser']
        self.config_ini = config.read_config_ini()

        # personal_data.ini
        self.personal_data_ini = config.read_personal_data_ini()

        # Obtain flight_data.ini file
        self.flight_data_ini = config.read_flight_data_ini()

        # setup webdriver:
        if self.config_ini['browser'] == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.config_ini['browser'] == "Chrome":
            self.driver = webdriver.Chrome()

        # Set basic logging
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='../phptravels_logs/flight_reservation.log', level=logging.DEBUG,
                            format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_make_flight_reserved(self):
        """This function makes call PO pages and performs some action and checks on them"""

        # Set local veriables
        driver = self.driver
        url = self.config_ini['url']
        browser = self.config_ini['browser']
        log = self.log

        # Login MainPage
        driver.get(url)
        mainpage = MainPage(driver, url)

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the MainPage
        mainpage.make_screenshot(self._testMethodName)

        # Check title of Main page
        self.assertEqual(mainpage.return_title(), 'PHPTRAVELS | Travel Technology Partner')

        # Search the flight
        flightslistpage = mainpage.select_flight(self.flight_data_ini)

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the FlightsList page
        flightslistpage.make_screenshot(self._testMethodName)

        # Check title of Flights List page
        self.assertEqual(flightslistpage.return_title(), 'Flights List')

        # assert data FlightsList dict
        flightslist_asser_data = flightslistpage.flights_list_assert_data()

        # Select flight from list
        flightapply = flightslistpage.select_flight()

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the FlightApply
        flightapply.make_screenshot(self._testMethodName)

        # Check title of flightapply page
        self.assertEqual(flightapply.return_title(), 'PHPTRAVELS | Travel Technology Partner')

        # Assert data dict FlightApply
        flightapply_assert_data = flightapply.flight_apply_assert_data()

        # Provision personal details for booking
        flightinvoice = flightapply.provision_personal_data(self.personal_data_ini)

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the FlightApply
        flightinvoice.make_screenshot(self._testMethodName)

        # Check title of flightapply page
        self.assertEqual(flightinvoice.return_title(), 'Invoice')

        # Assert Data dict of FlightInvoice
        flightinvoice.fight_invoice_asser_data()

        # Apply payment
        flightinvoice.pay_on_arrival()

    def tearDown(self):
        self.driver.get_screenshot_as_file("../phptravels_logs/screen_{}.png".format(self._testMethodName))
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
