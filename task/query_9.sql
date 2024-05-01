SELECT DISTINCT s.student, c.class_name
FROM students AS s
	LEFT JOIN marks AS m ON s.id = m.student_id
	LEFT JOIN classes AS c ON m.class_id = c.id
WHERE s.id = 15;