import datetime
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from BaseApp import BasePage
from fibonacci_number import find_the_fibonacci_number
from write_csv import write_csv


# Класс с константами для locator
class BankingProject:
    CUSTOMER_LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button"
    )
    USER_SELECT = (By.ID, "userSelect")
    NECESSARY_USER = (By.XPATH, "/html/body/div/div/div[2]/div/form/div/select/option[3]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > form > button")
    ACTION_BUTTON = (By.CSS_SELECTOR,)
    INPUT = (
        By.CSS_SELECTOR,
        "body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input"
    )
    HEADERS = (By.CSS_SELECTOR, "html body div div div table thead tr td")
    CONTENT = (By.CSS_SELECTOR, "html body div div div table tbody tr td")
    DICTIONARY_ACTIONS = {
        'transaction': ('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',),
        'deposit': ('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',),
        'withdrawn': ('body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',),
    }


class SearchHelper(BasePage):
    # Функция авторизации пользователя
    def customer_login(self, delay=2, time=10):
        sleep(delay)
        # Нажатие кнопки Customer Login
        self.find_element(BankingProject.CUSTOMER_LOGIN_BUTTON, time=time).click()
        sleep(delay)
        # Вывод списка пользователей
        element = self.find_element(BankingProject.USER_SELECT, time=time)
        element.click()
        sleep(delay)
        # Выбор нужного пользователей
        self.find_element(BankingProject.NECESSARY_USER, time=time).click()
        sleep(delay)
        # Нажатие кнопки Login
        self.find_element(BankingProject.LOGIN_BUTTON, time=time).click()

    # Функция выбора действий на странице профиля
    def select_actions(self, act, delay=2, time=10):
        action = tuple(BankingProject.DICTIONARY_ACTIONS.get(act))
        number = find_the_fibonacci_number(day=datetime.datetime.now().day)
        sleep(delay)
        # Пополнение или списание со счета
        if act in ('deposit', 'withdrawn'):
            self.find_element(BankingProject.ACTION_BUTTON + action, time=time).click()
            sleep(delay)
            # Ввести сумму пополнения или списания со счета
            element = self.find_element(BankingProject.INPUT, time=time)
            element.click()
            element.clear()
            element.send_keys(number)
            sleep(delay)
            element.send_keys(Keys.ENTER)
        # Просмотр транзакций
        elif act == 'transaction':
            # Переход на страницу с транзакциями
            self.find_element(BankingProject.ACTION_BUTTON + action, time=time).click()
        else:
            raise Exception('Повторите попытку')

    # Функция получение данных на странице с транзакциями
    def parsing_data(self, delay=2):
        sleep(delay)
        # Получение заголовков транзакций
        title = self.find_elements(BankingProject.HEADERS)
        # Получение содержания транзакций
        content = self.find_elements(BankingProject.CONTENT)
        # Запись в csv файл
        write_csv(title=title, content=content)
