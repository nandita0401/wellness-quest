from fastapi import FastAPI
from app.routes import user_routes, mood_routes, quest_routes, suggestion_routes

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(mood_routes.router, prefix="/mood", tags=["Mood Tracking"])
app.include_router(quest_routes.router, prefix="/quests", tags=["Quests"])
app.include_router(suggestion_routes.router, prefix="/suggestions", tags=["Suggestions"])

@app.get("/")
def home():
    return {"message": "Welcome to Wellness Quest API"}
