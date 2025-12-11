from abc import ABC, abstractmethod
from typing import Any, Dict, List


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API вакансий"""

    @abstractmethod
    def get_vacancies(
        self, search_query: str, page: int = 0, per_page: int = 100
    ) -> List[Dict[Any, Any]]:
        """Получить вакансии по запросу"""
        pass
