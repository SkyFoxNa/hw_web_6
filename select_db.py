class SelectManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # 1. Топ-5 студентів з найвищими середніми оцінками:
    def get_top_students(self, count=5):
        # Читання SQL-запиту з файлу
        with open("query_1.sql", "r") as file:
            query = file.read()

        top_students = self.db_manager.select_table(query, (count,))
        return top_students

    # 2. Найкращий учень з предмета
    def get_top_student_subject(self, subject_id) :
        # Читання SQL-запиту з файлу
        with open("query_2.sql", "r") as file :
            query = file.read()

        top_student_subject = self.db_manager.select_table(query, (subject_id,))
        return top_student_subject

    # Пошук назви предмета
    def get_subject_name_by_id(self, subject_id) :
        with open("get_subject_name_by_id.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (subject_id, ))
        if result :
            return result[0][0]
        else :
            return "Предмет не знайдено"

    # 3. Пошук середнього балу по всям группам
    def get_average_grade_by_subject(self, subject_id) :
        with open("query_3.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (subject_id, ))
        return result

    # 4. Пошук середній бал на потоці (по всій таблиці оцінок)
    def get_average_grade_all_subjects(self) :
        with open("query_4.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, ())
        return result[0][0] if result else None

    # 5. Пошук які курси читає певний викладач.
    def get_subjects_read_lecturer(self, lecturer_id):
        with open("query_5.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, ))
        return result

    # Пошук викладача
    def get_lecturers_name_by_id(self, lecturer_id) :
        with open("get_lecturers_name_by_id.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, ))
        if result :
            return result[0][0]
        else :
            return "Викладача не знайдено"

    # 6. Пошук списку студентів у певній групі.
    def get_students_by_group(self, group_id) :
        with open("query_6.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (group_id, ))
        return result

    # Пошук групи
    def get_groups_name_by_id(self, group_id) :
        with open("get_groups_name_by_id.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (group_id, ))
        if result :
            return result[0][0]
        else :
            return "Группу не знайдено"

    # 7. Пошук оцінки студентів у окремій групі з певного предмета.
    def get_grades_by_group_and_subject(self, group_id, subject_id) :
        with open("query_7.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (group_id, subject_id, ))
        return result

    # 8. Пошук середній бал, який ставить певний викладач зі своїх предметів.
    def get_average_grade_by_lecturer(self, lecturer_id):
        with open("query_8.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, ))
        return result

    # 9. Пошук список курсів, які відвідує студент.
    def get_courses_by_student(self, student_id) :
        with open("query_9.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (student_id, ))
        return result

    # Пошук студента
    def get_students_name_by_id(self, student_id) :
        with open("get_students_name_by_id.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (student_id, ))
        if result :
            return result[0][0]
        else :
            return "Студента не знайдено"

    # 10. Пошук курсів, які певному студенту читає певний викладач.
    def get_courses_by_lecturer_for_student(self, lecturer_id) :
        with open("query_10_1.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, ))
        student_id = result[0][0]

        with open("query_10_2.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, student_id, ))
        return result

    # Додатково
    # 10. Пошук курсів, які певному студенту читає певний викладач.
    def get_avg_grade_for_student(self, lecturer_id) :
        with open("query_10_1.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id,))
        student_id = result[0][0]

        with open("query_d_1.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (lecturer_id, student_id,))
        return result

    # 2. Оцінки студентів у певній групі з певного предмета на останньому занятті.
    def get_last_grades_for_subject(self, subject_id) :
        with open("query_d_2.sql", "r") as file :
            query = file.read()

        result = self.db_manager.select_table(query, (subject_id, subject_id, ))
        return result
