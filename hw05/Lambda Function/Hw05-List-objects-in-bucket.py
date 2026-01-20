import json
import boto3

def list_objects(bucket_name):
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    return [obj['Key'] for obj in response.get('Contents', [])]

def lambda_handler(event, context):
    try:
        bucket_name = event['pathParameters']['bucket-name']
        http_method = event['requestContext']['http']['method']
        if http_method == 'GET':
            objects = list_objects(bucket_name)
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'bucket': bucket_name, 'objects': objects})
            }

        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Internal Server Error: {str(e)}'})
        }
