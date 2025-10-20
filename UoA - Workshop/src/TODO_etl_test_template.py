# ETL for Can Weight Report CSV to new DB schema (Interview Template)

import pandas as pd
import pyodbc
import logging
import os
from dotenv import load_dotenv

# Logger setup
logging.basicConfig(
    filename="std.log", format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# TODO_#2
# Load environment variables from .env file (hint: using python-dotenv library)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
instance = os.getenv("DB_INSTANCE")
port = os.getenv("DB_PORT", "1433")
driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

conn_str = f"DRIVER={{{driver}}};SERVER={server};UID={username};PWD={password};PORT={port};INSTANCE={instance}"

try:
    cnxn = pyodbc.connect(conn_str)
finally:
    logger.info("Successfully connected to the database.")
    logger.info(cnxn)

#################################### END_of_TODO_#2 #############################################

cnxn.autocommit = True
cursor = cnxn.cursor()

# TODO
# Read CSV file into pandas dataframe

csv_file_path = os.path.join(os.path.dirname(__file__), "DATA_101549999 Can Weight Report.csv")
df = pd.read_csv(csv_file_path)

# #################################### END_of_TODO_#3 #############################################


# Helper functions to get or insert and return IDs
def get_or_insert_can(line_name):
    logger.debug(f"Looking up CanID for LineName: {line_name}")
    cursor.execute("SELECT CanID FROM Can WHERE LineName = ?", line_name)
    row = cursor.fetchone()
    if row:
        logger.debug(f"Found existing CanID: {row[0]} for LineName: {line_name}")
        return row[0]
    try:
        cursor.execute("INSERT INTO Can (LineName) VALUES (?)", line_name)
        cursor.execute("SELECT SCOPE_IDENTITY()")
        can_id = cursor.fetchone()[0]
        logger.debug(f"Inserted new CanID: {can_id} for LineName: {line_name}")
        return can_id
    except Exception as e:
        logger.error(f"Failed to insert/select CanID for LineName '{line_name}': {e}")
        return None


def get_or_insert_product(product_name, product_code=None):
    logger.debug(
        f"Looking up ProductID for ProductName: {product_name}, ProductCode: {product_code}"
    )
    cursor.execute("SELECT ProductID FROM Product WHERE ProductName = ?", product_name)
    row = cursor.fetchone()
    if row:
        logger.debug(
            f"Found existing ProductID: {row[0]} for ProductName: {product_name}"
        )
        return row[0]
    try:
        cursor.execute(
            "INSERT INTO Product (ProductName, ProductCode) VALUES (?, ?)",
            product_name,
            product_code,
        )
        cursor.execute("SELECT SCOPE_IDENTITY()")
        product_id_row = cursor.fetchone()
        product_id = product_id_row[0] if product_id_row else None
        logger.debug(
            f"Inserted new ProductID: {product_id} for ProductName: {product_name}"
        )
        return product_id
    except Exception as e:
        logger.error(
            f"Failed to insert/select ProductID for ProductName '{product_name}': {e}"
        )
        return None


def get_or_insert_operator(operator_name):
    logger.debug(f"Looking up OperatorID for OperatorName: {operator_name}")
    cursor.execute(
        "SELECT OperatorID FROM Operator WHERE OperatorName = ?", operator_name
    )
    row = cursor.fetchone()
    if row:
        logger.debug(
            f"Found existing OperatorID: {row[0]} for OperatorName: {operator_name}"
        )
        return row[0]
    try:
        cursor.execute("INSERT INTO Operator (OperatorName) VALUES (?)", operator_name)
        cursor.execute("SELECT SCOPE_IDENTITY()")
        operator_id_row = cursor.fetchone()
        operator_id = operator_id_row[0] if operator_id_row else None
        logger.debug(
            f"Inserted new OperatorID: {operator_id} for OperatorName: {operator_name}"
        )
        return operator_id
    except Exception as e:
        logger.error(
            f"Failed to insert/select OperatorID for OperatorName '{operator_name}': {e}"
        )
        return None

def insert_weight_measurement(can_id, product_id, operator_id, datetime, weight, shift, comments):
    logger.debug("Inserting WeightMeasurement")
    try:
        cursor.execute(
            "INSERT INTO WeightMeasurement (CanID, ProductID, OperatorID, DateTime, Weight, Shift, Comments) VALUES (?, ?, ?, ?, ?, ?, ?)",
            can_id, product_id, operator_id, datetime, weight, shift, comments
        )
        cursor.execute("SELECT SCOPE_IDENTITY()")
        weight_id_row = cursor.fetchone()
        weight_id = weight_id_row[0] if weight_id_row else None
        logger.debug(f"Inserted new WeightMeasurementID: {weight_id}")
        return weight_id
    except Exception as e:
        logger.error(f"Failed to insert WeightMeasurement': {e}")
        return None

# Map CSV columns to DB columns and perform ETL
for idx, row in df.iterrows():
    try:
        # Set LineName as 'Mountain Line' for all rows
        line_name = "Mountain Line"

        # Get ProductName from FORMULATION column
        product_name = row.get("FORMULATION", None)
        product_code = row.get("SKU", None)  # Use SKU as product code

        # Get Operator from USER column
        operator_name = row.get("USER", None)

        # Combine DATE and TIME columns for DateTime
        date_str = str(row.get("DATE", ""))
        time_str = str(row.get("TIME", ""))
        if date_str and time_str:
            try:
                dt = pd.to_datetime(
                    f"{date_str} {time_str}", dayfirst=True
                ).dt.tz_localize(
                    'Pacific/Auckland'
                ).dt.tz_convert('UTC')
            except Exception:
                dt = None
        else:
            dt = None

        # Get Weight from CAN NET WEIGHT column
        weight = row.get("CAN NET WEIGHT", None)

        # Set Shift as 'D' and Comments as 'N/A'
        shift = "D"
        comments = "N/A"

        # Skip if ProductName is missing (to avoid NULL error)
        if not product_name or pd.isna(product_name):
            logger.warning(
                f"Row {idx+1} skipped: ProductName (FORMULATION) is missing."
            )
            continue

        # Insert or get IDs
        can_id = get_or_insert_can(line_name)
        if can_id is None:
            logger.warning(
                f"Row {idx+1} skipped: Could not get or insert CanID for LineName '{line_name}'."
            )
            continue
        product_id = get_or_insert_product(product_name, product_code)
        if product_id is None:
            logger.warning(
                f"Row {idx+1} skipped: Could not get or insert ProductID for ProductName '{product_name}'."
            )
            continue
        operator_id = get_or_insert_operator(operator_name)
        if operator_id is None:
            logger.warning(
                f"Row {idx+1} skipped: Could not get or insert OperatorID for OperatorName '{operator_name}'."
            )
            continue

        # TODO
        # Insert measurement into WeightMeasurement table
        
        weight_measurement_id = insert_weight_measurement(
            can_id, product_id, operator_id, dt, weight, shift, comments
        )
        #################################### END_of_TODO_#4 #############################################
        logger.info(f"Inserted measurement row {idx+1}")
    except Exception as e:
        logger.warning(f"Failed to insert row {idx+1}: {e}")

cnxn.close()
