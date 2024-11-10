class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'city', 'salary', 'result', 'data_base_hh')

    def __init__(self, name, city, salary,data_base_hh ):
        """Инициализатор для класса"""
        self.name = name
        self.city = city
        self.salary = salary
        self.data_base_hh = data_base_hh
        self.result = []
        self.__reform_file(self.data_base_hh)

    def __reform_file(self, data_hh):
        """Метод для обработки JSON-ответа от сайта HH.ru"""
        for i in data_hh:
            if i["salary"] is None:
                self.result.append({
                    "name": i["name"],
                    "city": i["area"]["name"],
                    "salary": {"from": 0,
                               "to": 0},
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })
            elif i["salary"]["from"] is None and i["salary"]["currency"] == 'RUR':
                self.result.append({
                    "name": i["name"],
                    "city": i["area"]["name"],
                    "salary": {"from": 0,
                               "to": i["salary"]["to"]},
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })
            elif i["salary"]["to"] is None and i["salary"]["currency"] == 'RUR':
                self.result.append({
                    "name": i["name"],
                    "city": i["area"]["name"],
                    "salary": {"from": i["salary"]["from"],
                               "to": 0},
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })

            elif i["salary"]["currency"] == 'RUR':
                self.result.append({
                    "name": i["name"],
                    "city": i["area"]["name"],
                    "salary": {"from": i["salary"]["from"],
                               "to": i["salary"]["to"]},
                    "url": i["alternate_url"],
                    "description": i["snippet"]["requirement"]
                })

    def filter_city(self):
        """Метод фильтрации списка вакансий по нужному городу"""
        result_city = []
        for i in self.result:
            if self.city == i["city"]:
                result_city.append(i)
        return result_city

    def __le__(self, other, my_list):
        """ Магический метод фильтрации списка вакансий по заработной плате"""
        res_salary = []
        for i in my_list:
            if other <= i["salary"]["from"]:
                res_salary.append(i)
        return res_salary
