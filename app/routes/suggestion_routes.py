from fastapi import APIRouter, HTTPException
from app.models.suggestion import Suggestion
from app.database import database
from datetime import datetime

router = APIRouter()

# ✅ Generate a new suggestion for the user
@router.post("/generate_suggestion")
async def generate_suggestion(suggestion: Suggestion):
    await database["suggestions"].insert_one(suggestion.dict())
    return {"message": "Suggestion created successfully"}

# ✅ Get all active suggestions for a user
@router.get("/get_suggestions/{user_id}")
async def get_suggestions(user_id: str):
    suggestions = await database["suggestions"].find({"user_id": user_id, "dismissed_at": None}).to_list(length=50)
    return {"suggestions": suggestions}

# ✅ Dismiss a suggestion (User doesn't want it)
@router.put("/dismiss_suggestion/{suggestion_id}")
async def dismiss_suggestion(suggestion_id: str):
    result = await database["suggestions"].update_one(
        {"_id": suggestion_id}, 
        {"$set": {"dismissed_at": datetime.utcnow()}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Suggestion not found")

    return {"message": "Suggestion dismissed"}

# ✅ Get dismissed suggestions (Optional: For analytics)
@router.get("/get_dismissed_suggestions/{user_id}")
async def get_dismissed_suggestions(user_id: str):
    suggestions = await database["suggestions"].find({"user_id": user_id, "dismissed_at": {"$ne": None}}).to_list(length=50)
    # Convert MongoDB ObjectId to string for JSON serialization
    for suggestion in suggestions:
        suggestion["_id"] = str(suggestion["_id"])

    return {"dismissed_suggestions": suggestions}
