SELECT students.fullname, grades.grade
    FROM students
    JOIN grades ON students.id = grades.id_students
    JOIN groups ON students.id_groups = groups.id
    WHERE groups.id = ? AND grades.id_subjects = ?
    ORDER BY students.fullname, grades.grade