SELECT DISTINCT students.id, students.fullname, subjects.name
    FROM subjects
    JOIN lecturers ON subjects.id_lecturer = lecturers.id
    JOIN grades ON subjects.id = grades.id_subjects
    JOIN students ON grades.id_students = students.id
    WHERE lecturers.id = ? and students.id = ?