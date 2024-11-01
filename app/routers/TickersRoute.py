from fastapi import APIRouter, HTTPException

# Import the custom Pydantic typing models from schemas/PydanticSchemas
from app.schemas.PydanticSchemas import Ticker, TickerInput

# Some made-up ticker data in a dictionary
tickerDatabase = [
    {"ticker": "AAPL", "price":400},
    {"ticker": "MSFT", "price":200}
]

router = APIRouter()

# Get all the ticker data from the dictionary
@router.get("/tickers")
async def getAll() -> list[Ticker]:
    return [Ticker(**i) for i in tickerDatabase]

# Get specific ticker data from the dictionary
@router.get("/tickers/{inputTicker}")
async def getTickerData(inputTicker: str) -> Ticker:
    returnData = next((Ticker(**i) for i in tickerDatabase 
                        if i['ticker'].lower() == inputTicker.lower()), None)
    
    # If the ticker that was inputted is not found, raise a 404 Exception
    if returnData is None:
        raise HTTPException(status_code=404, detail="Ticker not found")
    
    return returnData