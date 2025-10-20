-- SQL Script to create the TeckInterview database and its tables
-- Create the database
CREATE DATABASE TeckInterview;
GO USE TeckInterview;
GO CREATE TABLE Can (
        CanID INT PRIMARY KEY IDENTITY(1, 1),
        LineName NVARCHAR(100) NULL
    );
GO CREATE TABLE Product (
        ProductID INT PRIMARY KEY IDENTITY(1, 1),
        ProductName NVARCHAR(100) NOT NULL,
        ProductCode NVARCHAR(50) NULL
    );
GO CREATE TABLE Operator (
        OperatorID INT PRIMARY KEY IDENTITY(1, 1),
        OperatorName NVARCHAR(100) NOT NULL
    );
GO CREATE TABLE WeightMeasurement (
        MeasurementID INT PRIMARY KEY IDENTITY(1, 1),
        CanID INT NULL,
        ProductID INT NULL,
        OperatorID INT NULL,
        [DateTime] DATETIME NOT NULL,
        [Weight] DECIMAL(10, 3) NOT NULL,
        Shift NVARCHAR(20) NULL,
        Comments NVARCHAR(255) NULL,
        -- Foreign Key constraints
        CONSTRAINT FK_WeightMeasurement_Can FOREIGN KEY (CanID) REFERENCES Can(CanID),
        CONSTRAINT FK_WeightMeasurement_Product FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
        CONSTRAINT FK_WeightMeasurement_Operator FOREIGN KEY (OperatorID) REFERENCES Operator(OperatorID)
    );
GO