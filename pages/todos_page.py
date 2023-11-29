from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.todo_locators import TodoLocators
from pages.base_page import BasePage
from test_data.todo_test_data import TodoTestData
import allure


class TodosPage(BasePage):
    locators = TodoLocators()
    test_data = TodoTestData()

    @allure.step('Написать текст в форму')
    def write_text_to_input_field(self, text):
        self.element_is_present(self.locators.TODO_INPUT).send_keys(text)

    @allure.step('Проверить текст в форме')
    def get_input_field_text(self):
        return self.element_is_present(self.locators.TODO_INPUT).get_attribute('value')

    @allure.step('Выбрать значимость')
    def select_importance(self, importance):
        self.element_is_present(self.locators.pick_importance_class(importance)).click()

    @allure.step('Проверить выбрана ли эта важность задачи')
    def is_importance_selected(self, importance):
        return self.element_is_present(self.locators.pick_importance_id(importance)).is_selected()

    @allure.step('Внести задачу в список')
    def hit_enter_on_todo_creation_input_field(self):
        self.element_is_present(self.locators.TODO_INPUT).send_keys(Keys.ENTER)

    @allure.step('Создание задачи')
    def create_todo(self, text, importance):
        self.write_text_to_input_field(text)
        self.select_importance(importance)
        self.hit_enter_on_todo_creation_input_field()

    @allure.step('Создать три задачи с уникальной важностью')
    def create_three_unique_todos(self):
        self.create_todo(self.test_data.COMMON_TODO_TEXT, self.test_data.COMMON_IMPORTANCE)
        self.create_todo(self.test_data.RARE_TODO_TEXT, self.test_data.RARE_IMPORTANCE)
        self.create_todo(self.test_data.EPIC_TODO_TEXT, self.test_data.EPIC_IMPORTANCE)

    @allure.step('Проверить правильность созданой задачи')
    def is_correct_todo_created(self, text, importance):
        todo_text = self.element_is_present(self.locators.ACTIVE_TODO_TEXT).text
        todo_importance = self.element_is_present(self.locators.ACTIVE_TODO).get_attribute('class')
        return todo_text == text and importance in todo_importance

    @allure.step('Проверить отсуствие активных задач')
    def is_there_no_active_todos(self):
        return self.elements_are_not_present(self.locators.ACTIVE_TODO)

    @allure.step('Проверить наличие активных задач')
    def is_there_active_todos(self):
        return len(self.elements_are_present(self.locators.ACTIVE_TODO)) > 0

    @allure.step('Присутствует ли фильтр')
    def is_filter_present(self):
        return self.element_is_present(self.locators.FILTER_BAR)

    @allure.step('Выбор фильтра')
    def apply_filter(self, importance):
        self.element_is_present(self.locators.pick_filter_class(importance)).click()

    @allure.step('Проверка наличия активной задачи')
    def is_correct_todo_filtered(self, text, importance):
        active_todos = self.driver.find_elements(*self.locators.ACTIVE_TODO)
        is_there_todo = False
        for todo in active_todos:
            todo_text = todo.find_element(By.XPATH, './div[@class="active-todo__text"]').text
            todo_importance = todo.get_attribute('class').split()[1].split('_')[1]
            if importance == todo_importance and text == todo_text:
                is_there_todo = True
            else:
                return False
        return is_there_todo

    @allure.step('Отфильтровать все задачи')
    def is_all_filtered(self, number_of_elements):
        return self.how_many_elements_are_present(self.locators.ACTIVE_TODO, number_of_elements)

    @allure.step('')
    def complete_todo(self, text, importance):
        todo = self.find_specific_todo(text, importance)
        todo.find_element(By.XPATH, './img[contains(@class, "active-todo__icon")]').click()

    @allure.step('Выполнить все активные задачи')
    def complete_all_todos(self):
        active_todos = self.driver.find_elements(*self.locators.ACTIVE_TODO)
        for todo in active_todos:
            todo.find_element(By.XPATH, './img[contains(@class, "active-todo__icon")]').click()

    @allure.step('Проверить отсутствие выполненных задач')
    def is_there_no_completed_todos(self):
        return self.elements_are_not_present(self.locators.COMPLETED_TODO)

    @allure.step('Проверить наличие правильного количества выполненных задач')
    def is_there_right_amount_of_completed_todos(self, number_of_elements):
        return self.how_many_elements_are_present(self.locators.COMPLETED_TODO, number_of_elements)

    @allure.step('Удалить все задачи')
    def delete_todo(self, text, importance):
        todo = self.find_specific_todo(text, importance)
        todo.find_elements(By.XPATH, './/img[contains(@class, "active-todo__icon")]')[2].click()

    @allure.step('Редактировать задачу')
    def edit_todo_text(self, text, importance, edited_text):
        todo = self.find_specific_todo(text, importance)
        todo.find_elements(By.XPATH, './/img[contains(@class, "active-todo__icon")]')[1].click()
        self.driver.find_element(By.CSS_SELECTOR, '.active-todo__editing-textarea').send_keys(edited_text)
        self.driver.find_element(By.CSS_SELECTOR, '.active-todo__editing-submit').click()

    @allure.step('Найти конкретную задачу')
    def find_specific_todo(self, text, importance):
        active_todos = self.driver.find_elements(*self.locators.ACTIVE_TODO)
        for todo in active_todos:
            todo_text = todo.find_element(By.XPATH, './div[@class="active-todo__text"]').text
            todo_importance = todo.get_attribute('class').split()[1].split('_')[1]
            if importance == todo_importance and text == todo_text:
                return todo

    @allure.step('Есть ли конкретная задача')
    def is_there_specific_todo(self, text, importance):
        active_todos = self.driver.find_elements(*self.locators.ACTIVE_TODO)
        for todo in active_todos:
            todo_text = todo.find_element(By.XPATH, './div[@class="active-todo__text"]').text
            todo_importance = todo.get_attribute('class').split()[1].split('_')[1]
            if importance == todo_importance and text == todo_text:
                return True
