from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData

app = FastAPI()

taxi_data = TaxiData()

@app.get("/taxi/")
async def read_taxi_data():
    return taxi_data.to_json()
