15.7 Работы с базами данных

1. Создаем новую базу
CREATE DATABASE Mytest

2. Устанавливаем использование по дефолту
USE MyTest

3. Создаем табличку "Регион" с указанием PrimaryKey
CREATE TABLE Region(
RegionID INT PRIMARY KEY, 
RegionDescription nchar(50))

4.  Создаем табличку "Territories" с указанием PrimaryKey и 
связью через свой ForeignKey c таблицей "Region" 
CREATE TABLE Territories(
TerritoryID int PRIMARY KEY, 
TerritoryDescription nchar(50) NOT NULL, 
FOREIGN KEY (RegionID) REFERENCES Region(RegionID))

5. Добавляем новые записи
INSERT INTO Region(RegionID, RegionDescription)
VALUES (1, 'Ural'),
       (2, 'Siberia'),
       (3, 'Far East')

6. Добавляем новые записи
INSERT INTO Territories(TerritoryID,TerritoryDescription, RegionID)
VALUES (123, 'Tumen',1),
       (234, 'Omsk',2),
       (356, 'Port',3)