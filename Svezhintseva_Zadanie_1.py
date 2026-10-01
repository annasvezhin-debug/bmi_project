# Калькулятор ИМТ (индекса массы тела) с историей измерений


def calculate_bmi(weight, height):
    """Считает ИМТ: вес / рост²"""
    return weight / (height ** 2)


def get_category(bmi_value):
    """Определяет категорию по значению ИМТ"""
    if bmi_value < 18.5:
        return "Недостаток веса"
    elif bmi_value < 25:
        return "Норма"
    elif bmi_value < 30:
        return "Избыточный вес"
    return "Ожирение"


def main():
    print("Калькулятор индекса массы тела")
    name = input("Как вас зовут? ")
    print("Здравствуйте, " + name + "!")

    history = []  # история измерений
    count = int(input("Сколько измерений вы хотите сделать? "))

    if count <= 0:
        print("Количество измерений должно быть больше нуля.")
        return

    for i in range(count):
        print(f"\n--- Измерение {i + 1} ---")
        user_height = float(input("Введите рост в метрах (например, 1.75): "))
        user_weight = float(input("Введите вес в кг: "))

        user_bmi = calculate_bmi(user_weight, user_height)  # своя функция
        history.append((user_height, user_weight, round(user_bmi, 2)))

        print("Ваш ИМТ: " + str(round(user_bmi, 2)))
        print("Категория: " + get_category(user_bmi))

    # Вывод всей истории
    print("\n=== История измерений ===")
    for i, record in enumerate(history, start=1):
        print(f"{i}) Рост: {record[0]} м, Вес: {record[1]} кг, ИМТ: {record[2]}")

    print("\nВсего измерений: " + str(len(history)))


if __name__ == "__main__":
    main()