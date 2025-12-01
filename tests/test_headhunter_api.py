import pytest
import requests_mock

from src.api.headhunter_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_get_vacancies_success(hh_api):
    mock_response = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/100",
                "salary": {"from": 150000, "to": 250000, "currency": "RUR"},
                "employer": {"name": "Яндекс"},
                "snippet": {"requirement": "Python, asyncio"},
            }
        ]
    }

    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json=mock_response, status_code=200)
        result = hh_api.get_vacancies("Python")
        assert len(result) == 1
        assert result[0]["name"] == "Python Developer"


def test_get_vacancies_empty(hh_api):
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json={"items": []}, status_code=200)
        result = hh_api.get_vacancies("неизвестный_запрос_12345")
        assert result == []
