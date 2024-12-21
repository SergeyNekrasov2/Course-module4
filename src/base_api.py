from abc import ABC, abstractmethod


class BaseSaveFile(ABC):
    """Абстрактный класс инициализации пути до файла, для записи"""

    @abstractmethod
    def __init__(self, file_worker):
        self.file_worker = file_worker


class BaseLoadVacancies(ABC):
    """Абстрактный класс для создания метода, получение вакансий по ключевому слову"""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass