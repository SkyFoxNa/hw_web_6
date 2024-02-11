SELECT DISTINCT subjects.name
    FROM students
    JOIN groups ON students.id_groups = groups.id
    JOIN grades ON students.id = grades.id_students
    JOIN subjects ON grades.id_subjects = subjects.id
    WHERE students.id = ?