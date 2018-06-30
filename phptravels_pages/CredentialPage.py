from page_objects import PageObject, PageElement
from selenium import webdriver


class CredentialPage(PageObject):
    """This class gets credentials from https://phptravels.com/demo.php"""

    credential_element = PageElement(css="html > body > section.grey-box > div.container > \
    div.rowdiv.wow.fadeInUp.col-md-12.animated > div.resource-box > div.row > div.col-md- 9 > div.col-md-12 > \
    div.row > div.col-md-6 > div.col-md-8 > div.row")

    def obtain_credentials(self):

        credential_string = self.credential_element.text()
        print(credential_string)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://phptravels.com/demo.php')
    obj = CredentialPage(driver)
    obj.obtain_credentials()
