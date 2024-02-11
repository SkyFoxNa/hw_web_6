SELECT subjects.name
    FROM subjects
    JOIN lecturers ON subjects.id_lecturer = lecturers.id
    WHERE lecturers.id = ?