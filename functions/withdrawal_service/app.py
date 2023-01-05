from random import randint


def lambda_handler(event, context):
    id = event["id"]
    source_account = event["source_account"]
    amount_to_transfer = event["amount"]
    destination_account = event["destination_account"]
    # Withdraw the money from the source account
    # response =  api call to the source account (chase bank, assuming this was a success)

    # geenerate the response event  for the next service to pick
    transfer_request_event = {
        "id": id,
        "amount": str(amount_to_transfer),
        "destination_account": str(destination_account),
        "timestamp": event['timestamp'],
        "status": "200"
    }

    return transfer_request_event