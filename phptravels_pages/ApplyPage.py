from page_objects import PageObject, PageElement


class ApplyPage(PageObject):

    note_element = PageElement(css="textarea.form-control[name='additionalnotes']")

    #personal data elements
    guest1_name_element = PageElement(css="input.form-control[name='passport[1][name]']")
    guest1_passport_element = PageElement(css="input.form-control[name='passport[1][passportnumber]']")
    guest1_age = PageElement(css="input.form-control[name='passport[1][age]']")
    guest2_name_element = PageElement(css="input.form-control[name = 'passport[2][name]']")
    guest2_passport_element = PageElement(css="input.form-control[name='passport[2][passportnumber]']")
    guest2_age = PageElement(css="input.form-control[name='passport[2][age]']")
    guest3_name_element = PageElement(css="input.form-control[name='passport[3][name]']")
    guest3_passport_element = PageElement(css="input.form-control[name='passport[3][passportnumber]']")
    guest3_age = PageElement(css="input.form-control[name='passport[3][age]']")


    """
    TO DO: Mozna sprawdzic dane na stonie:
    <input class="form-control" placeholder="" name="" value="Johny" disabled="disabled" style="background-color: #DEDEDE !important" type="text">
    sprawdzoc czy vale jest value="Johny"
    <input class="form-control" placeholder="" name="" value="Smith" disabled="disabled" style="background-color: #DEDEDE !important" type="text">
    value=Smith    
    """

    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def update_note(self, note="Holidays for three people"):
        """This function updates note with text 'Holidays for three people'"""

        self.note_element.send_keys(note)

    def update_personal_data(self, name1='John', name2='Eva', name3='Lukas', passp1='AJ12345', passp2='AE3456', \
                             passp3='AL9876', age1='45', age2='46', age3='15'):
        """This function populates guest information part"""

        """TO DO: use **kwargs and put dict as argument"""

        # set personal data
        guest1_name = name1
        guest2_name = name2
        guest3_name = name3
        guest1_passport = passp1
        guest2_passport = passp2
        guest3_passport = passp3
        guest1_age = age1
        guest2_age =age2
        guest3_age = age3

        # Send personal_data
        self.guest1_name_element.send_keys(guest1_name)
        self.guest1_passport_element.send_keys(guest1_passport)
        self.guest1_age.send_keys(guest1_age)
        self.guest2_name_element.send_keys(guest2_name)
        self.guest2_passport_element.send_keys(guest2_passport)
        self.guest2_age.send_keys(guest2_age)
        self.guest3_name_element.send_keys(guest3_name)
        self.guest3_passport_element.send_keys(guest3_passport)
        self.guest3_age.send_keys(guest3_age)








