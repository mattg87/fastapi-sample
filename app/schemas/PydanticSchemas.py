from enum import Enum
from pydantic import BaseModel

class Ticker(BaseModel):
    ticker: str
    price: int

class TickerInput(BaseModel):
    ticker: str