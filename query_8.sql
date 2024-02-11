SELECT subjects.name, ROUND(AVG(grades.grade), 2) as average_grade
    FROM subjects
    JOIN lecturers ON subjects.id_lecturer = lecturers.id
    JOIN grades ON subjects.id = grades.id_subjects
    WHERE lecturers.id = ?
    GROUP BY subjects.name