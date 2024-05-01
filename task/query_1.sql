SELECT s.id, s.student, AVG(m.mark)
FROM marks AS m
LEFT JOIN students AS s ON m.student_id = s.id
GROUP BY s.id
ORDER BY AVG(m.mark) DESC 
LIMIT 5;