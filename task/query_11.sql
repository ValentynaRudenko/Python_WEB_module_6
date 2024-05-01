SELECT l.lecturer, s.student, AVG(m.mark)
FROM marks AS m
	LEFT JOIN students AS s ON m.student_id = s.id
	LEFT JOIN classes AS c ON m.class_id = c.id
	LEFT JOIN lecturers AS l ON c.lecturer_id = l.id
WHERE l.id = 2 AND s.id = 3;