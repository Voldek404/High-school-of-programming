16. Indexes

CREATE INDEX IndexAndREgion on Region(RegionID,RegionDescription)
  
CREATE INDEX IndexAndTerritory on Territories(TerritoryID,TerritoryDescription)

DROP INDEX IndexAndTerritory on Territories

CREATE CLUSTERED INDEX IndexAndTerritory on Territories(TerritoryID,TerritoryDescription)