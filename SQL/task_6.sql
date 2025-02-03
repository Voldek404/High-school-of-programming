Task 6. Группировка и фильтрация

6.3.1
	SELECT ContactType, COUNT(*) as Count
	FROM Contacts
	WHERE ContactType IS NOT NULL
	GROUP BY ContactType

6.3.2
	SELECT CategoryID, AVG(UnitPrice) as Average_price
	FROM Products
	GROUP BY CategoryID
	ORDER BY Average_price