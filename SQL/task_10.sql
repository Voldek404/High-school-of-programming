Task 10. JOIN

10.4.1
  SELECT [Order Details].UnitPrice, Products.ProductName
  FROM Products JOIN [Order Details]
  ON [Order Details].ProductID = Products.ProductID 
  AND  [Order Details].UnitPrice < 20

10.4.2
  В табличке Orders всего 830 строк, результатом FULL JOINa становится выдача 832 строк
  Таким образом, в связи с тем, что FULL JOIN объединяет множества, 
  он же недостающие данные добивает NULLом, получается

10.4.3
  Декартово произведение превращено в декартово пересечение ниже, через WHERE и условие

  SELECT Employees.FirstName, Employees.LastName, Orders.Freight
  FROM Employees CROSS JOIN Orders


  SELECT Employees.FirstName, Employees.LastName, Orders.Freight
  FROM Employees CROSS JOIN Orders
  WHERE Employees.EmployeeID = Orders.EmployeeID

10.4.4
  Здесь, по сути, задача обратная заданию 10.4.3
  SELECT Products.ProductName, [Order Details].UnitPrice
  FROM Products JOIN [Order Details]
  ON Products.ProductID = [Order Details].ProductID