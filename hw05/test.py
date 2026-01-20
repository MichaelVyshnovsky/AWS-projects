import pytest
from http_utils import get, post, delete

def test_list_buckets(requests_mock):
    url = "https://test.com/list"
    mock_response = {"buckets": ["bucket1", "bucket2"]}
    requests_mock.get(url, json=mock_response)
    response = get(url)
    assert response == mock_response

def test_list_objects(requests_mock):
    bucket_name = "test-bucket"
    url = f"https://test.com/{bucket_name}"
    mock_response = {"objects": ["file1.txt", "file2.txt"]}
    requests_mock.get(url, json=mock_response)
    response = get(url)
    assert response == mock_response

def test_add_object(requests_mock):
    bucket_name = "test-bucket"
    url = f"https://test.com/{bucket_name}"
    post_data = {"file_name": "file1.txt", "body": "content"}
    mock_response = {"message": "Object added successfully"}
    requests_mock.post(url, json=mock_response)
    response = post(url, post_data)
    assert response == mock_response

def test_delete_object(requests_mock):
    bucket_name = "test-bucket"
    object_name = "file1.txt"
    url = f"https://test.com/{bucket_name}/{object_name}"
    delete_data = {"bucket": bucket_name, "file_name": object_name}
    mock_response = {"message": "Object deleted successfully"}
    requests_mock.delete(url, json=mock_response)
    response = delete(url, delete_data)
    assert response == mock_response

if __name__ == "__main__":
    pytest.main()
