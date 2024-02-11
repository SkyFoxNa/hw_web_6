SELECT students.id, students.fullname, subjects.name, grades.grade, grade_date
FROM students
JOIN grades ON students.id = grades.id_students
JOIN subjects ON grades.id_subjects = subjects.id
JOIN (
    SELECT id_students, MAX(grade_date) AS max_date
    FROM grades
    WHERE id_subjects = ?
    GROUP BY id_students
) AS last_dates ON grades.id_students = last_dates.id_students AND grades.grade_date = last_dates.max_date
WHERE subjects.id = ?
