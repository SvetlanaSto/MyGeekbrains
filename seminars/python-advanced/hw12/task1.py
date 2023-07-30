# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not value.replace(' ', '').isalpha():
            raise ValueError("ФИО должно содержать только буквы")
        if not value.istitle():
            raise ValueError("ФИО должно начинаться с заглавной буквы")
        obj.__dict__[self.name] = value


class Grade:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not (2 <= value <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        obj.__dict__[self.name] = value


class TestResult:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not (0 <= value <= 100):
            raise ValueError("Результат теста должен быть от 0 до 100")
        obj.__dict__[self.name] = value


class Student:
    name = Name()

    def __init__(self, name, csv_file):
        self.name = name
        self.subjects = self.load_subjects(csv_file)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects(self, csv_file):
        subjects = []
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                subjects.append(row[0])
        return subjects

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' отсутствует в программе")
        self.grades[subject].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' отсутствует в программе")
        self.test_results[subject].append(result)

    def average_score_by_subject(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет '{subject}' отсутствует в программе")
        grades = self.grades[subject]
        avg_grades = sum(grades) / len(grades) if grades else 0
        test_results = self.test_results[subject]
        avg_test_results = sum(test_results) / len(test_results) if test_results else 0

        return avg_grades, avg_test_results

    def average_score_overall(self):
        all_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0


if __name__ == '__main__':
    print("Ivanov Ivan Ivan".isalpha())
    student = Student("Иванов Пётр Сидорович", "subjects.csv")

    student.add_grade("математика", 4)
    student.add_grade("физика", 5)

    student.add_test_result("математика", 75)

    print(f"Средний балл по математике: {student.average_score_by_subject('математика')}")
    print(f"Средний балл по физике: {student.average_score_by_subject('физика')}")
    print(f"Средний балл по всем предметам: {student.average_score_overall()}")
