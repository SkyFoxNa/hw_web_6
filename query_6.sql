SELECT students.id, students.fullname
    FROM students
    JOIN groups ON students.id_groups = groups.id
    WHERE groups.id = ?