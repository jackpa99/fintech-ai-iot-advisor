from pydantic import BaseModel
from typing import Dict, List

class User(BaseModel):
    username: str

class FinancialData(BaseModel):
    total_assets: float
    total_liabilities: float
    net_worth: float
    monthly_income: float
    monthly_expenses: float

class InvestmentAdvice(BaseModel):
    risk_profile: str
    recommended_asset_allocation: Dict[str, int]
    specific_recommendations: List[str]

class Expense(BaseModel):
    category: str
    amount: float
    date: str