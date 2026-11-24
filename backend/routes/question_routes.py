from fastapi import APIRouter
from pydantic import BaseModel
from services.question_service import extract_callsign
from services.opensky_service import get_flight_by_callsign

router =APIRouter()

class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
async def ask(request: QuestionRequest):
    callsign= extract_callsign(request.question)

    if callsign is None:
        return {
            "message": "I couldn't identify a flight callsign."
        }

    flight_data= await get_flight_by_callsign(callsign)

    if flight_data is None:
        return {
            "callsign" : callsign,
            "message" :"Flight not found"
        }


    return {
        "question" : request.question,
        
        "flight" : flight_data
    }