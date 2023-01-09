from random import randint
import boto3

from datetime import datetime
from random import randint
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')

SOURCE_TABLE_NAME = 'saga-pattern-example-account-balance-transfer-ChaseBankTable-WVV8N378S236'


def fetch_amount(event, context):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    response = table.get_item(Key={'Id': event['source_account']})
    item = response['Item']
    return item['amount']


def store_amount(event, context):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    amount = event['amount']
    current_balance = fetch_amount(event, context)
    print('current balance', current_balance)
    new_balance = amount + current_balance
    print('current balance', new_balance)

    Id = event['source_account']
    response = table.put_item(
        Item={
            "Id": Id,
            "amount": new_balance
        }
    )


def lambda_handler(event, context):
    source_account = event["source_account"]
    amount_to_transfer = event["amount"]
    destination_account = event["destination_account"]

    # response =  api call to the source account (chase bank, assuming this was a success)

    response_status = 200

    if response_status != 200:
        raise Exception('Failed to withdraw money')

    # withdraw money
    print('Withdrawing money')
    store_amount(event, context)
    transfer_request_event = {
        "id": event['id'],
        "amount": str(amount_to_transfer),
        "destination_account": str(destination_account),
        "timestamp": event['timestamp'],
        "status": response_status
    }

    return transfer_request_event
