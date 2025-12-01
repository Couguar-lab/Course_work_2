from typing import Dict, List, Optional


class Vacancy:
    """Класс для представления вакансии"""

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        description: str,
        employer: str | None = None,
    ):
        self.title = title
        self.url = url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.description = description or ""
        self.employer = employer or "Не указан"

        # Валидация и нормализация зарплаты
        self._validate_salary()

    def _validate_salary(self):
        """Валидация зарплаты: если не указана — ставим 0"""
        if self.salary_from is None or self.salary_from < 0:
            self.salary_from = 0
        if self.salary_to is None or self.salary_to < 0:
            self.salary_to = 0

    @property
    def salary_avg(self) -> float:
        """Средняя зарплата для сравнения"""
        if self.salary_from == 0 and self.salary_to == 0:
            return 0
        elif self.salary_from > 0 and self.salary_to > 0:
            return (self.salary_from + self.salary_to) / 2
        elif self.salary_from > 0:
            return self.salary_from
        else:
            return self.salary_to

    def __str__(self):
        salary = (
            f"{self.salary_from} - {self.salary_to} руб."
            if self.salary_from or self.salary_to
            else "Не указана"
        )
        return f"{self.title} | {self.employer} | {salary} | {self.url}"

    def __repr__(self):
        return f"Vacancy('{self.title}', '{self.url}', {self.salary_from}, {self.salary_to})"

    # Методы сравнения по средней зарплате
    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return False
        return self.salary_avg == other.salary_avg

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_avg < other.salary_avg

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    @classmethod
    def cast_to_object_list(cls, vacancies_data: List[Dict]) -> List["Vacancy"]:
        """Преобразование списка вакансий из API в объекты Vacancy"""
        result = []
        for item in vacancies_data:
            salary = item.get("salary") or {}
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            if salary.get("currency") != "RUR":
                continue  # только рубли

            vacancy = cls(
                title=item.get("name", "Без названия"),
                url=item.get("alternate_url", "#"),
                salary_from=salary_from,
                salary_to=salary_to,
                description=item.get("snippet", {}).get("requirement", "Нет описания"),
                employer=item.get("employer", {}).get("name", "Не указан"),
            )
            result.append(vacancy)
        return result
