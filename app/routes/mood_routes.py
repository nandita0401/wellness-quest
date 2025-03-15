from fastapi import APIRouter, HTTPException
from app.models.mood_log import MoodLog
from app.database import database

router = APIRouter()

@router.post("/log_mood")
async def log_mood(mood: MoodLog):
    await database["mood_logs"].insert_one(mood.dict())
    return {"message": "Mood logged successfully"}

@router.get("/get_mood_logs/{user_id}")
async def get_mood_logs(user_id: str):
    logs = await database["mood_logs"].find({"user_id": user_id}).to_list(length=100)
    return {"mood_logs": logs}
