SELECT g.group_name, s.student 
FROM students AS s
LEFT JOIN groups AS g ON s.group_id = g.id
WHERE g.id = 2;