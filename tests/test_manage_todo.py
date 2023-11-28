from test_data.todo_test_data import TodoTestData


test_data = TodoTestData()


def test_complete_todo(todos_page):
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    todos_page.complete_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    assert todos_page.is_there_no_active_todos(), ''
    assert todos_page.is_there_right_amount_of_completed_todos(1), ''


def test_delete_todo(todos_page):
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    todos_page.delete_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    assert todos_page.is_there_no_active_todos()


def test_edit_todo(todos_page):
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    todos_page.edit_todo_text(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE, ' редактирована')
    assert todos_page.is_there_specific_todo(test_data.COMMON_TODO_TEXT + ' редактирована', test_data.COMMON_IMPORTANCE)
