import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def lambda_handler(event, context):
    path_params = event.get('pathParameters')
    
    try:
        # Case 1: GET /user/{userId}
        if path_params and 'userId' in path_params:
            user_id = path_params['userId']
            response = table.get_item(Key={'PK': user_id})
            item = response.get('Item')

            if item:
                return {
                    'statusCode': 200,
                    'body': json.dumps(item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'error': 'User not found'})
                }

        # Case 2: GET /user -> scan all users
        response = table.scan()
        items = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
