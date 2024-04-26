import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')
    remove = table.delete_item(
        Key={
            'year': '2006',
            'title': '300'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(remove)
    }
