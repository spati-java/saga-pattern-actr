from datetime import datetime
from random import randint
from uuid import uuid4


def rollback_withdrawal(account_id, amount):
    # Implement the rollback logic for the withdrawal service here
    pass


def rollback_deposit(account_id, amount):
    # Implement the rollback logic for the deposit service here
    pass


def compensation(event, context):
    success = event['message']
    if success == 'Transaction Succeeded':
        return

    error = event['error']

    if error == "Failed to check balance":  # No further action is required
        return

    elif error == "Insufficient balance":  # No further action is required
        return

    elif error == "Failed to withdraw money":
        account_id = event['source_account']
        amount = event['amount']
        rollback_withdrawal(account_id, amount)

    elif error == "Failed to deposit money":
        account_id = event['destination_account']
        amount = event['amount']

    rollback_deposit(account_id, amount)


def lambda_handler(event, context):
    compensation(event, context)
