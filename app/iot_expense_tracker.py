import boto3
from app.models import User, Expense

iot_client = boto3.client('iot')

def get_expenses(user: User) -> list[Expense]:
    # This is a mock implementation. In a real application, you would fetch data from IoT Core.
    return [
        Expense(category="Groceries", amount=150.00, date="2024-08-20"),
        Expense(category="Utilities", amount=80.00, date="2024-08-19"),
        Expense(category="Entertainment", amount=50.00, date="2024-08-18")
    ]