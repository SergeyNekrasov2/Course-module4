from typing import List

import pytest

from src.operations_with_vacancies import OperationsWithVacancies, SalaryOfVacancies


def test_operations_with_vacancies(input_test_operations_with_vacancies: List) -> None:
    sorted_vacancies = OperationsWithVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert sorted_vacancies._keyword == "python"
    assert sorted_vacancies._keyword_2 == "Junior"
    assert sorted_vacancies._employment == "Полная занятость"
    assert sorted_vacancies._currency == "RUR"
    assert sorted_vacancies._pay_from == 50_000
    assert sorted_vacancies._pay_to == 100_000
    assert sorted_vacancies._sorted_vacancies == []


def test_salary_of_vacancies_get_max_avg_salary(return_test_get_max_avg_salary: List) -> None:
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    assert salary_vacancies._get_max_avg_salary() == return_test_get_max_avg_salary


def test_salary_of_vacancies_more_or_less(return_test_get_max_avg_salary: List, capsys: pytest.CaptureFixture) -> None:
    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    salary_vacancies_2 = SalaryOfVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    if salary_vacancies > salary_vacancies_2:
        print("Python vacancies have a higher average salary.")
    elif salary_vacancies < salary_vacancies_2:
        print("Java vacancies have a higher average salary.")
    else:
        print("Both have the same average salary.")
    message = capsys.readouterr()
    assert message.out.strip() == "Java vacancies have a higher average salary."

    if salary_vacancies != salary_vacancies_2:
        print("Не равно.")
    else:
        print("Равно.")
    message = capsys.readouterr()
    assert message.out.strip() == "Не равно."