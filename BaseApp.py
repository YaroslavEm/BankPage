from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Инициализация класса
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    # Поиск элемента, подходящего под условие locator
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # Поиск списка элементов, подходящих под условие locator
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # Открытие браузера и переход на страницу сайта
    def go_to_site(self):
        return self.driver.get(self.base_url)
