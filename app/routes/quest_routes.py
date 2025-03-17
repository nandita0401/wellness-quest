from fastapi import APIRouter, HTTPException
from app.models.quest import Quest
from app.database import database

router = APIRouter()

@router.post("/create_quest")
async def create_quest(quest: Quest):
    await database["quests"].insert_one(quest.dict())
    return {"message": "Quest created successfully"}

@router.get("/get_quests/{user_id}")
async def get_quests(user_id: str):
    quests = await database["quests"].find({"user_id": user_id}).to_list(length=100)
    # Convert MongoDB ObjectId to string for JSON serialization
    for quest in quests:
        quest["_id"] = str(quest["_id"])

    return {"quests": quests}
