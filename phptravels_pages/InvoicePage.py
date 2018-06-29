from page_objects import PageObject, PageElement


class InvoicePage(PageObject):

    pay_button_element = PageElement(css="button.btn.btn-default.arrivalpay[data-module='tours']")

    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def make_screenshot(self):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_utils/screen_InvoicePage.png")

    def press_pay_button(self):
        """This function presses PAY ON ARRIVAL"""

        print(self.w.current_url)
        self.pay_button_element.click()