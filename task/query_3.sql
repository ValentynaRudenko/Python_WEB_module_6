SELECT g.group_name, c.class_name, AVG(m.mark)
FROM marks AS m
	LEFT JOIN students AS s ON m.student_id = s.id
	LEFT JOIN groups AS g ON s.group_id = g.id
	LEFT JOIN classes AS c ON m.class_id = c.id
WHERE c.class_name = 'buy'
GROUP BY g.id
ORDER BY AVG(m.mark) DESC;