from src.json_saver import JSONSaver
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/test_add_vacancy.json")

def test_add_vacancy_json_saver(test_add_vacancy):
    test_vacancy = test_add_vacancy

    json_saver = JSONSaver(file_path)
    json_saver.add_vacancy(test_vacancy)

    # Ожидаемое содержимое файла
    test_read_file = (
        '[\n'
        '    {\n'
        '        "name": "Python Developer",\n'
        '        "url": "<https://hh.ru/vacancy/123456>",\n'
        '        "salary": {\n'
        '            "from": 100000,\n'
        '            "to": 150000\n'
        '        },\n'
        '        "snippet": "Требования: опыт работы от 3 лет..."\n'
        '    }\n'
        ']'
    )

    with open(file_path, encoding="utf-8") as file:
        assert test_read_file == file.read()



def test_delete_vacancy_json_saver(test_add_vacancy):
    test_vacancy = test_add_vacancy

    json_saver = JSONSaver(file_path)
    json_saver.add_vacancy(test_vacancy)
    json_saver.delete_vacancy(test_vacancy)

    with open(file_path, encoding="utf-8") as file:
        expected = '[]'
        assert expected == file.read()