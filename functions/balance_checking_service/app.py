from datetime import datetime
from random import randint
from uuid import uuid4


def lambda_handler(event, context):
    source_account = event["source_account"]
    amount_to_transfer = event["amount"]
    destination_account = event["destination_account"]
    # Withdraw the money from the source account
    # response =  api call to the source account (chase bank, assuming this was a success)

    transfer_request_event = {
        "id": str(uuid4()),
        "amount": str(amount_to_transfer),
        "destination_account": str(destination_account),
        "source_account": str(source_account),
        "timestamp": datetime.now().isoformat(),
        "status": "200"
    }

    return transfer_request_event
