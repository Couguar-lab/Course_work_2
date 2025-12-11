import json
from typing import Any, Dict, List

from ..data.vacancy import Vacancy
from .abstract_saver import VacancySaver


class JSONSaver(VacancySaver):
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename

    def _vacancy_to_dict(self, vacancy: Vacancy) -> Dict[str, Any]:
        return {slot: getattr(vacancy, slot) for slot in vacancy.__slots__}

    def _dict_to_vacancy(self, data: Dict[str, Any]) -> Vacancy:
        return Vacancy(
            title=data["title"],
            url=data["url"],
            salary_from=data.get("salary_from"),
            salary_to=data.get("salary_to"),
            description=data.get("description", ""),
            employer=data.get("employer", "Не указан"),
        )

    def add_vacancy(self, vacancy: Vacancy) -> None:
        data = self._load_data()
        data.append(self._vacancy_to_dict(vacancy))
        self._save_data(data)

    def get_vacancies(self, criteria: Dict[str, str] | None = None) -> List[Vacancy]:
        if criteria is None:
            criteria = {}
        data = self._load_data()
        result = [self._dict_to_vacancy(item) for item in data]

        if "keyword" in criteria:
            keyword = criteria["keyword"].lower()
            result = [
                v
                for v in result
                if keyword in f"{v.title} {v.description} {v.employer}".lower()
            ]
        return result

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        data = self._load_data()
        vac_dict = self._vacancy_to_dict(vacancy)
        data = [item for item in data if item != vac_dict]
        self._save_data(data)

    def _load_data(self) -> List[Dict[str, Any]]:
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, data: List[Dict[str, Any]]) -> None:
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
