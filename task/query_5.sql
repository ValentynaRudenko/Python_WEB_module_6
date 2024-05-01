SELECT l.lecturer, c.class_name
FROM classes AS c
LEFT JOIN lecturers AS l ON c.lecturer_id = l.id
WHERE l.lecturer = 'Diane Huynh';