SELECT s.student, l.lecturer, c.class_name
FROM students AS s
	LEFT JOIN marks AS m ON s.id = m.student_id
	LEFT JOIN classes AS c ON m.class_id = c.id
	LEFT JOIN lecturers AS l ON c.lecturer_id = l.id
WHERE s.id = 15 AND l.id = 2;
