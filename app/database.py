from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DB_NAME

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

# Create indexes for faster queries
async def init_db():
    await database["users"].create_index("email", unique=True)
    await database["daily_mood_logs"].create_index("user_id")
    await database["suggestions"].create_index("user_id")
    await database["user_quests"].create_index([("user_id", 1), ("quest_id", 1)], unique=True)
    await database["user_achievements"].create_index([("user_id", 1), ("achievement_id", 1)], unique=True)
