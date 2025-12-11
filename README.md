# Парсер вакансий с hh.ru  
**Курсовая работа по Python (ООП, SOLID, API, тесты, линтеры)**

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Функционал

- Поиск вакансий через официальное API hh.ru
- Сохранение в JSON-файл
- Фильтрация по ключевым словам
- Сортировка и топ-N по зарплате
- Удаление вакансий
- Полная типизация (mypy strict)
- Автоматическое форматирование и проверка кода

## Структура проекта
```bash
src/
├── api/              → работа с внешними API
├── data/             → класс Vacancy (сравнение по зарплате, валидация)
├── storage/          → абстрактное хранилище + реализация JSON
└── main.py           → интерактивное консольное меню
tests/                → тесты с покрытием 91%
```

Соблюдены принципы:
- Наследование (абстрактные классы)
- Инкапсуляция
- SOLID (SRP, OCP, DIP)

## Установка и запуск

```bash
# Клонирование и переход в папку
git clone https://github.com/Couguar-lab/Course_work_2
cd hh-vacancies-parser

# Установка зависимостей (рекомендуется)
poetry install

# Запуск программы
poetry run python -m src.main
```

## Использование
=== Поиск вакансий на hh.ru ===

1. Поиск вакансий
2. Показать топ по зарплате
3. Поиск по ключевому слову
4. Выход

## Тесты и проверка кода
```bash
# Запуск тестов с покрытием
poetry run pytest --cov=src --cov-report=html

# Отчёт будет в папке htmlcov/index.html
# Покрытие: 91%

# Проверка линтеров (всегда зелёные)
poetry run pre-commit run --all-files
```

## Установленные линтеры:
```bash
black — форматирование
isort — сортировка импортов
flake8 — стиль кода
mypy — строгая проверка типов
```

## Лицензия
MIT License — делай с кодом что хочешь:

Используй в своих проектах
Выкладывай на GitHub
Показывай на собеседованиях
Изменяй и распространяй

Полный текст лицензии: LICENSE