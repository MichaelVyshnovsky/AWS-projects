"""Tests if object to S3 and verifies Lambda processed it and checking DynamoDB"""
import os
import time
import boto3

s3 = boto3.client("s3", region_name="us-east-1")
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

BUCKET_NAME = "hw04-mdv21001"
TABLE_NAME = "hw04-mdv21001"
TEST_OBJECT_KEY = "test_object.txt"
TEST_OBJECT_CONTENT = "This is a test."

def upload_to_s3():
    """Uploads a test object to the specified S3 bucket."""
    s3.put_object(Bucket=BUCKET_NAME, Key=TEST_OBJECT_KEY)
    with open(TEST_OBJECT_KEY, "w", encoding="utf-8") as f:
        f.write(TEST_OBJECT_CONTENT)

def get_dynamodb_record():
    """Fetches the record from DynamoDB corresponding to the test object."""
    table = dynamodb.Table(TABLE_NAME)
    time.sleep(5)
    response = table.get_item(Key={"file name": TEST_OBJECT_KEY})
    return response.get("Item")

def delete_s3_object():
    """Deletes the test object from the S3 bucket."""
    s3.delete_object(Bucket=BUCKET_NAME, Key=TEST_OBJECT_KEY)
    table = dynamodb.Table(TABLE_NAME)
    table.delete_item(Key={"file name": TEST_OBJECT_KEY})

def delete_local_file():
    """Deletes the local test file if it exists."""
    if os.path.exists(TEST_OBJECT_KEY):
        os.remove(TEST_OBJECT_KEY)

def main():
    """Uploads an object to S3 and verifies Lambda processed it correctly by checking DynamoDB."""
    upload_to_s3()
    record = get_dynamodb_record()

    if record is None:
        print("DynamoDB record was not created.")
    elif record.get("file name") != TEST_OBJECT_KEY:
        print("DynamoDB record content mismatch.")
    else:
        print("Test passed: DynamoDB record is correct.")

    delete_s3_object()
    delete_local_file()

if __name__ == "__main__":
    main()
