from datetime import datetime
import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')

TABLE_NAME = 'saga-pattern-example-account-balance-transfer-TransactionTable-UL85DR1JV3TB'


def fetch_amount(event, context):
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'Id': event['source_account']})
    item = response['Item']
    return item['amount']


def check_balance(event, context):
    source_account = event["source_account"]
    amount_to_transfer = event["amount"]
    destination_account = event["destination_account"]
    # Withdraw the money from the source account
    # response =  api call to the source account (chase bank, assuming this was a success)
    response_status = 200

    if response_status != 200:
        raise Exception("Failed to check balance")

    balance = fetch_amount(event, context)

    if balance < int(amount_to_transfer):
        raise Exception("Insufficient Balance")

    transfer_request_event = {
        "id": str(uuid4()),
        "amount": str(amount_to_transfer),
        "destination_account": str(destination_account),
        "source_account": str(source_account),
        "timestamp": datetime.now().isoformat(),
        "status": "200"
    }

    return transfer_request_event


def lambda_handler(event, context):
    return check_balance(event, context)
