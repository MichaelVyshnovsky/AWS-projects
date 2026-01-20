"""Tests S3 bucket actions"""
import boto3
import pytest
from moto import mock_aws
from main import list_buckets, upload, delete_object, list_contents

@pytest.fixture
def s3(name="s3_instance"):
    """S3 setup"""
    with mock_aws():
        temp = name
        name = temp
        s3_client = boto3.client("s3", region_name="us-east-1")
        bucket_name = "test-bucket"
        s3_client.create_bucket(Bucket=bucket_name)
        yield s3_client, bucket_name

def test_list_buckets(s3_instance):
    """Test listing buckets"""
    _, bucket_name = s3_instance
    buckets = list_buckets()
    assert bucket_name in buckets

def test_upload(s3_instance, tmp_path):
    """Test uploading files"""
    s3_client, bucket_name = s3_instance
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test file")
    upload(str(test_file), bucket_name)
    objects = s3_client.list_objects_v2(Bucket=bucket_name).get("Contents", [])
    assert any(obj["Key"] == "test.txt" for obj in objects)

def test_list_contents(s3_instance, tmp_path):
    """Test listing bucket contents"""
    _, bucket_name = s3_instance
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test file")
    upload(str(test_file), bucket_name)
    contents = list_contents(bucket_name)
    assert "test.txt" in contents

def test_delete_object(s3_instance, tmp_path):
    """Test deleting an object"""
    s3_client, bucket_name = s3_instance
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test file")
    upload(str(test_file), bucket_name)
    delete_object(bucket_name, "test.txt")
    objects = s3_client.list_objects_v2(Bucket=bucket_name).get("Contents", [])
    assert not any(obj["Key"] == "test.txt" for obj in objects)

if __name__ == "__main__":
    pytest.main()
