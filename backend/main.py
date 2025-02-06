from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from models import Investor  # Import Investor from models.py
from proration import prorate_allocation

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use more restrictive CORS in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the Investor class to be used in request validation
class Investor(BaseModel):
    name: str
    requested_amount: float
    average_amount: float

# Define the request body for proration
class ProrationRequest(BaseModel):
    allocation_amount: float
    investor_amounts: List[Investor]

# Test route to ensure server is running (optional but useful for debugging)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Allocation Proration Tool API!"}

# Request body model for Proration
class ProrationRequest(BaseModel):
    allocation_amount: float
    investor_amounts: List[Investor]

@app.post("/prorate")
def prorate(request: ProrationRequest):
    result = prorate_allocation(request.allocation_amount, request.investor_amounts)
    return result