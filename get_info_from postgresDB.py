import json
import time
from calendar import timegm
from db_util import make_conn, fetch_data
import pandas as pd


def lambda_handler(event, context):
       
    conn = make_conn()
    result = fetch_data(conn)
    conn.close()    
    
    dataframe = pd.DataFrame(result, columns=['barcode', 'description', 'year', 'stockqty'])
      
    return {
            'statusCode': 200,
            'body': json.loads(dataframe.to_json(orient="records")),
        }
