from datetime import datetime
from random import randint
from uuid import uuid4
import boto3

import json

dynamodb = boto3.resource('dynamodb')
SOURCE_TABLE_NAME = 'saga-pattern-example-account-balance-transfer-ChaseBankTable-S5Y10F6Z79ZT'


def fetch_amount(event, context):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    response = table.get_item(Key={'Id': event['source_account']})
    item = response['Item']
    return item['amount']


def store_amount(account_id, amount):
    table = dynamodb.Table(SOURCE_TABLE_NAME)
    print("storng data ", account_id, amount)
    response = table.put_item(
        Item={
            "Id": account_id,
            "amount": amount
        }
    )
    return response


def rollback_withdrawal(account_id, amount):
    return store_amount(account_id, amount)


def rollback_deposit(account_id, amount):
    # Nothing to do since deposit was not success
    # But can do things in case deposit was success but some other reasons the deposit needs to be rolled back
    pass


def compensation(event, context):
    error = event['error']['Cause']
    error_json = json.loads(error)
    message = error_json['errorMessage']
    source_account = event['source_account']
    if message == "Failed to check balance":  # No further action is required
        return

    elif error == "Insufficient balance":  # No further action is required
        message

    elif message == "Failed to withdraw money":
        account_id = source_account
        amount = event['amount']

        rollback_withdrawal(account_id, amount)

    elif message == "Failed to deposit money":
        account_id = source_account
        amount = event['amount']
        current_balance = fetch_amount(event, context)

        print("print current balance ", current_balance)
        rollback_amount = current_balance + amount
        print('amount to be roll back', rollback_amount)
        rollback_withdrawal(account_id, rollback_amount)
        return {"message": "Money returned to the source account due to a failure"}


def lambda_handler(event, context):
    return compensation(event, context)
