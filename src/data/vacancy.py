from typing import Dict, List, Optional


class Vacancy:
    __slots__ = ("title", "url", "salary_from", "salary_to", "description", "employer")

    def __init__(
        self,
        title: str,
        url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        description: str,
        employer: str | None = None,
    ):
        self.title = title.strip()
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description.strip() if description else ""
        self.employer = employer.strip() if employer else "Не указан"

    @property
    def salary_avg(self) -> int:
        if self.salary_from and self.salary_to:
            return (self.salary_from + self.salary_to) // 2
        return self.salary_from or self.salary_to or 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_avg < other.salary_avg

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_avg == other.salary_avg

    def __le__(self, other: "Vacancy") -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_avg <= other.salary_avg

    def __str__(self) -> str:
        return (
            f"{self.title} | {self.employer} | {self.salary_avg or 'З/п не указана'} ₽"
        )

    @classmethod
    def cast_to_object_list(cls, vacancies_data: List[Dict]) -> List["Vacancy"]:
        vacancies = []
        for item in vacancies_data:
            salary = item.get("salary") or {}
            if salary.get("currency") != "RUR":
                continue
            vacancies.append(
                cls(
                    title=item.get("name", "Без названия"),
                    url=item.get("alternate_url", "#"),
                    salary_from=salary.get("from"),
                    salary_to=salary.get("to"),
                    description=item.get("snippet", {}).get("requirement", "") or "",
                    employer=item.get("employer", {}).get("name"),
                )
            )
        return vacancies
