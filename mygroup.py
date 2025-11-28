
def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(35), "Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(15),
              str(student["exams"]).ljust(35),
              str(student["marks"]).ljust(20))


def filter_by_average(students, min_avg):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= min_avg:
            result.append(student)
    return result


groupmates = [
    {"name": "Татьяна", "surname": "Подъяпольская",
     "exams": ["Информатика", "ЭЭиС", "Web"], "marks": [4, 3, 5]},
    {"name": "Савелий", "surname": "Булгаров",
     "exams": ["История", "АиГ", "Front"], "marks": [4, 4, 4]},
    {"name": "Анна", "surname": "Тарасова",
     "exams": ["Философия", "ИС", "КТП"], "marks": [5, 5, 5]},
    {"name": "Алексей", "surname": "Кутловский",
     "exams": ["Математика", "ГиА", "Back"], "marks": [3, 5, 3]},
    {"name": "Илья", "surname": "Левченко",
     "exams": ["Физика", "АиГ", "КТП"], "marks": [5, 4, 3]}
]

# --- Основной цикл программы ---
while True:
    min_avg = float(input("Введите минимальный средний балл (0 — выход): "))

    if min_avg == 0:
        print("Программа завершена.")
        break

    filtered = filter_by_average(groupmates, min_avg)

    print("\nСтуденты с средним баллом выше", min_avg, ":\n")
    print_students(filtered)
    print("-" * 70)
