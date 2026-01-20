"""
Lambda function to generate thumbnails for image uploads in AWS S3.
Triggered by SNS messages containing S3 event data.
"""

import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError

s3_client = boto3.client('s3')

def lambda_handler(event: dict, _context) -> None:
    """Processes SNS messages to create thumbnails from S3 image uploads."""
    print("Received event:", json.dumps(event, indent=2))

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

            if not key.lower().endswith(('png', 'jpg', 'jpeg')):
                print(f"Skipping non-image file: {key}")
                continue

            response = s3_client.get_object(Bucket=bucket, Key=key)
            image_data = response['Body'].read()
            resized_image_data = image_data[:10000]  # Simulated resize

            thumbnail_bucket = "hw07-thumbnail-mdv21001"
            thumbnail_key = f"thumbnails/{key}"

            s3_client.put_object(
                Bucket=thumbnail_bucket,
                Key=thumbnail_key,
                Body=resized_image_data,
                ContentType=response.get('ContentType', 'application/octet-stream')
            )
            print(f"Thumbnail saved to {thumbnail_bucket}/{thumbnail_key}")

        except json.JSONDecodeError:
            print("Error decoding JSON in SNS message.")
        except KeyError as e:
            print(f"Missing expected key: {str(e)}")
        except (BotoCoreError, ClientError) as e:
            print(f"AWS S3 error: {str(e)}")
