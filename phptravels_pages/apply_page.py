from page_objects import PageObject, PageElement
from selenium.webdriver.support.wait import WebDriverWait
from phptravels_pages.invoice_page import InvoicePage


class ApplyPage(PageObject):
    note_element = PageElement(css="textarea.form-control[name='additionalnotes']")

    # personal data elements
    guest1_name_element = PageElement(css="input.form-control[name='passport[1][name]']")
    guest1_passport_element = PageElement(css="input.form-control[name='passport[1][passportnumber]']")
    guest1_age = PageElement(css="input.form-control[name='passport[1][age]']")
    guest2_name_element = PageElement(css="input.form-control[name = 'passport[2][name]']")
    guest2_passport_element = PageElement(css="input.form-control[name='passport[2][passportnumber]']")
    guest2_age = PageElement(css="input.form-control[name='passport[2][age]']")
    guest3_name_element = PageElement(css="input.form-control[name='passport[3][name]']")
    guest3_passport_element = PageElement(css="input.form-control[name='passport[3][passportnumber]']")
    guest3_age = PageElement(css="input.form-control[name='passport[3][age]']")

    # confirmation button
    confirm_button = PageElement(css="button.btn.btn-success.btn-lg.btn-block.completebook[type = 'submit']")

    # 3 Nights Accomodation
    extras_nights_element = PageElement(xpath='//div[4]/div/div/div[1]/div/form/div[2]/table/tbody/tr[2]/td[4]'
                                              '/label/span/span[2]')
    extras_insurance_element = PageElement(xpath='//div[4]/div/div/div[1]/div/form/div[2]/table/tbody/tr[3]/td[4]'
                                                 '/label/span/span[2]')
    extras_aiport_pickup_element = PageElement(xpath='//div[4]/div/div/div[1]/div/form/div[2]/table/tbody/tr[4]'
                                                     '/td[4]/label/span/span[2]')
    # Summary
    total_amount = PageElement(xpath='//*[@id="displaytotal"]')

    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def update_note(self, note="Holidays for three people"):
        """This function updates note with text 'Holidays for three people'"""

        self.note_element.send_keys(note)

    def make_screenshot(self, test_name):
        """This function makes screenshot of the page"""

        self.w.get_screenshot_as_file("../phptravels_logs/screen_ApplyPage{}.png".format(test_name))

    def update_extras(self):
        """This function sets extra options"""

        self.extras_nights_element.click()
        self.extras_insurance_element.click()
        self.extras_aiport_pickup_element.click()

    def return_total_amount(self):
        """This function returns total cost"""

        return self.total_amount.text

    def update_personal_data(self, personal_data_ini):
        """This function provision personal data """

        # set personal data
        guest1_name = personal_data_ini['guest1']['first_name'] + personal_data_ini['guest1']['first_name']
        guest2_name = personal_data_ini['guest2']['first_name'] + personal_data_ini['guest2']['first_name']
        guest3_name = personal_data_ini['guest3']['first_name'] + personal_data_ini['guest3']['first_name']

        # Send personal_data
        self.guest1_name_element.send_keys(guest1_name)
        self.guest1_passport_element.send_keys(personal_data_ini['guest1']['passport'])
        self.guest1_age.send_keys(personal_data_ini['guest1']['age'])
        self.guest2_name_element.send_keys(guest2_name)
        self.guest2_passport_element.send_keys(personal_data_ini['guest2']['passport'])
        self.guest2_age.send_keys(personal_data_ini['guest1']['age'])
        self.guest3_name_element.send_keys(guest3_name)
        self.guest3_passport_element.send_keys(personal_data_ini['guest3']['passport'])
        self.guest3_age.send_keys(personal_data_ini['guest1']['age'])
        self.confirm_button.click()

        WebDriverWait(self.w, 30).until(lambda driver: driver.title != "Big Bus Tour of Dubai")

        return InvoicePage(self.w, root_uri=None)
