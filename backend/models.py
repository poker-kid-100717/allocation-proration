from pydantic import BaseModel

class Investor(BaseModel):
    name: str
    requested_amount: float
    average_amount: float