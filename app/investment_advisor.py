from app.models import User, InvestmentAdvice

def get_investment_advice(user: User) -> InvestmentAdvice:
    # This is a mock implementation. In a real application, you would use a machine learning model to generate advice.
    return InvestmentAdvice(
        risk_profile="Moderate",
        recommended_asset_allocation={
            "Stocks": 60,
            "Bonds": 30,
            "Cash": 10
        },
        specific_recommendations=[
            "Consider investing in low-cost index funds",
            "Diversify your portfolio across different sectors",
            "Rebalance your portfolio annually"
        ]
    )