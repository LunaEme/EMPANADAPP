USE EmpanadaFranchise

CREATE TABLE PaymentMethods (
PaymentId INT PRIMARY KEY IDENTITY(1,1),
PaymentDescription varchar(100),
Enabled BIT,
DateAdded DATETIME,
)


CREATE TABLE UsersRoles (
RoleId INT PRIMARY KEY IDENTITY(1,1),
RoleName varchar(25)
)


CREATE TABLE Users (
UserId INT PRIMARY KEY IDENTITY(1,1),
Username VARCHAR(30),
UserRoleId INT,
Enabled BIT,
LastLogin datetime
FOREIGN KEY (UserRoleId) REFERENCES UsersRoles (RoleId)
)


CREATE TABLE Products (
ProductId INT PRIMARY KEY IDENTITY(1,1),
ProductName varchar(50),
ProductPrice FLOAT
)


CREATE TABLE Stock (
ProductId INT PRIMARY KEY IDENTITY(1,1),
Quantity INT
FOREIGN KEY (ProductId) REFERENCES Products (ProductId)
)

CREATE TABLE StockHistory (
HistoryId INT PRIMARY KEY IDENTITY(1,1),
ProductId INT,
Quantity INT,
Operation VARCHAR(1),
UserId INT,
Date DATETIME
FOREIGN KEY (ProductId) REFERENCES Products (ProductId),
FOREIGN KEY (UserId) REFERENCES Users (UserId)
)


CREATE TABLE Reports (
ReportId INT PRIMARY KEY IDENTITY(1,1),
ReportName varchar(100),
StoredProcedure varchar(255)
)


CREATE TABLE Sales (
SaleId INT PRIMARY KEY IDENTITY(1,1),
TotalPrice FLOAT,
PaymentMethodId INT,
Date DATETIME,
UserId INT,
FOREIGN KEY (UserId) REFERENCES Users (UserId)
)


CREATE TABLE SalesDetails (
SaleId INT,
SaleDetailId INT PRIMARY KEY IDENTITY(1,1),
ProductId INT,
IndividualPrice FLOAT,
Amount INT,
FOREIGN KEY (SaleId) REFERENCES Sales (SaleId),
FOREIGN KEY (ProductId) REFERENCES Products (ProductId)
)