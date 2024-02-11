from faker import Faker
import random
from datetime import datetime, timedelta
import sqlite3


class DataGenerator :
    def __init__(self) :
        self.fake = Faker('uk_UA')

    # Таблиця студентів
    def generate_students(self, count) :
        students = [(self.fake.name(), random.randint(1, 3)) for _ in range(count)]
        return students

    #  Таблиця груп
    def generate_groups(self, count) :
        groups = [(self.fake.catch_phrase(),) for _ in range(count)]
        return groups

    # Таблиця викладачів
    def generate_lecturers(self, count) :
        lecturers = [(self.fake.name(), random.randint(1, 3)) for _ in range(count)]
        return lecturers

    #  Таблиця предметів
    def generate_subjects(self, count) :
        subjects = [(self.fake.catch_phrase(), random.randint(1, 5)) for _ in range(count)]
        return subjects

    # Таблиця оцінок
    def generate_grades(self, students_count, subjects_count) :
        grades = []
        for student_id in range(1, students_count + 1) :
            for subject_id in range(1, subjects_count + 1) :
                for _ in range(20) :  # Генеруємо 20 оцінок для кожного студента з кожного предмету
                    grade = random.randint(1, 12)  # Випадкова оцінка від 1 до 12
                    grade_date = self.fake.date_of_birth(minimum_age = 1, maximum_age = 6).strftime(
                        '%d-%m-%Y')  # Випадкова дата в межах 1-6 років
                    grades.append((grade, grade_date, student_id, subject_id))
        return grades


if __name__ == "__main__" :
    pass
