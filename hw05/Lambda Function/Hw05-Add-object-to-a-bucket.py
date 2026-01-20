import json
import boto3

def add_object_to_bucket(bucket_name, object_name, file_contents):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=file_contents
        )

def lambda_handler(event, context):
    try:
        bucket_name = event['pathParameters']['bucket-name']
        http_method = event['requestContext']['http']['method']

        if http_method == 'POST':
            body = json.loads(event['body'])
            object_name = body.get('name')
            file_contents = body.get('contents')

            if not object_name or not file_contents:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'Both object_name and file_contents are required.'})
                }

            add_object_to_bucket(bucket_name, object_name, file_contents)

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'message': 'Object added successfully',
                    'bucket': bucket_name,
                    'object_name': object_name
                })
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Internal Server Error: {str(e)}'})
        }
