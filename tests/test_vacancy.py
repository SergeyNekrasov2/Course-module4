from src.vacancy import Vacancy


def test_init_vacancy(test_add_vacancy):
    assert test_add_vacancy.name == "Python Developer"
    assert test_add_vacancy.url == "<https://hh.ru/vacancy/123456>"
    assert test_add_vacancy.salary == {'from': 100000, 'to': 150000}
    assert test_add_vacancy.snippet == "Требования: опыт работы от 3 лет..."

    Vacancy().clear_list()


def test_list_vacancies(test_add_vacancy, test_result_filtered_vacancy):
    assert test_add_vacancy.list_vacancies()[0] == test_result_filtered_vacancy

    Vacancy().clear_list()


def test_filtered_salary_vacancy(capsys, vacancy_1, vacancy_2, test_result_filtered_vacancy):
    assert len(Vacancy.list_vacancies()) == 2

    Vacancy.filtered_salary(0, 150000)
    message = capsys.readouterr()
    assert message.out.strip() == f"{test_result_filtered_vacancy}"

    Vacancy().clear_list()


def test_ge_vacancy(capsys, vacancy_1, vacancy_2):
    print(Vacancy.__ge__(vacancy_2, vacancy_1))
    message = capsys.readouterr()
    assert message.out.strip() == 'True'

    Vacancy().clear_list()


def test_cast_to_object_list(test_cast_to_object_vacancy, test_cast_to_add_vacancy):
    Vacancy().clear_list()
    Vacancy.cast_to_object_list(test_cast_to_object_vacancy)
    assert Vacancy.list_vacancies() == test_cast_to_add_vacancy