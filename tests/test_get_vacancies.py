from typing import Any

from src.get_vacancies import GetVacancies


def test_init_get_vacancies() -> Any:
    data = GetVacancies("python")
    assert data._keyword == "python"