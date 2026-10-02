def calculate_average(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_result(average):
    if average >= 90:
        return "Отлично"
    elif average >= 75:
        return "Хорошо"
    elif average >= 50:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"


def main():
    print("=== Калькулятор среднего балла студента ===")

    grades_input = input("Введите оценки через пробел: ")
    grades = [float(x) for x in grades_input.split()]

    average = calculate_average(grades)
    result = get_result(average)

    print(f"Средний балл: {average:.2f}")
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()