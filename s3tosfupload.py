from config import account,user,password,warehouse,database,schema
import snowflake.connector

""" # Set the Snowflake connection parameters
account = 'your_account_name'
user = 'your_username'
password = 'your_password'
warehouse = 'your_warehouse_name'
database = 'your_database_name'
schema = 'your_schema_name' """

# Set the local file path
local_file_path = 'dataengineering_posts.csv'

# Create a Snowflake connection
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# Create a Snowflake cursor
cur = conn.cursor()

# Create a Snowflake table with the same column names and data types as the CSV file
with open(local_file_path, 'r') as file:
    header = file.readline().strip()
    columns = ','.join([f'{col} VARCHAR' for col in header.split(',')])
    create_table_query = f'CREATE TABLE IF NOT EXISTS R_DATA_ENGINEERING ({columns})'
    cur.execute(create_table_query)

# Copy the data from the CSV file to the Snowflake table
copy_query = f"COPY INTO R_DATA_ENGINEERING FROM '@REDDIT/{local_file_path}' FILE_FORMAT = (type = csv) ON_ERROR = 'CONTINUE'"
cur.execute(copy_query)

# Close the Snowflake cursor and connection
cur.close()
conn.close()

