Task 9. Дополнительные возможности

9.3.1.
  SELECT t1.CustomerID, t2.CustomerID
  FROM Customers t1, Customers t2
  WHERE t1.Region IS NULL
    AND t2.Region IS NULL

9.3.2.
  SELECT t1.CustomerID, t1.OrderID, t3.Region
  FROM Orders t1, Customers t3
  WHERE t1.CustomerID = t3.CustomerID
    AND t3.Region = ANY 
        (SELECT Region 
         FROM Customers 
         WHERE Region IS NOT NULL)
9.3.3.
  SELECT t2.Freight, t2.OrderID, t1.UnitPrice
  FROM Orders t2, Products t1 
  WHERE t2.Freight > 
  (SELECT MAX(UnitPrice)
  From Products)