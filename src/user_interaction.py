from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: list, filter_words: list):
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies = []

    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() in vacancy.name.lower() or word.lower() in vacancy.snippet.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция сортирует вакансии по вилке зарплаты(от и до)"""
    filtered_salary_vacancies = []
    from_to_salary = salary_range.split()

    for vacancy in filtered_vacancies:
        if vacancy.salary["from"] >= int(from_to_salary[0]) and vacancy.salary["to"] <= int(from_to_salary[2]):
            filtered_salary_vacancies.append(vacancy)

    result = sorted(filtered_salary_vacancies, reverse=True)
    return result

def get_top_vacancies(filtered_vacancies, top_n):
    """Функция вывода топ вакансий по выбору пользователя"""
    filtered_vacancies = filtered_vacancies[: top_n]
    return filtered_vacancies


def print_vacancies(vacancies):
    """Функция вывода отфильтрованных вакансий в консоль"""
    for vacancy in vacancies:
        print(f"{vacancy}\n")


if __name__ == "__main__":
    my_list = [
        {"name": "Август",
         "snippet": "Август и февраль",
         "salary": {
             "from": 100,
             "to": 200
         }
         },
        {"name": "Сентябрь",
         "snippet": "Август и февраль",
         "salary": {
             "from": 100,
             "to": 300
         }
         },
        {"name": "Октябрь",
         "snippet": "ноябрь",
         "salary": {
             "from": 400,
             "to": 500
         }
         },
        {"name": "Ноябрь",
         "snippet": "февраль",
         "salary": {
             "from": 600,
             "to": 800
         }
         }
    ]

    # search_query = input("Введите поисковый запрос: ")
    top_ = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_rang = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(my_list, filter_word)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_rang)

    top_vacancies = get_top_vacancies(ranged_vacancies, top_)

    print_vacancies(top_vacancies)

    for top in top_vacancies:
        vac = Vacancy(top)
        json_templ = JSONSaver(file_saver="../data/filtered_vacancies.json")
        json_templ.add_vacancy(vac)