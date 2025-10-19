==============================
 ETL Data Engineer Test
==============================

Welcome! Please follow the instructions below to complete the ETL exercise.
Each step is important for a robust data pipeline.

------------------------------
 TO DO List
------------------------------

1️⃣  Create the required tables in SQL Server
    - Use the ERD.png and the provided SQL template.
    - Ensure all primary and foreign keys are set up correctly.

2️⃣  Set up a secure connection to SQL Server in Python
    - Use environment variables (e.g., with python-dotenv and pyodbc).

    SQL_DRIVER={ODBC Driver 17 for SQL Server}
    DB_SERVER=10.111.22.333
    DB_INSTANCE=SQLSERVER444\SQLEXPRESS
    DB_PORT=1433
    DB_NAME=TechTest
    DB_USER=TechTestUser
    DB_PASSWORD=StrongPassword123!

    - Do not hardcode credentials in your etl.py script.

3️⃣  Read CSV file
    - Read using pandas library and save as dataframe (e.g., df)

4️⃣  Insert measurement into WeightMeasurement table
    - Use the pandas dataframe and cursor to insert data into the SQL Server table.
    - Ensure that the data columns match the SQL Server schema.

5️⃣  EXTRA CREDIT: Transform data from NZDT to UTC
    - Use the pandas library to convert the 'NZDT' column in the dataframe to UTC.
    - Ensure that the transformation is applied before inserting into the SQL Server table.

------------------------------
 Good luck! 🚀
------------------------------
