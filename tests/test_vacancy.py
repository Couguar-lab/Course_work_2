from src.data.vacancy import Vacancy


def test_vacancy_salary_average():
    v1 = Vacancy("Dev", "url", 100000, 150000, "desc")
    v2 = Vacancy("Dev", "url", 120000, None, "desc")
    v3 = Vacancy("Dev", "url", None, None, "desc")

    assert v1.salary_avg == 125000
    assert v2.salary_avg == 120000
    assert v3.salary_avg == 0


def test_vacancy_comparison():
    v1 = Vacancy("A", "url1", 100000, 120000, "desc")
    v2 = Vacancy("B", "url2", 150000, 200000, "desc")
    v3 = Vacancy("C", "url3", 150000, 200000, "desc")

    assert v1 < v2
    assert v2 == v3
    assert v1 <= v3
    assert sorted([v2, v1, v3]) == [v1, v2, v3]


def test_cast_to_object_list():
    raw_data = [
        {
            "name": "Python Разработчик",
            "alternate_url": "https://hh.ru/vacancy/999",
            "salary": {"from": 180000, "to": 300000, "currency": "RUR"},
            "employer": {"name": "Сбер"},
            "snippet": {"requirement": "Python, Docker, SQL"},
        },
        {
            "name": "DevOps",
            "alternate_url": "https://hh.ru/vacancy/888",
            "salary": {
                "from": 1000,
                "to": 2000,
                "currency": "USD",
            },  # не рубли → пропустится
            "employer": {"name": "Тинькофф"},
            "snippet": {"requirement": "Kubernetes"},
        },
    ]

    vacancies = Vacancy.cast_to_object_list(raw_data)
    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Разработчик"
    assert vacancies[0].salary_avg == 240000
