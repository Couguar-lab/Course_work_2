import json
import os
from typing import Any, Dict, List

from ..data.vacancy import Vacancy
from .abstract_saver import VacancySaver


class JSONSaver(VacancySaver):
    """Класс для сохранения вакансий в JSON-файл"""

    def __init__(self, filename: str = "vacancies.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy: Vacancy):
        vacancies = self._load_vacancies()
        vacancy_dict = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "description": vacancy.description,
            "employer": vacancy.employer,
        }
        # Проверка на дубли
        if not any(v["url"] == vacancy.url for v in vacancies):
            vacancies.append(vacancy_dict)
            self._save_vacancies(vacancies)

    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Vacancy]:
        vacancies = self._load_vacancies()
        result = []
        for v in vacancies:
            match = True
            if "keyword" in criteria:
                keyword = criteria["keyword"].lower()
                if (
                    keyword not in v["title"].lower()
                    and keyword not in v["description"].lower()
                ):
                    match = False
            if "min_salary" in criteria:
                if (v["salary_from"] or 0) < criteria["min_salary"]:
                    match = False
            if match:
                vac = Vacancy(
                    title=v["title"],
                    url=v["url"],
                    salary_from=v["salary_from"],
                    salary_to=v["salary_to"],
                    description=v["description"],
                    employer=v["employer"],
                )
                result.append(vac)
        return result

    def delete_vacancy(self, vacancy: Vacancy):
        vacancies = self._load_vacancies()
        new_vacancies = [v for v in vacancies if v["url"] != vacancy.url]
        self._save_vacancies(new_vacancies)

    def _load_vacancies(self) -> List[Dict]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save_vacancies(self, vacancies: List[Dict]):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)
