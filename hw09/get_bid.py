import json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['hw09-BidsTable-mdv21001'])

def lambda_handler(event, context):
    auction_id = event['queryStringParameters'].get('auction')
    
    if not auction_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing auction query parameter'})
        }

    try:
        response = table.query(
            KeyConditionExpression=Key('PK').eq(auction_id)
        )
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
