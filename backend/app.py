from fastapi import FastAPI
from routes.flight_routes import router as flight_router
from routes.question_routes import router as question_router

app = FastAPI()
app.include_router(flight_router)
app.include_router(question_router)

@app.get("/")
def home():
    return {
        "message": "Flight AI Agent Backend Running"
    }


