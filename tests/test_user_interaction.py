from src.user_interaction import filter_vacancies, get_vacancies_by_salary

def test_filter_vacancies_no_matches():
    vacancies_list = [
        {"name": "Vacancy A",
         "snippet": "Some description.",
         "salary": {"from": 100000, "to": 150000}},
        {"name": "Vacancy B",
         "snippet": "Another description.",
         "salary": {"from": 50000, "to": 70000}},
    ]
    filter_words = ["Ruby"]
    result = filter_vacancies(vacancies_list, filter_words)
    assert result == []

def test_get_vacancies_by_salary():
    filtered_vacancies = [
        {"name": "Senior Python Developer",
         "snippet": "We are looking for a senior Python developer.",
         "salary": {"from": 100000, "to": 150000}},
        {"name": "Junior Java Developer",
         "snippet": "Entry-level Java developer position.",
         "salary": {"from": 50000, "to": 70000}},
        {"name": "Python Developer",
         "snippet": "Looking for an experienced Python developer.",
         "salary": {"from": 80000, "to": 120000}},
    ]
    salary_range = "80000 - 150000"
    expected_result = [
        {"name": "Senior Python Developer",
         "snippet": "We are looking for a senior Python developer.",
         "salary": {"from": 100000, "to": 150000}},
        {"name": "Python Developer",
         "snippet": "Looking for an experienced Python developer.",
         "salary": {"from": 80000, "to": 120000}},
    ]
    result = get_vacancies_by_salary(filtered_vacancies, salary_range)
    assert result == expected_result