import json
import boto3

def lambda_handler(event, context):
    
    

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'year': '1997',
                'title': 'The Fifth Element'
                }
        )
        batch.put_item(
            Item={
                'year': '2006',
                'title': '300'
                }
        )
        batch.put_item(
            Item={
                'year': '2010',
                'title': 'Tron: Legacy'
                }
        )
        batch.put_item(
            Item={
                'year': '2010',
                'title': 'Inception'
                }
        )

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
