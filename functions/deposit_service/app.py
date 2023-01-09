import boto3

from datetime import datetime
from random import randint
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')

DESTINATION_TABLE_NAME = 'saga-pattern-example-account-balance-transfer-BankOfAmericaTable-1IRU241ZT1Q1B'


def fetch_amount(event, context):
    table = dynamodb.Table(DESTINATION_TABLE_NAME)
    response = table.get_item(Key={'Id': event['destination_account']})
    item = response['Item']
    return item['amount']


def store_amount(event, context):
    table = dynamodb.Table(DESTINATION_TABLE_NAME)
    amount = event['amount']
    new_balance = amount + fetch_amount(event, context)
    Id = event['destination_account']
    response = table.put_item(
        Item={
            "Id": Id,
            "amount": new_balance
        }
    )


def lambda_handler(event, context):
    destination_account = event["destination_account"]
    amount = event["amount"]

    response_status = 200
    if response_status != 200:
        raise Exception("Failed to deposit money")
    # deposit money
    store_amount(event, context)
    transfer_request_event = {
        "id": id,
        "amount": str(amount),
        "destination_account": str(destination_account),
        "timestamp": event['timestamp'],
        "status": response_status,
        "message": "Transaction Succeeded"
    }

    return {"message": "Transaction Succeeded"}
