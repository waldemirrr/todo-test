from test_data.todo_test_data import TodoTestData


test_data = TodoTestData()


def test_write_todo_text_to_input_field(todos_page):
    todos_page.write_text_to_input_field(test_data.COMMON_TODO_TEXT)
    assert todos_page.get_input_field_text() == test_data.COMMON_TODO_TEXT, 'Текст в форме не соотвествует введённому'


def test_select_common_importance(todos_page):
    todos_page.select_importance(test_data.COMMON_IMPORTANCE)
    assert todos_page.is_importance_selected(test_data.COMMON_IMPORTANCE), 'Common важность не выбрана'


def test_select_rare_importance(todos_page):
    todos_page.select_importance(test_data.RARE_IMPORTANCE)
    assert todos_page.is_importance_selected(test_data.RARE_IMPORTANCE), 'Rare важность не выбрана'


def test_select_epic_importance(todos_page):
    todos_page.select_importance(test_data.EPIC_IMPORTANCE)
    assert todos_page.is_importance_selected(test_data.EPIC_IMPORTANCE), 'Epic важность не выбрана'


def test_is_common_importance_default(todos_page):
    assert todos_page.is_importance_selected(test_data.COMMON_IMPORTANCE), 'Common важность не является важностью по умолчанию'


def test_create_common_todo(todos_page):
    todos_page.create_todo(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE)
    assert todos_page.is_correct_todo_created(test_data.COMMON_TODO_TEXT, test_data.COMMON_IMPORTANCE), 'Задача не соответствует заданным данным'


def test_create_rare_todo(todos_page):
    todos_page.create_todo(test_data.RARE_TODO_TEXT, test_data.RARE_IMPORTANCE)
    assert todos_page.is_correct_todo_created(test_data.RARE_TODO_TEXT, test_data.RARE_IMPORTANCE), 'Задача не соответствует заданным данным'


def test_create_epic_todo(todos_page):
    todos_page.create_todo(test_data.EPIC_TODO_TEXT, test_data.EPIC_IMPORTANCE)
    assert todos_page.is_correct_todo_created(test_data.EPIC_TODO_TEXT, test_data.EPIC_IMPORTANCE), 'Задача не соответствует заданным данным'


def test_create_todo_with_blank_text(todos_page):
    todos_page.create_todo('', test_data.EPIC_IMPORTANCE)
    assert todos_page.is_there_no_active_todos(), 'Задача создалась с пустым текстом'


def test_create_todo_with_spaces(todos_page):
    todos_page.create_todo('   ', test_data.EPIC_IMPORTANCE)
    assert todos_page.is_there_no_active_todos(), 'Задача создалась с пробелами'
