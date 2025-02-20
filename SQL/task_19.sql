Task 19.
1. 
SELECT *
FROM Squads
WHERE leader_id is NULL


2. П
SELECT *
FROM DWarves
WHERE profession = "Warrior" AND age > 150

3. 
SELECT Dwarves.name, Dwarves.dwarf_id
FROM Dwarves
JOIN Items
ON Dwarves.dwarf_id = Items.dwarf_id
AND type = 'weapon'

4.
SELECT Dwarves.dwarf_id, Tasks.status, COUNT(*) AS task_count
FROM Dwarves
JOIN Tasks ON Dwarves.dwarf_id = Tasks.dwarf_id
GROUP BY Dwarves.dwarf_id, Tasks.status

5. 
SELECT * FROM Tasks
WHERE assigned_to IN
(SELECT dwarf_id
FROM Dwarves
WHERE squad_id IN 
(SELECT squad_id
FROM Squads
WHERE name = 'Guardians'))
  
6. 

SELECT Dwarves.name,  Relationships.relationship
FROM Dwarves
LEFT JOIN Relationships 
ON Dwarves.dwarf_id = Relationships.dwarf_id
LEFT JOIN Dwarves  
ON Relationships.related_to = Relatives.dwarf_id;