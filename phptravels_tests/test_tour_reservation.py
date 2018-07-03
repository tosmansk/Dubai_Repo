from selenium import webdriver
import unittest
import logging
from phptravels_pages.credential_page import CredentialPage
from phptravels_pages.main_page import MainPage
from phptravels_tests.read_config_data import ReadConfigData


class DubaiTourReservationTest(unittest.TestCase):
    """This class tests flight reservation"""

    def setUp(self):
        """This function makes test setup"""

        # obtain configuration data
        config = ReadConfigData()

        # config_ini['url'] config_ini['credential_url'] config_ini['browser']
        self.config_ini = config.read_config_ini()

        # personal_data.ini
        self.personal_data_ini = config.read_personal_data_ini()

        # setup webdriver:
        if self.config_ini['browser'] == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.config_ini['browser'] == "Chrome":
            self.driver = webdriver.Chrome()

        # Set basic logging
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='../phptravels_logs/dubai_tour_reservation.log', level=logging.DEBUG,
                            format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_make_tour_reserved(self):
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

        # Check title of login page
        self.assertEqual(mainpage.return_title(), 'PHPTRAVELS | Travel Technology Partner')
        
        # Make login
        loginpage = mainpage.click_loging()

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the LoginPage
        loginpage.make_screenshot(self._testMethodName)

        # Check title of login page
        self.assertEqual(loginpage.return_title(), 'Login')

        # Obtain Login credential
        credentialpage = CredentialPage()
        credentials = credentialpage.retrive_credential_data(self.config_ini['credential_url'])

        # Make login action; accountpage returned
        accountpage = loginpage.make_login(credentials)

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the AccountPage
        accountpage.make_screenshot(self._testMethodName)

        # Check title of account page
        self.assertEqual(accountpage.return_title(), 'My Account')

        # Click TOURS; new Tours Listing page displayed
        tourspage = accountpage.click_tours()

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ToursPage
        tourspage.make_screenshot(self._testMethodName)

        # Check title of tours page
        self.assertEqual(tourspage.return_title(), 'Tours Listings')

        # Provide Dubai data
        bigbuspage = tourspage.send_dubai_data('Dubai')

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the BigBusTourPage
        bigbuspage.make_screenshot(self._testMethodName)

        # Check title of  Big Bus Tour of Dubai page
        self.assertEqual(bigbuspage.return_title(), 'Big Bus Tour of Dubai')

        # Make submit on the page
        applypage = bigbuspage.book_vacation()

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ApplyPage
        applypage.make_screenshot(self._testMethodName)

        # Check title of  Big Bus Tour of Dubai page
        self.assertEqual(applypage.return_title(), 'Big Bus Tour of Dubai')

        # Make note updated on the page, can be overwritten, default use
        applypage.update_note()

        # Set Extras
        applypage.update_extras()

        # Check total prise for this order
        self.assertEqual(applypage.return_total_amount(), '632.5')

        # Make personal data provisioning
        invoicepage = applypage.update_personal_data(self.personal_data_ini)

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ApplyPage
        invoicepage.make_screenshot(self._testMethodName)

        # Check title of  Big Bus Tour of Dubai page
        self.assertEqual(invoicepage.return_title(), 'Invoice')

        # press payment button
        invoicepage.press_pay_button()

    def tearDown(self):
        self.driver.get_screenshot_as_file("../phptravels_logs/screen_{}.png".format(self._testMethodName))
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
