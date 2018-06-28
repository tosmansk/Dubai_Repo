from page_objects import PageObject, PageElement

from phptravels_pages.ApplyPage import ApplyPage


class BigBusTourPage(PageObject):


    add_child_element = PageElement(css="select.selectx.changeInfo.input-sm[name='child'] > option[value='1']")
    book_button_element = PageElement(css="button.btn.btn-block.btn-action.btn-lg.loader[type='submit']")

    def return_title(self):
        """This function returns page title for assertation"""

        return self.w.title

    def book_vacation(self):
        """This function adds one child within booking option and press submit"""

        """TO DO: add date validation and who and cost
        
        <span style="color:#333333;" class="totalCost">USD $145</span>
        <select style="min-width:50px" name="adults" class="selectx changeInfo input-sm" id="selectedAdults">
                                                    <option value="1">1</option>
                                                    <option value="2" selected="">2</option>
                                                    <option value="3">3</option>
                                                    <option value="4">4</option>
                                                    <option value="5">5</option>
                                                    <option value="6">6</option>
                                                  </select>
        
        """
        # Add option for one child
        self.add_child_element.click()
        # press BOOK NOW button
        self.book_button_element.click()

        return ApplyPage(self.w, root_uri='https://www.phptravels.net/tours/book/\
                                    Big-Bus-Tour-of-Dubai?date=02%2F08%2F2018&adults=2&child=1&infant=0')
