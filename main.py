import sqlite3
import logging

from create_db import CreateGrade, CreateGroup, CreateLecturer, CreateStudent, CreateSubject
from insert_db import DataGenerator
from select_db import SelectManager
from search_request import *

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    'line_num: %(lineno)s > %(message)s'
)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class DatabaseManager :
    def __init__(self, db_name) :
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # видалення всіх баз
    def drop_tables(self) :
        self.cursor.execute("DROP TABLE IF EXISTS students")
        self.cursor.execute("DROP TABLE IF EXISTS groups")
        self.cursor.execute("DROP TABLE IF EXISTS lecturers")
        self.cursor.execute("DROP TABLE IF EXISTS subjects")
        self.cursor.execute("DROP TABLE IF EXISTS grades")
        self.conn.commit()
        logging.debug("Видалення всіх таблиць")

    # очистка всех баз
    def delete_all_db(self) :
        self.cursor.execute("DELETE FROM students")
        self.cursor.execute("DELETE FROM groups")
        self.cursor.execute("DELETE FROM lecturers")
        self.cursor.execute("DELETE FROM subjects")
        self.cursor.execute("DELETE FROM grades")
        self.conn.commit()
        logging.debug("очистка всех баз")

    def create_table(self, create_query) :
        self.cursor.execute(create_query)
        self.conn.commit()

    def insert_data(self, insert_query, data) :
        self.cursor.executemany(insert_query, data)
        self.conn.commit()

    def select_table(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self) :
        self.conn.close()


def main() :
    db_manager = DatabaseManager("institution_db.db")

    tables = [CreateGrade, CreateGroup, CreateLecturer, CreateStudent, CreateSubject]
    try :
        # видалення всіх баз
        logging.debug(f" Видалення таблиць {db_manager.drop_tables()}")
        # Створення таблиць
        for table_class in tables :
            logging.debug(
                f" Створення таблиць {table_class.__name__}: {db_manager.create_table(table_class.create_tables)}")

        # Наповнення таблиць
        generator = DataGenerator()
        students_data = generator.generate_students(50)
        groups_data = generator.generate_groups(3)
        lecturers_data = generator.generate_lecturers(5)
        subjects_data = generator.generate_subjects(8)
        grades_data = generator.generate_grades(len(students_data), len(subjects_data))

        db_manager.insert_data("INSERT INTO students (fullname, id_groups) VALUES (?, ?)", students_data)
        db_manager.insert_data("INSERT INTO groups (name) VALUES (?)", groups_data)
        db_manager.insert_data("INSERT INTO lecturers (fullname, id_groups) VALUES (?, ?)", lecturers_data)
        db_manager.insert_data("INSERT INTO subjects (name, id_lecturer) VALUES (?, ?)", subjects_data)
        db_manager.insert_data(
            "INSERT INTO grades (grade, grade_date, id_students, id_subjects) VALUES (?, ?, ?, ?)", grades_data)

        student_manager = SelectManager(db_manager)

        # 1. Топ-5 студентів з найвищими середніми оцінками
        Top5StodentHighestAverageGrades(student_manager)

        # 2. Найкращий учень з предмета
        TopStudentSubject(student_manager)

        # 3. Пошук середнього балу по всям группам
        AGGroupSubject(student_manager)

        # 4. Пошук середній бал на потоці (по всій таблиці оцінок)
        AVGSubject(student_manager)
        #
        # 5. Пошук які курси читає певний викладач.
        SubjectsReadLector(student_manager)

        # 6. Пошук списку студентів у певній групі.
        StudentsByGroup(student_manager)

        # 7. Пошук оцінки студентів у окремій групі з певного предмета.
        GradesGroupSubject(student_manager)

        # 8. Пошук середній бал, який ставить певний викладач зі своїх предметів.
        AVGGradeLecturer(student_manager)

        # 9. Пошук список курсів, які відвідує студент.
        CoursesByStudent(student_manager)

        # 10. Пошук курсів, які певному студенту читає певний викладач.
        CoursesLecturerStudent(student_manager)

        # Додатково
        # 1. Середній бал, який певний викладач ставить певному студентові.
        AvgGradeForStudent(student_manager)

        # 2. Оцінки студентів у певній групі з певного предмета на останньому занятті.
        LastGradesForSubject(student_manager)

    except sqlite3.Error as e :
        logging.error(f"Error {e}")
    finally :
        db_manager.close_connection()


if __name__ == "__main__" :
    main()
