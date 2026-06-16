from fastapi import FastAPI
from services.opensky_service import (get_all_flights , get_flight_by_callsign)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Flight AI Agent Backend Running"}

@app.get("/flights")
async def flights():
    return await get_all_flights()

@app.get("/flight/{callsign}")
async def flight(callsign: str):
    return await get_flight_by_callsign(callsign)

