SELECT l.lecturer, c.class_name, AVG(m.mark)
FROM lecturers AS l
	LEFT JOIN classes AS c ON l.id = c.lecturer_id
	LEFT JOIN marks AS m ON c.id = m.class_id
WHERE l.id = 5;