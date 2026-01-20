import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['AUCTIONS_TABLE'])

def lambda_handler(event, context):
    path_params = event.get('pathParameters')
    
    try:
        # Case 1: GET /auction/{auctionId}
        if path_params and 'auctionId' in path_params:
            auction_id = path_params['auctionId']
            response = table.get_item(Key={'PK': auction_id})
            item = response.get('Item')

            if item:
                return {
                    'statusCode': 200,
                    'body': json.dumps(item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'error': 'Auction not found'})
                }

        # Case 2: GET /auction -> get all auctions
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
