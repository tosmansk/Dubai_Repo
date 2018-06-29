import configparser

from selenium import webdriver
import unittest
import logging
from phptravels_pages.MainPage import MainPage


class DubaiVacationTest(unittest.TestCase):
    """This class tests vacation reservation"""

    def setUp(self):
        """This function makes test setup"""

        # obtain configuration data from config.ini
        config = configparser.ConfigParser()
        config.read('../phptravels_utils/config.ini')
        self.url = config['Selenium']['url']
        self.browser = config['Selenium']['browser']

        # setup webdriver:
        if self.browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "Chrome":
            self.driver = webdriver.Chrome()

        # Set basic logging
        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename='../phptravels_utils/dubai_test.log', level=logging.INFO, format=logging_format)
        self.log = logging.getLogger(__name__)

    def test_makevacationorganized(self):
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
        mainpage.make_screenshot()
        
        # Make login
        loginpage = mainpage.make_loging()

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the LoginPage
        loginpage.make_screenshot()

        # Check title of login page
        self.assertEqual(loginpage.return_title(), 'Login')

        # Make login action; accountpage returned
        accountpage = loginpage.make_login()

        # Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the AccountPage
        accountpage.make_screenshot()

        # Check title of account page
        self.assertEqual(accountpage.return_title(), 'My Account')

        # Click TOURS; new Tours Listing page displayed
        tourspage = accountpage.click_tours()

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ToursPage
        tourspage.make_screenshot()

        # Check title of tours page
        self.assertEqual(tourspage.return_title(), 'Tours Listings')

        # Provide Dubai data
        bigbuspage = tourspage.send_dubai_data('Dubai')

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the BigBusTourPage
        bigbuspage.make_screenshot()

        # Check title of  Big Bus Tour of Dubai page
        self.assertEqual(bigbuspage.return_title(), 'Big Bus Tour of Dubai')

        # Make submit on the page
        applypage = bigbuspage.book_vacation()

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ApplyPage
        applypage.make_screenshot()

        # Check title of  Big Bus Tour of Dubai page
        self.assertEqual(applypage.return_title(), 'Big Bus Tour of Dubai')

        # Make note updated on the page, can be overwritten, default use
        applypage.update_note()

        # Make personal data provisioning
        invoicepage = applypage.update_personal_data()

        #  Make browser and  url logged
        log.info('{0} LOGGED URL: {1}'.format(browser, driver.current_url))

        # Make screenshot of the ApplyPage
        invoicepage.make_screenshot()

        # Check title of  Big Bus Tour of Dubai page
        #self.assertEqual(invoicepage.return_title(), 'Invoice')

        invoicepage.press_pay_button()


if __name__ == '__main__':
    unittest.main()
