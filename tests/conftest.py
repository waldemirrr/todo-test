from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.todos_page import TodosPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


@pytest.fixture()
def todos_page(driver):
    todos_page = TodosPage(driver)
    return todos_page



