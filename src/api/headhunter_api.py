from typing import Any, Dict, List

import requests

from .abstract_api import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API hh.ru"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(
        self, search_query: str, page: int = 0, per_page: int = 100
    ) -> List[Dict[Any, Any]]:
        params: dict[str, Any] = {
            "text": search_query,
            "page": page,
            "per_page": per_page,
            "area": 113,  # Россия
            "only_with_salary": False,
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        except requests.RequestException as e:
            print(f"Ошибка при запросе к hh.ru: {e}")
            return []
