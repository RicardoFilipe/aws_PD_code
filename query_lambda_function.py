import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq('2010')
    )

    item = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
