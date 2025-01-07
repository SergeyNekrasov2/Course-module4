class Vacancy:
    """Класс создания вакансии с параметрами"""
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__snippet", "__salary")

    def __init__(
        self,
        name: str = "Не указан",
        url: str = "Не указан",
        salary: str | None | dict = None,
        snippet: str = "Не указан"

    ):
        """Констркутор инициализации обьекта класса Vacancy (вакансия работника)"""
        self.__name = name
        self.__url = url
        self.__snippet = snippet if snippet else "Не указаны требования"
        self.__salary = salary

        dict_vacancy = {"name": self.__name, "url": self.__url, "salary": self.__salary, "snippet": self.__snippet}
        self.__list_vacancies.append(self)

    def __validate(self, salary):
        """Метод валидации зарплаты"""
        if salary is not None:
            self.__salary = salary
            if type(salary) is str:
                salary_split = salary.split(" ")
                self.__salary = {"from": int(salary_split[0]), "to": int(salary_split[2])}
        else:
            self.__salary = {"from": 0, "to": 0}
        return self.__salary

    def __ge__(self, other):
        """Метод сравнения вакансий по зарплате (верхний порог)"""
        # Проверяем, если __salary является строкой, преобразуем его в словарь
        if isinstance(self.__salary, str):
            try:
                from_salary, to_salary = map(int, self.__salary.split(" - "))
                self_salary_to = to_salary
            except ValueError:
                self_salary_to = 0  # Значение по умолчанию, если формат строки некорректен
        else:
            self_salary_to = self.__salary.get("to", 0)

        if isinstance(other.__salary, str):
            try:
                from_salary, to_salary = map(int, other.__salary.split(" - "))
                other_salary_to = to_salary
            except ValueError:
                other_salary_to = 0
        else:
            other_salary_to = other.__salary.get("to", 0)

        return self_salary_to >= other_salary_to

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancy_data in list_vacancies:
            # Валидируем зарплату
            salary = cls.__validate(vacancy_data.get("salary"))

            snippet = vacancy_data.get("snippet", "Не указан")
            # Если сниппет является словарем, извлекаем требование
            if isinstance(snippet, dict):
                snippet = snippet.get("requirement", "")

            # Создаем экземпляр вакансии
            cls(
                name=vacancy_data.get("name", "Не указан"),
                url=vacancy_data.get("url", "Не указан"),
                salary=salary,
                snippet=snippet,
            )
        return cls.__list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies.salary("from", 0) >= from_salary and vacancies.salary.get["to"] <= to_salary:
                print(vacancies)

    @classmethod
    def list_vacancies(cls):
        """Метод для получения всех вакансий"""
        formatted_vacancies = []
        for vacancy in cls.__list_vacancies:
            salary = vacancy.salary

            # Преобразуем строку в объект, если нужно
            if isinstance(salary, str):
                try:
                    from_salary, to_salary = map(int, salary.split(" - "))
                    salary = {"from": from_salary, "to": to_salary}
                except ValueError:
                    salary = {"from": 0, "to": 0}

            formatted_vacancy = vacancy.copy()
            formatted_vacancy.salary = salary
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def snippet(self):
        return self.__snippet

    def __str__(self):
        return f"Название: {self.__name}\nСсылка: {self.__url}\nЗарплата: {self.__salary}"


if __name__ == "__main__":
    rob1 = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                   snippet="Требования: опыт работы от 3 лет...")
    rob2 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "100000 - 150000",
        "Требования: опыт работы от 3 лет...")
    rob3 = Vacancy(
        "Python Developer", "<https://hh.ru/vacancy/123456>", "110000 - 160000",
        "Требования: опыт работы от 3 лет...")

    # Vacancy.validate_salary()
    # print(Vacancy.list_vacancies)

    Vacancy.filtered_salary(0, 150000)

    print(rob3.list_vacancies())
    print(rob2.salary)
    print(rob1.salary)
    print(Vacancy.__ge__(rob2, rob3))