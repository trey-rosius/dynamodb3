from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_single_product(id,createdDate,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        
    table = dynamodb.Table('products')
        
    try:
        response = table.get_item(Key={'id':id,'createdDate':createdDate})
                               
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        
            
        return response['Item']   
        
if __name__=='__main__':
    product = get_single_product(2,"2021-04-16T12:22:41+00:00")        
    
    if product:
        print("successfully retrieved product")
        pprint(product,sort_dicts=False)      
                