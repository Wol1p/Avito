import time



class AddToFavoritesTest:

    def __init__(self, browser, element_finder):
        self.browser = browser
        self.element_finder = element_finder

    def test_add_to_favorites(self):
        # Переходит на ссылку объявления.
        self.browser.open("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

        # Находит кнопку по полному пути xpath.
        favorite_button = self.element_finder.find_element("/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button")
        # Нажимает кнопку "Добавить в избранное".
        favorite_button.click()
        time.sleep(10)