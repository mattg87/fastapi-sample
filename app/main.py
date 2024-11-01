from fastapi import FastAPI, HTTPException
from app.routers import TickersRoute

from pydantic import BaseModel

# Import the custom Pydantic typing models from schemas/PydanticSchemas
from app.schemas.PydanticSchemas import Ticker

app = FastAPI()

# Some made-up ticker data in a dictionary
tickerDatabase = [
    {"ticker": "AAPL", "price":400},
    {"ticker": "MSFT", "price":200}
]

app = FastAPI()
app.include_router(TickersRoute.router)

# Root of the app
@app.get("/")
async def root():
    return {"message": "Hi! Thanks for running this little project!"}

# Get all the ticker data from the dictionary
@app.get("/all")
async def getAll() -> list[Ticker]:
    return [Ticker(**i) for i in tickerDatabase]

# Get specific ticker data from the dictionary
@app.get("/tickers/{ticker}")
async def getTickerData(inputTicker: str) -> Ticker:
    returnData = next((Ticker(**i) for i in tickerDatabase 
                        if i['ticker'] == inputTicker), None)
    
    # If the ticker that was inputted is not found, raise a 404 Exception
    if returnData is None:
        raise HTTPException(status_code=404, detail="Ticker not found")
    
    return returnData