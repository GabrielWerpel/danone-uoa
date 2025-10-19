-- SQL script to create tables for Can Weight Report data in MSSQL (Interview Template)

CREATE TABLE Can (
    CanID INT IDENTITY(1,1) PRIMARY KEY,
    LineName NVARCHAR(100) NULL
);
-- TODO:
-- Create the Product table
-- CREATE TABLE Product (...)

-- Create the Operator table
-- CREATE TABLE Operator (...)

-- Create the WeightMeasurement table with foreign keys to Can, Product, and Operator
-- CREATE TABLE WeightMeasurement (...)

--------------------------------------------END_of_TODO_#1-----------------------------------------