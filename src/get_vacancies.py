from abc import ABC, abstractmethod
from typing import Any, Dict

import requests


class AbstractGet(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _loading(self) -> Any:
        """Метод, который должен быть в дочернем классе"""
        pass


class GetVacancies(AbstractGet):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru"""

    def __init__(self, keyword: str):
        """Класс-конструктор, который получает ключевое слово для поиска(keyword)"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params: Dict[str, str | int] = {"text": keyword, "per_page": 100}
        self._keyword = keyword
        self._vacancies: Any = []

    def _loading(self) -> Any:
        """Метод, подключающийся к API и получающий вакансии"""
        try:
            json_data = requests.get(self.__url, params=self.__params)
            if json_data.status_code == 200:
                self._vacancies = json_data.json().get("items", [])
            return self._vacancies
        except Exception as e:
            print(e)
            print("Ошибка в классе GetVacancies")
            return []


if __name__ == "__main__":
    data = GetVacancies("python")
    result = data._loading()
    print(result)