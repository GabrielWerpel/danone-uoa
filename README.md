# Danone UoA Data Engineering Workshop

A comprehensive ETL (Extract, Transform, Load) data engineering test and workshop designed to assess skills in database design, data processing, and Python development. This project simulates a real-world scenario of processing can weight measurement data from a production line into a normalized database schema.

## 📋 Project Overview

This workshop provides a hands-on experience with:
- **Database Design**: Creating normalized tables with proper relationships
- **ETL Development**: Building data pipelines using Python and pandas
- **Data Security**: Implementing secure database connections with environment variables
- **Data Transformation**: Converting timezone data and handling CSV processing
- **SQL Server Integration**: Working with Microsoft SQL Server using pyodbc

## 🏗️ Architecture

The project implements a normalized database schema for manufacturing data:

### Database Schema
- **Can**: Stores production line information
- **Product**: Contains product details and codes
- **Operator**: Manages operator information
- **WeightMeasurement**: Central fact table storing weight measurements with foreign key relationships

### Data Flow
```
CSV Data → Python ETL Script → SQL Server Database
```

## 📊 Sample Data

The workshop includes real-world production data (`DATA_101549999 Can Weight Report.csv`) containing:
- Date/time measurements in NZDT timezone
- Operator information (USER)
- Production order numbers and SKUs
- Product formulations
- Weight measurements (tare weight, net weight)
- Denomination units

## 🛠️ Technical Components

### 1. Database Setup (`TODO_erd_schema_test_template.sql`)
- SQL template for creating normalized tables
- Primary and foreign key relationships
- Proper data types and constraints

### 2. ETL Pipeline (`TODO_etl_test_template.py`)
- Secure database connection using environment variables
- CSV data processing with pandas
- Data insertion into SQL Server
- Optional timezone conversion (NZDT to UTC)

### 3. Documentation
- Complete ERD schema specification
- Step-by-step implementation guide
- Security best practices

## 🎯 Learning Objectives

Participants will demonstrate proficiency in:
- Creating relational database schemas
- Implementing secure database connections
- Processing CSV data with pandas
- Managing environment variables and configuration
- Handling timezone conversions
- Building robust ETL pipelines

## 🚀 Getting Started

1. Review the ERD schema in `UoA - Workshop/src/ERD_schema.txt`
2. Complete the SQL table creation in `TODO_erd_schema_test_template.sql`
3. Implement the ETL pipeline in `TODO_etl_test_template.py`
4. Process the sample data file and validate results

## 📁 Project Structure

```
UoA - Workshop/
├── src/
│   ├── DATA_101549999 Can Weight Report.csv    # Sample production data
│   ├── ERD_schema.txt                          # Database schema specification
│   ├── README.md                               # Detailed instructions
│   ├── TODO_erd_schema_test_template.sql       # SQL implementation template
│   └── TODO_etl_test_template.py               # Python ETL template
```

This workshop provides practical experience with modern data engineering practices while working with realistic manufacturing data scenarios.
This repository is focused on the partnership with the University of Auckland.
