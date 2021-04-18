import boto3


def create_products_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='products',
        KeySchema=[
            {
                'AttributeName': 'yearManufactured',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'createdDate',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'yearManufactured',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'createdDate',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    product_table = create_products_table()
    print("Table status:", product_table.table_status)