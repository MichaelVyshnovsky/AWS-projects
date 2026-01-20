"""
Lambda function to store image metadata in DynamoDB.
Triggered by SNS messages containing S3 event data.
"""

import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event: dict, _context) -> None:
    """Processes SNS messages and stores image metadata in DynamoDB."""
    table_name = "hw07-table-mdv21001"
    table = dynamodb.Table(table_name)

    for record in event.get('Records', []):
        try:
            sns_message = json.loads(record.get('body', '{}'))
            sns_payload = json.loads(sns_message.get('Message', '{}'))
            s3_info = sns_payload.get('Records', [{}])[0]

            bucket = s3_info.get('s3', {}).get('bucket', {}).get('name')
            key = s3_info.get('s3', {}).get('object', {}).get('key')

            if not bucket or not key:
                print("Skipping record due to missing bucket or key.")
                continue

            response = s3_client.head_object(Bucket=bucket, Key=key)

            metadata = {
                'key': key,
                'Bucket': bucket,
                'Size': response['ContentLength'],
                'LastModified': response['LastModified'].isoformat()
            }

            table.put_item(Item=metadata)
            print(f"Metadata stored for {key}")

        except json.JSONDecodeError:
            print("Error decoding JSON in SNS message.")
        except KeyError as e:
            print(f"Missing expected key: {str(e)}")
        except (BotoCoreError, ClientError) as e:
            print(f"AWS error: {str(e)}")
