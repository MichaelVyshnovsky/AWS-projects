"""Modified Program of HW03 that allows file actions to be perform and saves them to a S3 Bucket """
import os
import sys
import boto3

def upload(local_folder_name,bucket_name):
    """Uploads all files from the selected folder"""
    s3 = boto3.client('s3')
    for root, _, files in os.walk(local_folder_name):
        for file in files:
            local_path = os.path.join(root,file)
            s3_path = os.path.relpath(local_path, local_folder_name)
            s3.upload_file(local_path,bucket_name, s3_path)
            print(f"Uploaded {local_path} to {bucket_name}/{s3_path}")

def list_buckets():
    """Lists all s3 buckets"""
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response.get('Buckets', [])]

def list_contents(bucker_name):
    """Lists all objects in a Bucket"""
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucker_name)
    return [obj['Key'] for obj in response.get('Contents', [])]

def main_menu():
    """Code for Menu"""
    selected_bucket = "hw04-mdv21001"

    while True:
        print("////////////////////////////////////////////")
        print("\nPlease choose an option:\n")
        print("Backup files: 1")
        print("List all objects: 2")
        print("List all buckets: 3")
        print("Exit Program: 4")
        print("--------------------------------------------")

        choice = input("Enter choice: ")
        if choice == "1":
            local_folder = input("Enter local folder path to upload: ")
            upload(local_folder, selected_bucket)
        elif choice == "2":
            print("Bucket Contents:", list_contents(selected_bucket))
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()
