
import boto3
import pytest
from moto import mock_s3

@mock_s3
def test_mock_upload_employee_benefits_files():
    s3 = boto3.client("s3", region_name="us-east-1")
    bucket_name = "mock-bucket"
    s3.create_bucket(Bucket=bucket_name)

    # Simulated file keys
    file_keys = [
        "employee_benefits_2019.csv",
        "employee_benefits_2020.csv",
        "employee_benefits_2021.csv",
        "employee_benefits_2022.csv",
        "employee_benefits_2023.csv"
    ]

    # Simulate upload
    for key in file_keys:
        s3.put_object(Bucket=bucket_name, Key=key, Body="some,data,to,upload\n1,2,3,4")

    # Check that files exist
    for key in file_keys:
        response = s3.head_object(Bucket=bucket_name, Key=key)
        assert response["ResponseMetadata"]["HTTPStatusCode"] == 200
