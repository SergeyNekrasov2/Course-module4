import json
from abc import ABC, abstractmethod
from typing import Any

from src.operations_with_vacancies import OperationsWithVacancies, SalaryOfVacancies


class AbstractSave(ABC):
    """Абстрактный класс, который обязывает реализовать метод для добавления вакансий в файл"""

    @abstractmethod
    def _save_data(self) -> Any:
        """Метод для добавления вакансий в файл, который должен быть в дочернем классе"""
        pass


class AbstractGet(ABC):
    """Абстрактный класс, который обязывает реализовать метод для получения данных из файла по указанным критериям"""

    @abstractmethod
    def _get_data(self) -> Any:
        """Метод для получения данных из файла по указанным критериям, который должен быть в дочернем классе"""
        pass


class AbstractDelete(ABC):
    """Абстрактный класс, который обязывает реализовать метод для удаления информации о вакансиях"""

    @abstractmethod
    def _delete_data(self) -> Any:
        """Метод для удаления информации о вакансиях, который должен быть в дочернем классе"""
        pass


class SaveData(SalaryOfVacancies, OperationsWithVacancies, AbstractSave):
    """Класс для работы с добавления информации о вакансиях в JSON-файл"""

    def __init__(
        self,
        keyword: str,
        keyword_2: str,
        employment: str,
        currency: str,
        pay_from: int,
        pay_to: int,
        file: str = "C:/Users/Nurlan/IT/Проекты/results4/data/hh_vacancies.json",
    ):  # noqa: E501
        """Метод-конструктор"""
        super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
        self.__file = file

    def _save_data(self) -> Any:
        """Метод для добавления вакансий в файл"""
        with open(self.__file, "r", encoding="utf-8") as file:
            try:
                data_from_json_file = json.load(file)
            except json.decoder.JSONDecodeError:
                data_from_json_file = []
            try:
                vacancies = self._comparison_pay()
                if vacancies is not None:
                    for vacancy in vacancies:
                        if vacancy not in data_from_json_file:
                            data_from_json_file.append(vacancy)

                    with open(self.__file, "w", encoding="utf-8") as f:
                        json.dump(data_from_json_file, f, ensure_ascii=False)
                    return vacancies
                else:
                    return []
            except Exception as e:
                print(e)
                print("Ошибка в классе SaveData")
                return None


class GetData(OperationsWithVacancies, AbstractGet):
    """Класс для получения информации о вакансиях в JSON-файл"""

    def __init__(
        self,
        keyword: str,
        keyword_2: str,
        employment: str,
        currency: str,
        pay_from: int,
        pay_to: int,
        file: str = "C:/Users/Nurlan/IT/Проекты/results4/data/hh_vacancies.json",
    ):  # noqa: E501
        """Метод-конструктор"""
        super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
        self.__file = file

    def _get_data(self) -> Any:
        """Метод для получения данных из файла по указанным критериям"""
        try:
            with open(self.__file, "r", encoding="utf-8") as file:
                data_from_json_file = json.load(file)
        except json.decoder.JSONDecodeError:
            return "Файл пустой"
        try:
            vacations = []
            for vacancy in data_from_json_file:
                if (
                    self._keyword_2 in vacancy.get("name")
                    and self._employment in vacancy["employment"].get("name")
                    and self._currency in vacancy["salary"].get("currency")
                    and vacancy["salary"].get("from", 0) >= self._pay_from
                    and vacancy["salary"].get("to", 0) <= self._pay_to
                ):
                    vacations.append(vacancy)
                else:
                    continue
            return vacations if vacations else "Работа не найдена"
        except Exception as e:
            print(e)
            print("Ошибка в классе GetData")


class DeleteData(OperationsWithVacancies, AbstractDelete):
    """Класс для очистки JSON-файла"""

    def __init__(
        self,
        keyword: str,
        keyword_2: str,
        employment: str,
        currency: str,
        pay_from: int,
        pay_to: int,
        file: str = "C:/Users/Nurlan/IT/Проекты/results4/data/hh_vacancies.json",
    ):
        """Метод-конструктор"""
        super().__init__(keyword, keyword_2, employment, currency, pay_from, pay_to)
        self.__file = file

    def _delete_data(self) -> str:
        """Метод для удаления информации о вакансиях"""
        with open(self.__file, "w"):
            return f"Файл {self.__file} очищен"


if __name__ == "__main__":
    data_to_file = SaveData("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(data_to_file._save_data())