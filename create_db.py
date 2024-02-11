# Таблиця студентів
class CreateStudent :
    create_tables = '''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            fullname VARCHAR(150) NOT NULL,
                            id_groups INTEGER,
                                FOREIGN KEY (id_groups) REFERENCES groups(id) on delete cascade)'''


#  Таблиця груп
class CreateGroup :
    create_tables = '''CREATE TABLE IF NOT EXISTS groups (
                                id INTEGER PRIMARY KEY,
                                name VARCHAR(50) NOT NULL)'''
    #
    # id_students INTEGER,
    # FOREIGN KEY (id_students) REFERENCES students(id))'''


# Таблиця викладачів
class CreateLecturer :
    create_tables = '''CREATE TABLE IF NOT EXISTS lecturers (
                                id INTEGER PRIMARY KEY,
                                fullname VARCHAR(150) NOT NULL,
                                id_groups INTEGER,
                                FOREIGN KEY (id_groups) REFERENCES groups(id) on delete cascade)'''


#  Таблиця предметів
class CreateSubject :
    create_tables = '''CREATE TABLE IF NOT EXISTS subjects (
                                id INTEGER PRIMARY KEY,
                                name VARCHAR(170) NOT NULL,
                                id_lecturer INTEGER,
                                FOREIGN KEY (id_lecturer) REFERENCES lecturers(id) on delete cascade)'''


# Таблиця оцінок
class CreateGrade :
    create_tables = '''CREATE TABLE IF NOT EXISTS grades (
                                id INTEGER PRIMARY KEY,
                                grade INTEGER CHECK (grade >= 1 AND grade <= 12),
                                grade_date DATE NOT NULL,
                                id_students INTEGER,
                                id_subjects INTEGER,
                                FOREIGN KEY (id_students) REFERENCES students(id) on delete cascade,
                                FOREIGN KEY (id_subjects) REFERENCES subjects(id) on delete cascade)'''


if __name__ == "__main__" :
    pass
