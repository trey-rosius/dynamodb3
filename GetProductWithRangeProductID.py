from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project_products(id,createdDate, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('products')
    print(f"Get id, description, price, and category")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="id, title, description, category",
        
        #ExpressionAttributeNames={"#nm": "name"},
        KeyConditionExpression= Key('createdDate').eq(createdDate[0]),
             ScanIndexForward=True,
    )
    return response['Items']


if __name__ == '__main__':
    query_id = 3
    
    query_range = ('2021-04-16T12:22:41+00:00', '2021-04-14T12:39:34+00:00')
  
    products = query_and_project_products(query_id, query_range)
    for product in products:
        print(f"\n{product['id']} : {product['title']}")
        pprint(product['description'])