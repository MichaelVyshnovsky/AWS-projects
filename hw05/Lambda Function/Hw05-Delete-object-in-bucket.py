import json
import boto3

def delete_object_from_bucket(bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        return True
    except Exception as e:
        raise e

def lambda_handler(event, context):
    try:
        path_params = event.get('pathParameters', {})

        bucket_name = path_params.get('bucket-name')
        object_name = path_params.get('object-name')

        if not bucket_name or not object_name:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required path parameters: bucket-name or object-name.'})
            }

        http_method = event.get('requestContext', {}).get('http', {}).get('method', '').upper()
        
        if http_method == 'DELETE':
            delete_object_from_bucket(bucket_name, object_name)

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'message': 'Object deleted successfully.',
                    'bucket': bucket_name,
                    'object_name': object_name
                })
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error: {str(e)}'})
        }
