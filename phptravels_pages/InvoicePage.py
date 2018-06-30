from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InvoicePage(PageObject):

    pay_button_element = PageElement(css="button.btn.btn-default.arrivalpay[data-module='tours']")

    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_InvoicePage{}.png".format(test_name))

    def press_pay_button(self):
        """This function presses PAY ON ARRIVAL"""

        self.pay_button_element.click()
        WebDriverWait(self.w, 6).until(ec.alert_is_present(), 'Timed out waiting for PA creation confirmation '
                                                              'popup to appear.')
        alert = self.w.switch_to.alert
        alert.accept()
