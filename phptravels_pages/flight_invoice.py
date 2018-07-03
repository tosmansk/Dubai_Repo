from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class FlightInvoice(PageObject):
    """This class apply payment"""

    # Element to press PAY ON ARRIVAL
    pay_on_arrival_element = PageElement(css="button.arrivalpay")
    # assert data
    byd_departure_date_element = PageElement(xpath="//div[4]/div[2]/div/table[1]/tbody/tr[4]/td/table[1]/tbody/tr[2]"
                                                   "/td/table[2]/tbody/tr[2]/td[1]/p")
    dub_arrival_date_element = PageElement(xpath="//div[4]/div[2]/div/table[1]/tbody/tr[4]/td/table[1]/tbody/tr[2]"
                                                   "/td/table[2]/tbody/tr[3]/td[1]/p")
    dub_departure_date_element = PageElement(xpath="//div[4]/div[2]/div/table[1]/tbody/tr[4]/td/table[1]/tbody/tr[2]"
                                                   "/td/div[2]/table/tbody/tr[2]/td[1]/p")
    byd_arrival_date_element = PageElement(xpath="//div[4]/div[2]/div/table[1]/tbody/tr[4]/td/table[1]/tbody/tr[2]"
                                                 "/td/div[2]/table/tbody/tr[3]/td[1]/p")
    total_amount_element = PageElement(xpath="//div[4]/div[2]/div/table[1]/tbody/tr[4]/td/table[2]/tbody/tr/td[3]")


    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_logs/screen_MainPage.{}.png".format(test_name))

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def fight_invoice_asser_data(self):
        """assert data"""

        invoice_assert_data = {}

        invoice_assert_data['byd_dep_d'] = self.byd_departure_date_element.text
        invoice_assert_data['dub_arr_d'] = self.dub_arrival_date_element.text
        invoice_assert_data['dub_dep_d'] = self.dub_departure_date_element.text
        invoice_assert_data['byd_arr_d'] = self.byd_arrival_date_element.text
        invoice_assert_data['total_amount'] = self.total_amount_element.text.split(' ')[1].strip("$")

        """
        for k in invoice_assert_data.keys():
            print(k + ";" + invoice_assert_data[k])
        """
        return invoice_assert_data

    def pay_on_arrival(self):
        """This function make pay on arrival button press"""

        for loop in range(3):
            try:
                self.pay_on_arrival_element.click()
                WebDriverWait(self.w, 2).until(ec.alert_is_present(), 'Timed out waiting for PA creation confirmation '
                                                                   'popup to appear.')
                break
            except:
                print("Retry")

        alert = self.w.switch_to.alert
        alert.accept()