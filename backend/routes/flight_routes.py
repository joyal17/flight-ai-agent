from fastapi import APIRouter

from services.opensky_service import (
    get_all_flights,
    get_flight_by_callsign
)

router = APIRouter()

@router.get("/flights")
async def flights():
    return await get_all_flights()


@router.get("/flight/{callsign}")
async def flight(callsign: str):
    return await get_flight_by_callsign(callsign)