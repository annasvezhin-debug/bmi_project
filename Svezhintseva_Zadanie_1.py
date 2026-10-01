# Калькулятор ИМТ (индекса массы тела) с историей измерений
# Версия 2: добавлена валидация ввода, меню и сохранение истории в файл.

import os
from typing import List, Tuple


HISTORY_FILE = "bmi_history.txt"
Record = Tuple[float, float, float]  # (рост, вес, ИМТ)


def calculate_bmi(weight: float, height: float) -> float:
    """Считает ИМТ: вес / рост²."""
    if height <= 0:
        raise ValueError("Рост должен быть больше нуля.")
    if weight <= 0:
        raise ValueError("Вес должен быть больше нуля.")
    return weight / (height ** 2)


def get_category(bmi_value: float) -> str:
    """Определяет категорию по значению ИМТ."""
    if bmi_value < 18.5:
        return "Недостаток веса"
    elif bmi_value < 25:
        return "Норма"
    elif bmi_value < 30:
        return "Избыточный вес"
    return "Ожирение"


def read_float(prompt: str) -> float:
    """Безопасный ввод числа с плавающей точкой."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value <= 0:
                print("Значение должно быть больше нуля.")
                continue
            return value
        except ValueError:
            print("Некорректный ввод. Введите число, например 1.75.")


def save_history(history: List[Record]) -> None:
    """Сохраняет историю измерений в файл."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        for height, weight, bmi in history:
            f.write(f"{height};{weight};{bmi}\n")


def load_history() -> List[Record]:
    """Загружает историю измерений из файла, если он существует."""
    if not os.path.exists(HISTORY_FILE):
        return []
    history: List[Record] = []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 3:
                history.append((float(parts[0]), float(parts[1]), float(parts[2])))
    return history


def clear_history() -> None:
    """Очищает историю измерений."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("История измерений очищена.")
    else:
        print("История и так пуста.")


def print_history(history: List[Record]) -> None:
    """Печатает историю измерений."""
    print("\n=== История измерений ===")
    for i, (height, weight, bmi) in enumerate(history, start=1):
        print(f"{i}) Рост: {height} м, Вес: {weight} кг, ИМТ: {bmi}")
    print(f"\nВсего измерений: {len(history)}")


def main() -> None:
    print("Калькулятор индекса массы тела")
    name = input("Как вас зовут? ").strip()
    print(f"Здравствуйте, {name}!")

    history: List[Record] = load_history()

    while True:
        print("\nМеню:")
        print("1 - Добавить измерение")
        print("2 - Показать историю")
        print("3 - Очистить историю")
        print("0 - Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            height = read_float("Введите рост в метрах (например, 1.75): ")
            weight = read_float("Введите вес в кг: ")
            bmi = round(calculate_bmi(weight, height), 2)
            history.append((height, weight, bmi))
            save_history(history)
            print(f"Ваш ИМТ: {bmi}")
            print(f"Категория: {get_category(bmi)}")
        elif choice == "2":
            print_history(history)
        elif choice == "3":
            clear_history()
            history = []
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()