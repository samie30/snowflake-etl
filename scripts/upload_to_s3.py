
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))

bucket_name = os.getenv("S3_BUCKET_NAME")
file_path = "data/sample_data.csv"
s3_key = "sample_data.csv"

s3.upload_file(file_path, bucket_name, s3_key)
print(f"✅ Uploaded '{file_path}' to '{bucket_name}/{s3_key}'")
