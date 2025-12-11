from unittest.mock import Mock, patch

import pytest

from src.api.headhunter_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_get_vacancies_success(hh_api):
    mock_head = Mock()
    mock_head.status_code = 200

    mock_get = Mock()
    mock_get.json.return_value = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/100",
                "salary": {"from": 150000, "to": 250000, "currency": "RUR"},
                "employer": {"name": "Яндекс"},
                "snippet": {"requirement": "Python"},
            }
        ]
    }
    mock_get.raise_for_status.return_value = None

    with (
        patch("requests.head", return_value=mock_head),
        patch("requests.get", return_value=mock_get),
    ):
        result = hh_api.get_vacancies("Python")
        assert len(result) == 1
        assert result[0]["name"] == "Python Developer"


def test_get_vacancies_empty(hh_api):
    mock_head = Mock(status_code=200)
    mock_get = Mock()
    mock_get.json.return_value = {"items": []}
    mock_get.raise_for_status.return_value = None

    with (
        patch("requests.head", return_value=mock_head),
        patch("requests.get", return_value=mock_get),
    ):
        result = hh_api.get_vacancies("неизвестный_запрос")
        assert result == []


def test_get_vacancies_no_connection(hh_api):
    with patch("requests.head", side_effect=Exception("Нет интернета")):
        result = hh_api.get_vacancies("Python")
        assert result == []
