import random


# Топ 5 студентів з найвищими середніми оцінками
class Top5StodentHighestAverageGrades:
    def __init__(self, student_manager):
        top_students = student_manager.get_top_students()
        print("Топ-5 студентів з найвищими середніми оцінками:")
        for student in top_students :
            print(f"ID: {student[0]}, Студент: {student[1]}, Средня оцінка: {student[2]}")


# Найкращий учень з предмета
class TopStudentSubject:
    def __init__(self, student_manager):
        subject_id = random.randint(1, 8)  # генеруємо випадковий предмет
        subject_name = student_manager.get_subject_name_by_id(subject_id)
        top_student_subject = student_manager.get_top_student_subject(subject_id)
        if top_student_subject :
            print(f"Найкращий учень з предмета: {subject_name}:")
            print(
                f"ID: {top_student_subject[0][0]}, Студент: {top_student_subject[0][1]}, "
                f"Средня оцінка: {top_student_subject[0][2]}")
        else :
            print(f"Не знайдено жодного студента з предмета: {subject_name} {subject_id}")


# Пошук середнього балу по всям группам
class AGGroupSubject:
    def __init__(self, student_manager):
        subject_id = random.randint(1, 8)  # генеруємо випадковий предмет
        subject_name = student_manager.get_subject_name_by_id(subject_id)

        average_grades_by_group = student_manager.get_average_grade_by_subject(subject_id)
        print(f"Середні бали по групах з предмета: {subject_name}")
        for group_grade in average_grades_by_group :
            print(f"Група: {group_grade[0]}, Средня оцінка: {group_grade[1]}")


# Пошук середній бал на потоці (по всій таблиці оцінок)
class AVGSubject:
    def __init__(self, student_manager):
        average_grade_all_subjects = student_manager.get_average_grade_all_subjects()
        if average_grade_all_subjects is not None :
            print(f"Середній бал з усіх предметів: {average_grade_all_subjects}")
        else :
            print("У базі даних не знайдено оцінок!")


# Пошук які курси читає певний викладач.
class SubjectsReadLector:
    def __init__(self, student_manager):
        lecturer_id = random.randint(1, 5)  # генеруємо випадкового викладача
        lector_name = student_manager.get_lecturers_name_by_id(lecturer_id)

        courses_by_lecturer = student_manager.get_subjects_read_lecturer(lecturer_id)
        if courses_by_lecturer :
            print(f"Курси читає викладач: {lector_name}")
            for course in courses_by_lecturer :
                print(f"Курс: {course[0]}")
        else :
            print(f"Не знайдено курсів для викладача: {lector_name}")


# Пошук списку студентів у певній групі.
class StudentsByGroup:
    def __init__(self, student_manager):
        group_id = random.randint(1, 3)  # Генеруємо випадкову групу
        groups_name = student_manager.get_groups_name_by_id(group_id) # Пошук групи

        students_by_group = student_manager.get_students_by_group(group_id)
        if students_by_group :
            print(f"Студенти в групі: {groups_name}")
            for student in students_by_group :
                print(f"ID: {student[0]}, Повне ім'я: {student[1]}")
        else :
            print(f"Не знайдено студентів у групі: {groups_name}")


# Пошук оцінки студентів у окремій групі з певного предмета.
class GradesGroupSubject:
    def __init__(self, student_manager):
        group_id = random.randint(1, 3)  # Генеруємо випадкову групу
        groups_name = student_manager.get_groups_name_by_id(group_id) # Пошук групи

        subject_id = random.randint(1, 8)  # генеруємо випадковий предмет
        subject_name = student_manager.get_subject_name_by_id(subject_id)

        grades_by_group_and_subject = student_manager.get_grades_by_group_and_subject(group_id, subject_id)
        if grades_by_group_and_subject:
            print(f"Оцінки за групу: {groups_name}, та предмет: {subject_name}.")
            for grade in grades_by_group_and_subject :
                print(f"Студент: {grade[0]}, Оцінка: {grade[1]}")
        else :
            print(f"Не знайдено оцінок для групи: {group_id}, та предмета: {subject_id}")


# Пошук середній бал, який ставить певний викладач зі своїх предметів.
class AVGGradeLecturer:
    def __init__(self, student_manager):
        lecturer_id = random.randint(1, 5)  # генеруємо випадкового викладача
        lector_name = student_manager.get_lecturers_name_by_id(lecturer_id)

        average_grade_by_lecturer = student_manager.get_average_grade_by_lecturer(lecturer_id)
        if average_grade_by_lecturer :
            print(f"Середні бали по викладачу: {lector_name}.")
            for subject in average_grade_by_lecturer :
                print(f"Предмет: {subject[0]}, Середня оцінка: {subject[1]}")
        else :
            print(f"Не знайдено оцінок для викладача: {lector_name}.")


# Пошук список курсів, які відвідує студент.
class CoursesByStudent:
    def __init__(self, student_manager):
        student_id = random.randint(1, 50)  # генеруємо випадкового студента
        lector_name = student_manager.get_students_name_by_id(student_id)

        courses_by_student = student_manager.get_courses_by_student(student_id)
        if courses_by_student :
            print(f"Предмети, відвідані студентом: {lector_name}.")
            for course in courses_by_student :
                print(f" Предмет: {course[0]}")
        else :
            print(f"Не знайдено предмета для студента with ID {student_id}")


# Пошук курсів, які певному студенту читає певний викладач.
class CoursesLecturerStudent:
    def __init__(self, student_manager):
        lecturer_id = random.randint(1, 5)  # генеруємо випадкового викладача
        lector_name = student_manager.get_lecturers_name_by_id(lecturer_id)

        courses_by_lecturer_for_student = student_manager.get_courses_by_lecturer_for_student(lecturer_id)
        if courses_by_lecturer_for_student :
            print(f"Предмети відвідав студент: {courses_by_lecturer_for_student[0][1]}, викладача: {lector_name}.")
            for course in courses_by_lecturer_for_student :
                print(f"Предмет: {course[2]}")
        else :
            print(f"Не знайдено курсів для студентів викладача: {lector_name}.")


# Додатково
# 1. Середній бал, який певний викладач ставить певному студентові.
class AvgGradeForStudent:
    def __init__(self, student_manager):
        lecturer_id = random.randint(1, 5)  # генеруємо випадкового викладача
        lector_name = student_manager.get_lecturers_name_by_id(lecturer_id)

        courses_by_lecturer_for_student = student_manager.get_avg_grade_for_student(lecturer_id)
        if courses_by_lecturer_for_student :
            print(f"Середня оцінка студента: {courses_by_lecturer_for_student[0][1]}, викладача: {lector_name}.")
            print(f"Середня оцінка: {courses_by_lecturer_for_student[0][3]}")
        else :
            print(f"Не знайдено курсів для студентів викладача: {lector_name}.")


# 2. Оцінки студентів у певній групі з певного предмета на останньому занятті.
class LastGradesForSubject:
    def __init__(self, student_manager):
        subject_id = random.randint(1, 8)  # генеруємо випадковий предмет
        subject_name = student_manager.get_subject_name_by_id(subject_id)

        last_grades_for_subject = student_manager.get_last_grades_for_subject(subject_id)
        pattern = r"|{:^70}|"
        print(pattern.format(f"Останні оцінки з предмета: {subject_name}."))
        # pattern = r"|{:^8}|{:^40}|{:^16}|{:^16}|"
        for grade in last_grades_for_subject:
            print(pattern.format(f"ID: {grade[0]}, Студент: {grade[1]}, Оцінка: {grade[3]}, Дата: {grade[4]}"))
