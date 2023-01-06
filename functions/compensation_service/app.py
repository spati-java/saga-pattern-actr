from datetime import datetime
from random import randint
from uuid import uuid4
import json


def rollback_withdrawal(account_id, amount):
    return 'Failed to deposit so money successfully return to the source-account'


def rollback_deposit(account_id, amount):
    # Nothing to do since deposit was not success
    # But can do things in case deposit was success but some other reasons the deposit needs to be rolled back
    pass


def compensation(event, context):
    error = event['error']['Cause']
    error_json = json.loads(error)
    message = error_json['errorMessage']

    if message == "Failed to check balance":  # No further action is required
        return

    elif error == "Insufficient balance":  # No further action is required
        message

    elif message == "Failed to withdraw money":
        account_id = "23920983"
        amount = event['amount']
        rollback_withdrawal(account_id, amount)

    elif message == "Failed to deposit money":
        account_id = "23920983"
        amount = event['amount']
        rollback_withdrawal(account_id, amount)


def lambda_handler(event, context):
    compensation(event, context)
