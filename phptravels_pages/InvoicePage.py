from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

        print(self.w.current_url)
        self.pay_button_element.click()

        """TO DO: Make click on pop-up window"""


        WebDriverWait(self.w, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

        alert = self.w.switch_to.alert
        alert.accept()
