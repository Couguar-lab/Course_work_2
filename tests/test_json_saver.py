import pytest

from src.storage.json_saver import JSONSaver


@pytest.fixture
def json_saver(tmp_path):
    # временный файл для тестов
    file_path = tmp_path / "test_vacancies.json"
    return JSONSaver(filename=str(file_path))


def test_add_and_get_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    results = json_saver.get_vacancies({})
    assert len(results) == 1
    assert results[0].title == "Python Developer"
    assert results[0].url == "https://hh.ru/vacancy/123"


def test_delete_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    json_saver.delete_vacancy(sample_vacancy)
    results = json_saver.get_vacancies({})
    assert len(results) == 0


def test_filter_by_keyword(json_saver, sample_vacancies_list):
    for vac in sample_vacancies_list:
        json_saver.add_vacancy(vac)

    found = json_saver.get_vacancies({"keyword": "Django"})
    assert len(found) == 1
    assert found[0].title == "Middle Python"

    found = json_saver.get_vacancies({"keyword": "Архитектура"})
    assert len(found) == 1
    assert "Яндекс" in found[0].employer
