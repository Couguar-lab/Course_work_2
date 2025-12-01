import pytest

from src.data.vacancy import Vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary_from=150000,
        salary_to=250000,
        description="Python, Django, FastAPI",
        employer="ООО Ромашка",
    )


@pytest.fixture
def sample_vacancies_list():
    return [
        Vacancy(
            "Junior Python",
            "https://hh.ru/vacancy/1",
            70000,
            90000,
            "Junior",
            "Компания А",
        ),
        Vacancy(
            "Middle Python",
            "https://hh.ru/vacancy/2",
            120000,
            180000,
            "Django",
            "Компания Б",
        ),
        Vacancy(
            "Senior Python",
            "https://hh.ru/vacancy/3",
            250000,
            None,
            "Архитектура",
            "Яндекс",
        ),
        Vacancy(
            "Без зарплаты",
            "https://hh.ru/vacancy/4",
            None,
            None,
            "Удалённо",
            "ООО Тест",
        ),
    ]
