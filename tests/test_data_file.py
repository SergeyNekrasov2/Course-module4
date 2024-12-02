import json
import unittest
from typing import Any
from unittest.mock import mock_open, patch

from src.data_file import GetData, SaveData


def test_save_data_json_decode_error(save_data_instance: SaveData) -> None:
    m = mock_open(read_data="invalid json")

    with patch("builtins.open", m):
        with patch("json.dump") as mock_dump:
            with patch.object(
                save_data_instance, "_comparison_pay", return_value=[{"vacancy": "Developer", "salary": 50000}]
            ):
                result = save_data_instance._save_data()

            mock_dump.assert_called_once()
            assert result == [{"vacancy": "Developer", "salary": 50000}]

            # Assertions
            mock_dump.assert_called_once()
            assert result == [{"vacancy": "Developer", "salary": 50000}]


class TestGetData(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [
                {
                    "name": "Разработчик Python",
                    "employment": {"name": "Полная занятость"},
                    "salary": {"currency": "RUB", "from": 80000, "to": 120000},
                },
                {
                    "name": "Junior Python Developer",
                    "employment": {"name": "Стажировка"},
                    "salary": {"currency": "RUB", "from": 30000, "to": 50000},
                },
            ]
        ),
    )
    def test_get_data_success(self, mock_file: Any) -> None:
        # arrange
        keyword = "Python"
        keyword_2 = "Разработчик"
        employment = "Полная занятость"
        currency = "RUB"
        pay_from = 80000
        pay_to = 120000
        get_data_instance = GetData(keyword, keyword_2, employment, currency, pay_from, pay_to)

        result = get_data_instance._get_data()

        expected_result = [
            {
                "name": "Разработчик Python",
                "employment": {"name": "Полная занятость"},
                "salary": {"currency": "RUB", "from": 80000, "to": 120000},
            }
        ]
        self.assertEqual(result, expected_result)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_data_empty_file(self, mock_file: Any) -> None:
        # arrange
        keyword = "Python"
        keyword_2 = "Разработчик"
        employment = "Полная занятость"
        currency = "RUB"
        pay_from = 80000
        pay_to = 120000
        get_data_instance = GetData(keyword, keyword_2, employment, currency, pay_from, pay_to)

        # act
        result = get_data_instance._get_data()

        # assert
        self.assertEqual(result, "Файл пустой")