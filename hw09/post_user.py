import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body.get('userId')
        name = body.get('name')
        acct_balance = body.get('acctBalance')

        if not user_id or not name or acct_balance is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        table.put_item(
            Item={
                'userid': user_id,
                'name': name,
                'acctBalance': acct_balance
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User created'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
