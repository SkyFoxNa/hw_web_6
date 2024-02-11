SELECT students.id, students.fullname, ROUND(AVG(grades.grade), 2) as average_grade
    FROM students
    JOIN grades ON students.id = grades.id_students
    GROUP BY students.id
    ORDER BY average_grade DESC
    LIMIT ?