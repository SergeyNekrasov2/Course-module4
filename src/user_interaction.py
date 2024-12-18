from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: list, filter_words: list):
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies = []

    for vacancy in vacancies_list:
        for word in filter_words:
            name = vacancy.get("name", "")
            snippet = vacancy.get("snippet", "")

            # Ensure that name and snippet are strings
            if not isinstance(name, str):
                name = ""
            if not isinstance(snippet, str):
                snippet = ""

            if word.lower() in name.lower() or word.lower() in snippet.lower():
                filtered_vacancies.append(vacancy)
                break  # Optional: Stop checking other words if a match is found

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция сортирует вакансии по вилке зарплаты (от и до)"""
    filtered_salary_vacancies = []
    from_to_salary = salary_range.split()

    try:
        min_salary = int(from_to_salary[0])
        max_salary = int(from_to_salary[2])
    except (IndexError, ValueError):
        print("Некорректный ввод диапазона зарплат. Пример: '100000 - 150000'")
        return []

    for vacancy in filtered_vacancies:
        salary = vacancy.get("salary", {})
        salary_from = salary.get("from")
        salary_to = salary.get("to")

        # Check if salary_from and salary_to are not None
        if salary_from is not None and salary_to is not None:
            try:
                salary_from = int(salary_from)
                salary_to = int(salary_to)
            except ValueError:
                continue  # Skip if salary values are not numeric

            if salary_from >= min_salary and salary_to <= max_salary:
                filtered_salary_vacancies.append(vacancy)
        else:
            # Handle vacancies with missing salary information if necessary
            continue  # Or you can include logic to handle these cases

    # Sort vacancies by 'to' salary in descending order
    return sorted(
        filtered_salary_vacancies,
        key=lambda x: x["salary"].get("to", 0),
        reverse=True
    )


def get_top_vacancies(filtered_vacancies, top_n):
    """Функция вывода топ вакансий по выбору пользователя"""
    filtered_vacancies = filtered_vacancies[0: top_n]
    return filtered_vacancies


def print_vacancies(vacancies):
    """Функция вывода отфильтрованных вакансий в консоль"""
    return print(vacancies)


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

    filtered_vacanciess = filter_vacancies(my_list, filter_word)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacanciess, salary_rang)

    top_vacancies = get_top_vacancies(ranged_vacancies, top_)

    print_vacancies(top_vacancies)

    for top in top_vacancies:
        vac = Vacancy(top)
        json_templ = JSONSaver(file_saver="../data/filtered_vacancies.json")
        json_templ.add_vacancy(vac)