import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://waldemirrr.github.io/todo-list/'
        self.open()

    @allure.step('Открыть страницу списка задач')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Найти существующий элемент')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Элементы отсутствуют')
    def elements_are_not_present(self, locator):
        return len(self.driver.find_elements(*locator)) == 0

    @allure.step('Подсчет элементов')
    def how_many_elements_are_present(self, locator, number_of_elements):
        return len(self.driver.find_elements(*locator)) == number_of_elements
