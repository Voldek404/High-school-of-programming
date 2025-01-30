Task 3. Принципы работы с БД

3.9.1
	SELECT ProductName, UnitsInStock FROM Product
3.9.2
	SELECT ProductName, UnitPrice FROM Products
        WHERE (UnitPrice < 20)
3.9.3
	SELECT * FROM Orders
	WHERE (11.7 <= Freight) AND (Freight < 98.1)
3.9.4
	SELECT * FROM Employees
        WHERE (TitleOfCourtesy <> 'Mrs.') AND (TitleOfCourtesy <> 'Ms.')
3.9.5
	SELECT * FROM Suppliers
	WHERE (Country = 'Japan')
3.9.6
	SELECT * FROM Orders
	WHERE EmployeeID in (2,4,8)
3.9.7
	SELECT * FROM [Order Details]
	WHERE (UnitPrice > 40) AND (Quantity < 10)
