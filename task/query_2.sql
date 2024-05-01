SELECT s.id, s.student, c.class_name, AVG(m.mark)
FROM marks AS m
	LEFT JOIN students AS s ON m.student_id = s.id
	LEFT JOIN classes AS c ON m.class_id = c.id
WHERE c.class_name = 'buy'
GROUP BY s.id
ORDER BY AVG(m.mark) DESC 
LIMIT 5;