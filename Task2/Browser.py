import selenium
from selenium.webdriver.common.by import By


class Browser:

    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.driver = None

    def open(self, url):
        #webdriver chrome подгружаемый из selenium
        self.driver = selenium.webdriver.Chrome()
        #Получит потом ссылку для открытия
        self.driver.get(url)
        #ожидание чтобы страница окончательно прогрузилась у пользователя
        self.driver.implicitly_wait(5)


    #Функция нахождения элемента страницы по xpath
    def find_element(self, xpath):
        return self.driver.find_element(By.XPATH,xpath)

    def close(self):
        self.driver.quit()
