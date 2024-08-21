from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse
from app.auth import auth_user_facebook, get_current_user
from app.financial_data import get_financial_data
from app.investment_advisor import get_investment_advice
from app.iot_expense_tracker import get_expenses
from app.models import User, FinancialData, InvestmentAdvice, Expense
from app.kafka_client import KafkaClient
from app.pinpoint_client import PinpointClient

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

kafka_client = KafkaClient()
pinpoint_client = PinpointClient()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("login.html", "r") as f:
        return f.read()
    
@app.post("/token")
async def login(fb_access_token: str):
    user = auth_user_facebook(fb_access_token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Facebook token")
    return {"access_token": fb_access_token, "token_type": "bearer"}


@app.get("/financial-data", response_model=FinancialData)
async def financial_data(current_user: User = Depends(get_current_user)):
    return get_financial_data(current_user)

@app.get("/investment-advice", response_model=InvestmentAdvice)
async def investment_advice(current_user: User = Depends(get_current_user)):
    return get_investment_advice(current_user)

@app.get("/expenses", response_model=list[Expense])
async def expenses(current_user: User = Depends(get_current_user)):
    return get_expenses(current_user)

@app.on_event("startup")
async def startup_event():
    kafka_client.start()

@app.on_event("shutdown")
async def shutdown_event():
    kafka_client.stop()