
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))

bucket_name = os.getenv("S3_BUCKET_NAME")

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"✅ S3 Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"⚠️ Error creating bucket: {e}")
