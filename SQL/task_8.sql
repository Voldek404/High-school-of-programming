Task 8. Соединение таблиц

8.3.1

  SELECT Products.ProductName, Categories.CategoryName
  FROM Products, Categories
  WHERE Products.ProductID = Categories.CategoryID

8.3.2

  SELECT [Order Details].UnitPrice, Products.ProductName
  FROM Products, [Order Details]
  WHERE [Order Details].ProductID = Products.ProductID 
  AND  [Order Details].UnitPrice < 20

8.3.3

  SELECT [Order Details].UnitPrice, Products.ProductName, Categories.CategoryName
  FROM Products, [Order Details], Categories
  WHERE [Order Details].ProductID = Products.ProductID 
  AND Products.CategoryID = Categories.CategoryID 
  AND  [Order Details].UnitPrice < 20