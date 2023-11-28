from selenium.webdriver.common.by import By


class TodoLocators:
    TODO_INPUT = (By.CSS_SELECTOR, '.todo-form__text-input')
    ACTIVE_TODO = (By.CSS_SELECTOR, '.active-todo')
    ACTIVE_TODO_TEXT = (By.CSS_SELECTOR, '.active-todo__text')
    COMPLETED_TODO = (By.CSS_SELECTOR, '.completed-todo')
    FILTER_BAR = (By.CSS_SELECTOR, '.filter-group')
    FILTER_COMMON = (By.CSS_SELECTOR, '.filter-button_common')
    FILTER_RARE = (By.CSS_SELECTOR, '.filter-button_rare')
    FILTER_EPIC = (By.CSS_SELECTOR, '.filter-button_epic')
    FILTER_ALL = (By.CSS_SELECTOR, '.filter-button_all')
    FILTER_DELETE_COMPLETED = (By.CSS_SELECTOR, '.filter-button__delete-completed')

    def pick_importance_class(self, importance):
        selected_importance_class = (By.CSS_SELECTOR, f'.todo-form__importance-button_{importance}')
        return selected_importance_class

    def pick_importance_id(self, importance):
        selected_importance_id = (By.CSS_SELECTOR, f'#{importance}')
        return selected_importance_id

    def pick_filter_class(self, importance):
        filter_importance_class = (By.CSS_SELECTOR, f'.filter-button_{importance}')
        return filter_importance_class
