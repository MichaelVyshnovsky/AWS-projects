"""Programs that allows file actions to be perform and saves them to a S3 Bucket"""
import os
import sys
import boto3

def upload(file, bucket_name):
    """Uploads a single file to S3"""
    s3 = boto3.client('s3')

    # Extract the filename from the uploaded file
    file_name = file.filename  

    if not file_name:
        return {"message": "Error: No file selected."}

    # Save the file temporarily before uploading
    temp_path = f"/tmp/{file_name}"  # For Linux/macOS
    if os.name == "nt":  # If Windows, adjust path
        temp_path = os.path.join(os.getenv("TEMP"), file_name)

    file.save(temp_path)  # Save file locally before uploading
    s3.upload_file(temp_path, bucket_name, file_name)  # Upload to S3

    # Optional: Remove temporary file after upload
    os.remove(temp_path)

    return {"message": f"Uploaded {file_name} to {bucket_name}/{file_name}"}

def upload_folder(local_folder_name,bucket_name):
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

def list_contents(bucket_name):
    """Lists all objects in a Bucket with Name, Size, and Last Modified"""
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        return []

    return [
        {
            "Name": obj["Key"],
            "Size": obj["Size"],
            "LastModified": obj["LastModified"].strftime("%Y-%m-%d %H:%M:%S")
        }
        for obj in response["Contents"]
    ]

def get_file(bucket_name, file_name, download_path):
    """Download a specific file from a bucket"""
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, download_path)
    print(f"Downloaded {file_name} to {download_path}")

def delete_object(bucket_name, file_name):
    """Delete a object from a bucket."""
    s3 = boto3.client('s3')
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    print(f"Deleted {file_name} from {bucket_name}")

def generate_presigned_url(bucket_name, file_name, expiration=3600):
    """Generate a pre-signed URL for the selected object."""
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': bucket_name, 'Key': file_name},
                                    ExpiresIn=expiration)
    return url

def list_versions(bucket_name):
    """Lists all versions of objects in an bucket."""
    s3 = boto3.client('s3')

    response = s3.list_object_versions(Bucket=bucket_name)

    versions = []
    for version in response['Versions']:
        versions.append({
            "Key": version["Key"],
            "VersionId": version["VersionId"],
            "LastModified": version["LastModified"],
            "IsLatest": version["IsLatest"],
            "Size": version.get("Size", "N/A")
        })

    return versions

def main_menu():
    """Code for Menu"""
    selected_bucket = None

    while True:
        print("////////////////////////////////////////////")
        print("\nPlease choose an option:\n")
        print("Pick a bucket to perform actions on: 0")
        print("List all buckets: 1")
        print("Backup files: 2")
        print("List all objects: 3")
        print("Download a specific object: 4")
        print("Generate a pre-signed URL: 5")
        print("List all version information for a bucket: 6")
        print("Delete File: 7")
        print("Exit Program: 8")
        print("--------------------------------------------")

        choice = input("Enter choice: ")
        if choice == "0":
            print("Available Buckets:", list_buckets())
            selected_bucket = input("Enter bucket name: ")
        elif choice == "1":
            print("Available Buckets:", list_buckets())
        elif choice == "2":
            local_folder = input("Enter local folder path to upload: ")
            upload(local_folder, selected_bucket)
        elif choice == "3":
            print("Bucket Contents:", list_contents(selected_bucket))
        elif choice == "4":
            file_name = input("Enter file name to download: ")
            download_path = input("Enter local path to save the file: ")
            get_file(selected_bucket, file_name, download_path)
        elif choice == "5":
            file_name = input("Enter file name to generate a pre-signed URL: ")
            print("Pre-signed URL:", generate_presigned_url(selected_bucket, file_name))
        elif choice == "6":
            print("\nObject Versions:")
            versions = list_versions(selected_bucket)
            for version in versions:
                print(f"File: {version['Key']}, Version ID: {version['VersionId']}, "
                      f"Last Modified: {version['LastModified']}, Latest: {version['IsLatest']},"
                      f"Size: {version['Size']} bytes")
        elif choice == "7":
            file_name = input("Enter file name to delete: ")
            delete_object(selected_bucket, file_name)
        elif choice == "8":
            sys.exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()
