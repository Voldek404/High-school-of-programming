Task 18.
1. 

SELECT Dwarves.*, Squads.name, Squads.mission
FROM Dwarves JOIN Squads
ON Dwarves.squad_id = Squads.squad_id

2.

SELECT dwarf_id
FROM Dwarves
WHERE profession = 'miner' AND squad_id IS NULL


3.

SELECT *
FROM Tasks
WHERE status = 'pending'
ORDER BY priority DESC 
LIMIT 10

4.

SELECT COUNT(Items.item_id), Dwarwes.dwarf_id
FROM Dwarves JOIN Items
ON Dwarves.dwarf_id = Items.owner_id 
GROUP BY Dwarves.dwarf_id

5. 

SELECT COUNT(Dwarves.dwarf_id), Squads.squad_id
FROM Squads JOIN Dwarves
ON Dwarves.squad_id = Squads.squad_id
GROUP BY Squads.squad_id

6.

SELECT Dwarves.profession, COUNT(*)  as task_count
FROM Dwarves JOIN Tasks
ON Dwarves.dwarves_id = Tasks.assigned_to
WHERE Tasks.status IN ('pending','in progress')
GROUP BY Dwarves.profession
ORDER BY task_count DESC 
LIMIT 3

7.

SELECT Items.item_id, AVG(Dwarves.age) as average_age
FROM Items JOIN Dwarves
ON Items.owner_id = Dwarves.dwarf_id
GROUP BY Items.item_id

8.

SELECT Dwarves.dwarf_id, Dwarves.age
FROM Dwarves
WHERE Dwarves.age > (SELECT AVG(age) FROM Dwarves)
AND Dwarves.dwarf_id NOT IN (SELECT DISTINCT Items.owner_id FROM Items)