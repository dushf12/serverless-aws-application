import json
import boto3

def lambda_handler(event, context):
    # Parse S3 event data
    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    file_name = s3_event['object']['key']
    
    # Store metadata in DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FileMetadata')
    table.put_item(Item={
        'FileName': file_name,
        'BucketName': bucket_name
    })

    return {
        'statusCode': 200,
        'body': json.dumps('File metadata stored successfully!')
    }
