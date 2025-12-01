from .api.headhunter_api import HeadHunterAPI
from .data.vacancy import Vacancy
from .storage.json_saver import JSONSaver


def user_interaction():
    hh_api = HeadHunterAPI()
    saver = JSONSaver()

    print("=== Поиск вакансий на hh.ru ===")

    while True:
        print("\n1. Поиск вакансий")
        print("2. Показать топ по зарплате")
        print("3. Поиск по ключевому слову")
        print("4. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            query = input("Введите запрос (например, Python разработчик): ")
            print("Ищем вакансии...")
            raw_vacancies = hh_api.get_vacancies(query)
            vacancies = Vacancy.cast_to_object_list(raw_vacancies)

            for vac in vacancies[:20]:  # сохраняем первые 20
                saver.add_vacancy(vac)

            print(f"Найдено и сохранено {len(vacancies)} вакансий")

        elif choice == "2":
            n = int(input("Сколько топ вакансий показать? "))
            all_vac = saver.get_vacancies({})
            top_vac = sorted(all_vac, reverse=True)[:n]
            print(f"\nТоп {n} вакансий по зарплате:")
            for i, v in enumerate(top_vac, 1):
                print(f"{i}. {v}")

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            found = saver.get_vacancies({"keyword": keyword})
            print(f"\nНайдено {len(found)} вакансий с упоминанием '{keyword}':")
            for v in found[:10]:
                print(f"• {v}")

        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    user_interaction()
