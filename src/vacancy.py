class Vacancy:
    """Класс создания вакансии с параметрами"""
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__snippet", "__salary")

    def __init__(
        self,
        name,
        url,
        salary: None | dict,
        snippet

    ):
        """Констркутор инициализации обьекта класса Vacancy (вакансия работника)"""
        self.__name = name
        self.__url = url
        self.__snippet = snippet
        self.__salary = salary
        self.__validate()
        self.__list_vacancies.append(self)

    def __validate(self):
        """Метод валидации зарплаты"""
        if not self.__snippet:
            self.__snippet = "Не указано"

        if not self.__salary:
            self.__salary = {"from": 0, "to": 0}
        else:
            if not self.__salary["from"]:
                self.__salary["from"] = 0
            if not self.__salary["to"]:
                self.__salary["to"] = 0


    def __lt__(self, other):
        return self.__salary["from"] < other.salary ["from"]

    def __str__(self):
        return (f"****************************\n"
               f"Название: {self.__name}\n"
               f"Зарплата: от {self.__salary["from"]} до {self.__salary["to"] if self.__salary["to"] else "не указана"}\n")

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancy_info in list_vacancies:
            cls(
                name=vacancy_info["name"],
                url=vacancy_info["alternate_url"],
                salary=vacancy_info["salary"],
                snippet=vacancy_info.get("snippet", {}).get("requirement")
            )
        return cls.__list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies.salary("from", 0) >= from_salary and vacancies.salary.get["to"] <= to_salary:
                print(vacancies)


    @classmethod
    def clear_list(cls):
        cls.__list_vacancies.clear()

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
