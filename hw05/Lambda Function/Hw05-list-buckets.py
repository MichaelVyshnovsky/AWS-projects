import json
import boto3

def list_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    return [bucket['Name'] for bucket in response.get('Buckets', [])]

def lambda_handler(event, context):
    try:
        buckets = list_buckets()
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'buckets': buckets})
        }
    except Exception as e:
        print(f"Lambda error: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Internal Server Error'})
        }
