from AddToFavorite import AddToFavoritesTest
from FindFavorite import ElementFinder
from Browser import Browser


def main():
    # Создает браузер
    browser = Browser("chrome")

    # Создает объект для поиска элементов на странице
    element_finder = ElementFinder(browser)

    # Выполняет тест
    AddToFavoritesTest(browser, element_finder).test_add_to_favorites()

    # Закрывает браузер
    browser.close()


if __name__ == "__main__":
    main()