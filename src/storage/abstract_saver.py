from abc import ABC, abstractmethod
from typing import List

from ..data.vacancy import Vacancy


class VacancySaver(ABC):
    """Абстрактный класс для работы с хранилищем вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

    # Заглушки для будущей работы с БД
    def connect(self):
        pass

    def disconnect(self):
        pass
