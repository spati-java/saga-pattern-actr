from datetime import datetime
from random import randint
from uuid import uuid4


def lambda_handler(event, context):
    """Sample Lambda function which mocks the operation of selling a random number
    of shares for a stock.

    For demonstration purposes, this Lambda function does not actually perform any 
    actual transactions. It simply returns a mocked result.

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: Object containing details of the stock selling transaction
    """
    # Get the price of the stock provided as input
    amount_to_transfer = event["amount_to_transfer"]
    # Mocked result of a stock selling transaction
    transaction_result = {
        "id": str(uuid4()),  # Unique ID for the transaction
        "price": str(amount_to_transfer),  # Price of each share
        "type": "sell",  # Type of transaction (buy/sell)
        "qty": str(
            randint(1, 10)
        ),  # Number of shares bought/sold (We are mocking this as a random integer between 1 and 10)
        "timestamp": datetime.now().isoformat(),  # Timestamp of the when the transaction was completed
    }
    return transaction_result
