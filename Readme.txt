Hi Gabriel, 

Thanks for the talk today, it was very insightful and inspiring. I was particularly curious about the case you mentioned about the overfilling problem so I created a synthetic dataset of 35000 records simulating ten key variables typically monitored in milk spray drying facilities: powder moisture, humidity, equipment calibration drift, temperature, bulk density, feeder rate, vibration of nearby equipment, static, valve delay, hour of the day. 

Using this dataset I trained three different models: linear regression, random forest and gradient boosting and performed a SHAP analysis to identify the most influential features.      

For the workshop task, I decided to use AI help to create a more robust ETL data engineering pipeline that processes manufacturing can weight measurement data into a normalized SQL Server database. It supports batch processing, timezone conversion, logging, and file archiving.

Components:
Can — Production line information
Product — Product attributes and SKU details
Operator — Production operator metadata
WeightMeasurement — Central fact table linked by foreign keys

Data Transformations
Concatenate DATE + TIME → MeasurementDateTime
Localize timestamp to Pacific/Auckland
Convert to UTC
Insert normalized data into respective tables

Features:
Uses environment variables via .env file (no credentials in code).
Efficient executemany() for large datasets.
Converts NZDT timestamps to UTC before database load.
Prevents duplicate records using key-based lookups.
Reads and processes all CSVs in the src/ directory.
Moves successfully processed files into src/processed/.
Records all ETL events, warnings, and errors in etl_log.txt.