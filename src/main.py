from extract_nfj import fetch_data_from_api
from load_to_s3 import upload_raw_data_to_s3
from transform_nfj import tranform_json_to_db
from load_to_db import load_data_to_db

def main_function():
    fetch_data_from_api()
    upload_raw_data_to_s3()
    load_data_to_db()

if __name__ == "__main__":
    main_function()