
import subprocess

print("🔁 Starting end-to-end ETL pipeline...")
subprocess.call(["python", "scripts/create_s3_bucket.py"])
subprocess.call(["python", "scripts/upload_to_s3.py"])
subprocess.call(["python", "scripts/load_to_snowflake.py"])
print("✅ ETL pipeline completed successfully.")
