-- SQL script to create tables for Can Weight Report data in MSSQL (Interview Template)

CREATE TABLE Can (
    CanID INT IDENTITY(1,1) PRIMARY KEY,
    LineName NVARCHAR(100) NULL
);

CREATE TABLE Product (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    ProductCode NVARCHAR(50) NULL
);

CREATE TABLE Operator (
    OperatorID INT IDENTITY(1,1) PRIMARY KEY,
    OperatorName NVARCHAR(100) NOT NULL
);

CREATE TABLE WeightMeasurement (
    MeasurementID INT IDENTITY(1,1) PRIMARY KEY,
    CanID INT NOT NULL FOREIGN KEY REFERENCES Can(CanID),
    ProductID INT NOT NULL FOREIGN KEY REFERENCES Product(ProductID),
    OperatorID INT NOT NULL FOREIGN KEY REFERENCES Operator(OperatorID),
    DateTime DATETIME NOT NULL,
    Weight DECIMAL(10,3) NOT NULL,
    Shift NVARCHAR(20) NULL,
    Comments NVARCHAR(255) NULL
);

-- TODO:
-- Create the Product table
-- CREATE TABLE Product (...)

-- Create the Operator table
-- CREATE TABLE Operator (...)

-- Create the WeightMeasurement table with foreign keys to Can, Product, and Operator
-- CREATE TABLE WeightMeasurement (...)

--------------------------------------------END_of_TODO_#1-----------------------------------------