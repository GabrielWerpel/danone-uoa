-- ================================================
-- Table Creation Script
-- ================================================

-- --- 1. Operator Table ---
CREATE TABLE Operator (
    OperatorID INT IDENTITY(1,1) PRIMARY KEY,
    UserName VARCHAR(50) NOT NULL UNIQUE
);

-- --- 2. Product Table ---
CREATE TABLE Product (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    SKU VARCHAR(50) NOT NULL UNIQUE,
    Formulation VARCHAR(100),
    Denomination VARCHAR(20)
);

-- --- 3. Can Table ---
CREATE TABLE Can (
    CanID INT IDENTITY(1,1) PRIMARY KEY,
    ProductionLine VARCHAR(50) NOT NULL UNIQUE
);

-- --- 4. WeightMeasurement Fact Table ---
CREATE TABLE WeightMeasurement (
    MeasurementID INT IDENTITY(1,1) PRIMARY KEY,
    CanID INT NOT NULL,
    ProductID INT NOT NULL,
    OperatorID INT NOT NULL,
    ProductionOrderNumber VARCHAR(50) NOT NULL,
    MeasurementDateTime DATETIME NOT NULL,
    AverageTareWeight FLOAT,
    CanNetWeight FLOAT,
    
    -- Unique constraint to prevent duplicates
    CONSTRAINT UQ_Weight UNIQUE (CanID, ProductID, OperatorID, ProductionOrderNumber, MeasurementDateTime),

    -- Foreign key relationships
    FOREIGN KEY (CanID) REFERENCES Can(CanID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (OperatorID) REFERENCES Operator(OperatorID)
);

-- ================================================
-- Optional: Indexes
-- ================================================
CREATE INDEX idx_Weight_Product ON WeightMeasurement(ProductID);
CREATE INDEX idx_Weight_Operator ON WeightMeasurement(OperatorID);
CREATE INDEX idx_Weight_Can ON WeightMeasurement(CanID);
CREATE INDEX idx_Weight_ProductionOrder ON WeightMeasurement(ProductionOrderNumber);
CREATE INDEX idx_Weight_DateTime ON WeightMeasurement(MeasurementDateTime);


