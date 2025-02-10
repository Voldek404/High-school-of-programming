Task 12. Insert

12.3.1
  INSERT INTO Employees(LastName, FirstName)
  VALUES ('Vladimirov','Vladimir')

12.3.2
  INSERT INTO EmployeeTerritories(EmployeeID,TerritoryID)
  VALUES (11, 55113)

12.3.3
  INSERT INTO Orders(Freight, ShipCity)
  VALUES (25, 'Makao')
  При такой конфигурации запроса никаких конфликтов не было, 
  Айди автоинкрементировался, остальное забилось  NULL`ми