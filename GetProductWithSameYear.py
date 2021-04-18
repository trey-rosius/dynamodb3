from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_products(yearManufactured, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('products')
    print(f"Get id, description, price, and category")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="id, title, description, category",
        
       
        KeyConditionExpression= Key('yearManufactured').eq(yearManufactured)
            
    )
    return response['Items']


if __name__ == '__main__':
    yearManufactured = 2001
    products = query_and_project_products(yearManufactured)
    for product in products:
        pprint(product)