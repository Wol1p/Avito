
class ElementFinder:

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, xpath):
        return self.browser.find_element(xpath)
    
