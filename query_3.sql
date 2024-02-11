SELECT groups.name, ROUND(AVG(grades.grade), 2) as average_grade
    FROM groups
    JOIN students ON groups.id = students.id_groups
    JOIN grades ON students.id = grades.id_students
    JOIN subjects ON grades.id_subjects = subjects.id
    WHERE subjects.id = ?
    GROUP BY groups.name