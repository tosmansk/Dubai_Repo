from page_objects import PageObject, PageElement
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from phptravels_pages.flight_invoice import FlightInvoice


class FlightApply(PageObject):
    """This class provision personal data and press confirmation button"""

    first_name_element = PageElement(css="input[placeholder='First Name']")
    last_name_element = PageElement(css="input[placeholder='Last Name']")
    email_element = PageElement(css="input[placeholder='Email']")
    email_confirm_element = PageElement(css="input[placeholder='Confirm Email']")
    contact_number_element = PageElement(css="input[placeholder='Contact Number']")
    address_element = PageElement(css="input[placeholder='Address']")
    country_box_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]"
                                            "/div[1]/form/div[6]/div[2]")
    country_element = PageElement(xpath="//div[10]/div/input")
    select_country_element = PageElement(xpath="//div[10]/ul/li/div/span")
    confirm_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[1]/div[2]/div[3]/button")

    # For assert purpose
    departure_dub_date_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[1]/span")
    arrival_byd_date_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[2]/span")
    departure_dub_time_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[3]/span")
    arrival_byd_time_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[4]/span")
    departure_byd_date_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[5]/span")
    arrival_dub_date_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[6]/span")
    departure_byd_time_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[7]/span")
    arrival_dub_time_element = PageElement(xpath="//div[4]/div/div/div[1]/div/div[2]/ul/li[8]/span")
    total_amount = PageElement(xpath="/html/body/div[4]/div/div/div[1]/div/div[2]/div[4]/table[2]/tbody/tr[2]/td[2]")

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_logs/screen_FlightApply.{}.png".format(test_name))

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def selct_element(self, element):
        """This function selects passengers amount"""

        action = ActionChains(self.w)
        action.move_to_element(element)
        action.click()
        action.perform()

    def flight_apply_assert_data(self):
        """This function stores total amount of prise"""

        fa_assert_data = {}

        """flight data"""
        fa_assert_data['dub_dep_d'] = self.departure_dub_date_element.text
        fa_assert_data['byd_arr_d'] = self.arrival_byd_date_element.text
        fa_assert_data['dub_dep_t'] = self.departure_dub_time_element.text
        fa_assert_data['byd_arr_t'] = self.arrival_byd_time_element.text
        fa_assert_data['byd_dep_d'] = self.departure_byd_date_element.text
        fa_assert_data['dub_arr_d'] = self.arrival_dub_date_element.text
        fa_assert_data['byd_dep_t'] = self.departure_byd_time_element.text
        fa_assert_data['dub_arr_t'] = self.arrival_dub_time_element.text
        fa_assert_data['total_amount'] = self.total_amount.text.split(' ')[1].rstrip('$')

        """
        for k in fa_assert_data.keys():
            print(k + ";" + fa_assert_data[k])
        """
        return fa_assert_data

    def provision_personal_data(self, personal_data_ini):
        """This function provision personal detail for booking"""

        # provision personal details for the order
        self.first_name_element.send_keys(personal_data_ini['guest1']['first_name'])
        self.last_name_element.send_keys(personal_data_ini['guest1']['last_name'])
        self.email_element.send_keys(personal_data_ini['guest1']['email'])
        self.email_confirm_element.send_keys(personal_data_ini['guest1']['email'])
        self.contact_number_element.send_keys(personal_data_ini['guest1']['mphone'])
        self.address_element.send_keys(personal_data_ini['guest1']['address'])
        self.country_box_element.click()
        self.country_element.send_keys(personal_data_ini['guest1']['country'])
        self.select_country_element.click()
        self.confirm_element.click()

        # During testing some sleep need to be made here. Wait conditioning doesn't work well.
        WebDriverWait(self.w, 30).until(lambda driver: driver.title != "PHPTRAVELS | Travel Technology Partner")

        return FlightInvoice(self.w, root_uri=None)

