'''
These are methods using the S3 Resource API. Feel free to switch to use
the S3 Client API
'''
import boto3
from hw03_main import list_contents,upload

def create_client():
    '''Create the S3 client'''   
    # Feel free to switch to the Client API instead of using the Resouce API 
    return boto3.resource('s3')

def list_objects(bucket_name):
    '''Returns a list of objects in the bucket'''
    contents = list_contents(bucket_name)
    return contents

def upload_file_to_s3(file, bucket_name):
    '''Uploads a file to S3'''
    s3 = create_client()
    upload(file, bucket_name)

#if __name__ == "__main__":
    # You can unit test your methods before trying to integrate with the HTML code
    #l = list_objects("hw06-mdv21001")
    #print(l)