import boto3

dynamodb = boto3.resource('dynamodb')

SOURCE_TABLE_NAME = 'ChaseBankTable'

DESTINATION_TABLE_NAME = 'saga-pattern-example-account-balance-transfer-BankOfAmericaTable-1IRU241ZT1Q1B'


def store_amount(event, context):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    amount = event['amount']
    Id = event['source_account']
    response = table.put_item(
        Item={
            "Id": Id,
            "amount": amount
        }
    )


def fetch_amount(event, context):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    response = table.get_item(Key={'Id': event['source_account']})
    item = response['Item']
    return item['amount']


def lambda_handler(event, context):
    event_type = event['type']
    if event_type == 'store':
        store_amount(event, context)
    else:
        fetch_amount(event, context)
        print(fetch_amount(event, context))
    return "SUCCESS"
