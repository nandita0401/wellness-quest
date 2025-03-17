from fastapi import APIRouter
from app.models.mood_log import MoodLog
from app.database import database

router = APIRouter()

# ✅ Log Mood (No Validation Needed)
@router.post("/log_mood")
async def log_mood(mood: MoodLog):
    await database["daily_mood_logs"].insert_one(mood.dict())
    return {"message": "Mood logged successfully"}

# ✅ Get Mood Logs for a User
@router.get("/get_mood_logs/{user_id}")
async def get_mood_logs(user_id: str):
    logs = await database["daily_mood_logs"].find({"user_id": user_id}).to_list(length=100)
    # Convert MongoDB ObjectId to string for JSON serialization
    for log in logs:
        log["_id"] = str(log["_id"])
        
    return {"mood_logs": logs}

# ✅ Get List of Mood Categories (For Frontend Use)
@router.get("/get_mood_categories")
async def get_mood_categories():
    return {
        "mood_categories": [
            "Anxiety/Stress", "Sadness/Despair", "Happiness/Joy", "Disappointment/Regret",
            "Shame/Guilt", "Pride/Confidence", "Comparison/Social Pressure", "Empathy/Compassion",
            "Anger/Resentment", "Curiosity/Awe", "Belonging/Connection", "Nostalgia/Irony", "Love/Trust Issues"
        ]
    }