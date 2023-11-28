from test_data.todo_test_data import TodoTestData


test_data = TodoTestData()


def test_filter_is_present_when_there_is_todos(todos_page):
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    assert todos_page.is_filter_present(), 'Панель фильтров не появилась при созданных задачах'


def test_filter_common(todos_page):
    todos_page.create_three_unique_todos()
    todos_page.apply_filter(test_data.COMMON_IMPORTANCE)
    assert todos_page.is_correct_todo_filtered(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE), 'Фильтр не сработал для фильтрации common задач'


def test_filter_rare(todos_page):
    todos_page.create_three_unique_todos()
    todos_page.apply_filter(test_data.RARE_IMPORTANCE)
    assert todos_page.is_correct_todo_filtered(test_data.RARE_TODO_TEXT, test_data.RARE_IMPORTANCE), 'Фильтр не сработал для фильтрации rare задач'


def test_filter_epic(todos_page):
    todos_page.create_three_unique_todos()
    todos_page.apply_filter(test_data.EPIC_IMPORTANCE)
    assert todos_page.is_correct_todo_filtered(test_data.EPIC_TODO_TEXT, test_data.EPIC_IMPORTANCE), 'Фильтр не сработал для фильтрации epic задач'


def test_filter_all(todos_page):
    todos_page.create_three_unique_todos()
    assert todos_page.is_all_filtered(3), 'Фильтр не показал всех задач'


def test_delete_completed(todos_page):
    todos_page.create_three_unique_todos()
    todos_page.complete_all_todos()
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    todos_page.apply_filter('_delete-completed')
    assert todos_page.is_there_active_todos(), 'Удалились активные задачи'
    assert todos_page.is_there_no_completed_todos(), 'Не удалились выполенные задачи'
