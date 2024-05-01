SELECT max(m.date_of), g.group_name, c.class_name, s.student, m.mark 
FROM marks AS m
	LEFT JOIN students AS s ON m.student_id = s.id
	LEFT JOIN classes AS c ON m.class_id = c.id
	LEFT JOIN groups AS g ON s.group_id = g.id
WHERE g.id = 2 AND c.id = 3;