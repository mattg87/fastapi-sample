from fastapi import FastAPI, HTTPException
from app.routers import TickersRoute

app = FastAPI()
app.include_router(TickersRoute.router)

# Root of the app
@app.get("/")
async def root():
    return {"message": "Hi! Thanks for running this little project!"}