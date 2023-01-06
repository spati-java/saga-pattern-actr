from datetime import datetime
from random import randint
from uuid import uuid4


def lambda_handler(event, context):

    destination_account = event["destination_account"]
    amount = event["amount"]
    # Mocked result of a stock selling transaction
    # make an api call to the bank of america using the amount to transfer

    response_status = 300
    if response_status != 200:
        raise Exception("Failed to deposit money")

    transfer_request_event = {
        "id": id,
        "amount": str(amount),
        "destination_account": str(destination_account),
        "timestamp": event['timestamp'],
        "status": response_status,
        "message": "Transaction Succeeded"
    }
    print(transfer_request_event)
    return {"message": "Transaction Succeeded"}
