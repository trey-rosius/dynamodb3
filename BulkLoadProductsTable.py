import json
from pprint import pprint
from decimal import Decimal
import boto3

def bulk_load_data(products,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000")
        table = dynamodb.Table('products')
        
        for product in products:
            id = int(product['id'])
            title = product['title']
            print("item:", id,title)
            table.put_item(Item=product)
    
if __name__=='__main__':
    with open ('products.json') as json_file:
        products = json.load(json_file,parse_float=Decimal)
    bulk_load_data(products)    
                