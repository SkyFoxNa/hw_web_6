SELECT students.id
    FROM students
    JOIN groups ON students.id_groups = groups.id
    JOIN lecturers ON groups.id = lecturers.id_groups
    WHERE lecturers.id = ?
    ORDER BY RANDOM() LIMIT 1