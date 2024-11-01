from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Testing the /tickers which should give all ticker data in the "database"
def test_get_all_tickers():
    response = client.get("/tickers")
    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0


# Testing the tickers/{ticker} which should show price data about the given ticker
def test_get_specific_ticker():
    response = client.get("/tickers/MSFT")
    data = response.json()

    assert response.status_code == 200
    assert data['ticker'] == "MSFT"
    assert data['price'] is not None


# Testing for when the user inputs a ticker that is not currently in the database
def test_get_unknown_ticker():
    response = client.get("/tickers/DOESNOTEXIST")

    assert response.status_code == 404
    assert response.json() == {"detail":"Ticker not found"}