# main entry point

# Step1: Setup FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app=FastAPI()

# Step2: Receive and validate request from Frontend
class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask():
    #inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}