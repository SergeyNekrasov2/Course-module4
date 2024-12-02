from src.data_file import DeleteData, GetData, SaveData
from src.get_vacancies import GetVacancies
from src.operations_with_vacancies import OperationsWithVacancies, SalaryOfVacancies
from src.user_interaction import get_vacations_with_keyword, search, top_vacations

if __name__ == "__main__":
    data = GetVacancies("python")
    result = data._loading()
    print(result)

    sorted_vacancies_2 = OperationsWithVacancies("java", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(sorted_vacancies_2._filtered_vacancies())

    salary_vacancies = SalaryOfVacancies("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(salary_vacancies._lowest_pay())

    data_to_file = SaveData("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(data_to_file._save_data())

    data_from_file = GetData("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(data_from_file._get_data())

    del_data = DeleteData("python", "Junior", "Полная занятость", "RUR", 50_000, 100_000)
    print(del_data._delete_data())
    key_word, name, employment, currency, pay_from, pay_to = input(
        "Введите информацию через запятую: \n"
        "ЯП, которым владеете; \n"
        "ваш уровень пользования этим языком;\n"
        "форма занятости; \n"
        "валюта, в которой хотите получать зарплату;\n"
        "зарплатА ОТ; \n"
        "зарплата ДО: \n"
    ).split(", ")
    n = input("ведите кол-во вакансий: ")
    vacations = search(key_word, name, employment, currency, pay_from, pay_to)
    for vacancy in vacations:
        print(vacancy)
    print(top_vacations(key_word, n))
    print(get_vacations_with_keyword(key_word))