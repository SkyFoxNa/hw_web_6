SELECT DISTINCT students.id, students.fullname, subjects.name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
JOIN students ON grades.id_students = students.id
JOIN subjects ON grades.id_subjects = subjects.id
JOIN lecturers ON subjects.id_lecturer = lecturers.id
WHERE lecturers.id = ? and students.id = ?