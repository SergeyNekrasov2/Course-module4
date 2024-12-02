import unittest
from typing import Any, List
from unittest.mock import patch

import pytest

from src.user_interaction import get_vacations_with_keyword, search, top_vacations


@pytest.mark.parametrize(
    "keyword, keyword_2, emp, curr, pey_from, pray_to, expected_output",
    [
        (
            "java",
            "Junior",
            "Полная занятость",
            "RUR",
            "50_000",
            "100_000",
            [
                "Имя вакансии - Junior Java разработчик,месторасположение - Новосибирск,средняя зарплата - 72500.0,валюта - RUR,url - https://hh.ru/vacancy/111396633",
                "Имя вакансии - Junior Java Developer,месторасположение - Москва,средняя зарплата - 60000.0,валюта - RUR,url - https://hh.ru/vacancy/110429201",
                "Имя вакансии - Тестировщик (Junior),месторасположение - Санкт-Петербург,средняя зарплата - 65000.0,валюта - RUR,url - https://hh.ru/vacancy/111211488",
                "Имя вакансии - Junior Java разработчик,месторасположение - Москва,средняя зарплата - 80000.0,валюта - RUR,url - https://hh.ru/vacancy/109788485",
            ],
        ),
    ],
)
def test_search(
    keyword: str, keyword_2: str, emp: str, curr: str, pey_from: str, pray_to: str, expected_output: List
) -> None:
    assert search(keyword, keyword_2, emp, curr, pey_from, pray_to) == expected_output


@pytest.mark.parametrize(
    "keyword, quantity, expected_output",
    [
        (
            "java",
            "2",
            [
                {
                    "имя вакансии": "Java разработчик",
                    "месторасположение": "Минск",
                    "средняя зарплата": 2000.0,
                    "валюта": "EUR",
                    "url": "https://hh.ru/vacancy/111249438",
                },
                {
                    "имя вакансии": "Frontend-разработчик",
                    "месторасположение": "Минск",
                    "средняя зарплата": 3600.0,
                    "валюта": "BYR",
                    "url": "https://hh.ru/vacancy/111112280",
                },
            ],
        )
    ],
)
def test_top_vacancies(keyword: str, quantity: str, expected_output: List) -> None:
    assert top_vacations(keyword, quantity) == expected_output


class TestGetVacationsWithKeyword(unittest.TestCase):

    @patch("src.user_interaction.GetVacancies")
    def test_get_vacations_with_keyword(self, mock_get_vacancies: Any) -> Any:
        mock_vacancies_data = [
            {
                "name": "Software Engineer",
                "area": {"name": "New York"},
                "salary": {"from": 100000, "to": 120000, "currency": "USD"},
                "alternate_url": "http://example.com/vacancy1",
            },
            {
                "name": "Data Scientist",
                "area": {"name": "San Francisco"},
                "salary": {"from": 110000, "to": 130000, "currency": "USD"},
                "alternate_url": "http://example.com/vacancy2",
            },
            {
                "name": "Product Manager",
                "area": {"name": "Los Angeles"},
                "salary": None,  # Вакансия без зарплаты
                "alternate_url": "http://example.com/vacancy3",
            },
        ]

        mock_instance = mock_get_vacancies.return_value
        mock_instance._loading.return_value = mock_vacancies_data

        result = get_vacations_with_keyword("Engineer")

        self.assertIn("Software Engineer", result)
        self.assertIn("New York", result)
        self.assertIn("100000", result)
        self.assertIn("120000", result)
        self.assertIn("USD", result)

        self.assertNotIn("Product Manager", result)