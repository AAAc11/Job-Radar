import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def upload_raw_data_to_s3():
    region = os.getenv("AWS_REGION")

    s3_client = boto3.client('s3', region_name=region)

    file_path = 'data/raw_nfj.json'
    bucket_name = 'job-radar-data-lake-anna'
    target_path = 'raw/nofluffjobs/data.json'

    print("Sending raw data to S3")

    try:
        s3_client.upload_file(
            Filename=file_path, 
            Bucket=bucket_name, 
            Key=target_path
        )
    except Exception as e:
        print(f"Error occured: {e}")
    else:
        print("Raw data succesfully sent to S3 bucket")

if __name__ == '__main__':
    upload_raw_data_to_s3()