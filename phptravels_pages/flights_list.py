from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from phptravels_pages.flight_apply import FlightApply


class FlightsList(PageObject):
    """This class makes simple selection of the flight"""

    select_first_flight = PageElement(xpath="//*[@id='bookbtn']")

    # Data for asertation from selected Flights Listing page
    # BYD -> DBX
    byd_start_date_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]"
                                               "/div[2]/p[2]/small")
    byd_landing_date_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]"
                                                 "/div[3]/p[1]/strong")
    byd_landing_time_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[3]"
                                                 "/div[3]/p[2]")
    dub_start_date_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[3]"
                                               "/div[2]/p[2]/small")
    dub_landing_date_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[3]" \
                                                "/div[3]/p[1]/strong")
    dub_landing_time_element = PageElement(xpath="//div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]"
                                                 "/div[3]/p[2]")
    book_and_prise_element = PageElement(xpath="/html/body/div[4]/div[4]/div/div[3]/div[1]/table/tbody/tr[1]/td"
                                               "/div[2]/p")

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_logs/screen_FlightsListPage.{}.png".format(test_name))

    def return_title(self):
        """This function returns page title"""

        return self.w.title

    def flights_list_assert_data(self):
        select_first_flight = WebDriverWait(self.w, 10).until(ec.element_to_be_clickable
                                                              ((By.XPATH, "//*[@id='bookbtn']")))
        fl_assert_data = {}

        fl_assert_data['byd_dep_t'] = self.byd_start_date_element.text.split(' ')[0]
        fl_assert_data['byd_dep_d'] = self.byd_start_date_element.text.split(' ')[1].lstrip('(').rstrip(')')
        fl_assert_data['byd_arr_d'] = self.byd_landing_date_element.text
        fl_assert_data['byd_arr_t'] = self.byd_landing_time_element.text
        fl_assert_data['dub_dep_t'] = self.dub_start_date_element.text.split(' ')[0]
        fl_assert_data['dub_dep_d'] = self.dub_start_date_element.text.split(' ')[1].lstrip('(').rstrip(')')
        fl_assert_data['dub_arr_d'] = self.dub_landing_date_element.text
        fl_assert_data['dub_arr_t'] = self.dub_landing_time_element.text
        fl_assert_data['total_amount'] = self.book_and_prise_element.text.split(' ')[1].split('$')[0]

        """
        for k in fl_assert_data.keys():
            print(k +";" + fl_assert_data[k])
        """
        return fl_assert_data

    def select_flight(self):
        """This function selects first flight on the list"""

        select_first_flight = WebDriverWait(self.w, 10).until(ec.element_to_be_clickable
                                                               ((By.XPATH, "//*[@id='bookbtn']")))
        select_first_flight.click()

        WebDriverWait(self.w, 30).until(lambda driver: driver.title != "Flights List")

        return FlightApply(self.w, root_uri=None)





