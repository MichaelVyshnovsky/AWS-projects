import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['AUCTIONS_TABLE'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        auction_id = body.get('auctionId')
        item_name = body.get('itemName')
        reserve = body.get('reserve')
        description = body.get('description')
        status = body.get('status')
        winning_user_id = body.get('winningUserId', '')

        if not auction_id or not item_name or reserve is None or not description or not status:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        table.put_item(
            Item={
                'PK': auction_id,
                'itemName': item_name,
                'reserve': reserve,
                'description': description,
                'status': status,
                'winningUserId': winning_user_id
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Auction created'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
