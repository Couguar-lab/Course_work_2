from typing import Any, Dict, List

import requests


class HeadHunterAPI:
    __BASE_URL = "https://api.hh.ru/vacancies"  # приватный
    __TIMEOUT = 10

    def __connect(self) -> bool:
        """Приватный метод проверки доступности API"""
        try:
            response = requests.head("https://api.hh.ru", timeout=self.__TIMEOUT)
            return response.status_code == 200
        except Exception:
            return False

    def get_vacancies(
        self, search_query: str, page: int = 0, per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """Получение вакансий с проверкой подключения"""
        if not self.__connect():
            print("Ошибка: нет доступа к API hh.ru")
            return []

        params = {
            "text": search_query,
            "page": page,
            "per_page": per_page,
            "area": 113,
            "only_with_salary": False,
        }

        try:
            response = requests.get(
                self.__BASE_URL,
                params=params,  # type: ignore[arg-type]
                timeout=self.__TIMEOUT,
            )
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return []
