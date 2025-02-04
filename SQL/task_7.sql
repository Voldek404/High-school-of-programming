Task 7. SQL: дополнительные возможности

7.3.1
	SELECT 'Discount:', Discount * FROM [Order Details]
	WHERE (Discount * 100) <> 0

7.3.2
	SELECT * FROM [Order Details]
	WHERE ProductID IN
	(SELECT ProductID 
	FROM Products
	WHERE UnitsInStock > 40)
7.3.3
	SELECT * FROM [Order Details]
	WHERE ProductID IN
	(SELECT ProductID
	FROM Products
	WHERE UnitsInStock > 40 and OrderID IN
	(SELECT OrderID 
	FROM Orders
	WHERE Freight <= 50))