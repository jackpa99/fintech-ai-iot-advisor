from app.models import User, FinancialData

def get_financial_data(user: User) -> FinancialData:
    # This is a mock implementation. In a real application, you would fetch data from a database or external API.
    return FinancialData(
        total_assets=100000,
        total_liabilities=50000,
        net_worth=50000,
        monthly_income=5000,
        monthly_expenses=3000
    )