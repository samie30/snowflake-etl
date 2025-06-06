
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cs = conn.cursor()

# Create Table
cs.execute("""
CREATE OR REPLACE TABLE employee_data (
    id INT,
    name STRING,
    age INT,
    department STRING
);
""")

# Create Stage
cs.execute(f"""
CREATE OR REPLACE STAGE {os.getenv("SNOWFLAKE_STAGE")}
STORAGE_INTEGRATION = my_s3_integration
URL = 's3://{os.getenv("S3_BUCKET_NAME")}/';
""")

# Load Data
cs.execute(f"""
COPY INTO employee_data
FROM @{os.getenv("SNOWFLAKE_STAGE")}/sample_data.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
ON_ERROR = 'CONTINUE';
""")

print("✅ Data loaded into Snowflake successfully.")
cs.close()
conn.close()
