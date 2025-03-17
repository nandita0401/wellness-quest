from fastapi import FastAPI
from app.routes import user_routes, mood_routes, quest_routes, suggestion_routes, recommendation
from app.models import recommendation_model as recommendation_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Wellness Quest API",
    description="AI-Powered Recommendations for Mental Well-being"
)

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],   # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],   # Allows all headers
)

# ✅ Include existing routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(mood_routes.router, prefix="/mood", tags=["Mood Tracking"])
app.include_router(quest_routes.router, prefix="/quests", tags=["Quests"])
app.include_router(suggestion_routes.router, prefix="/suggestions", tags=["Suggestions"])

# ✅ Register Wolfram API
app.include_router(recommendation.router, prefix="/recommendation", tags=["Recommendation"])

# ✅ Include AI-based recommendation routes
app.include_router(recommendation_model.router, prefix="/recommendation_model", tags=["AI Recommendation"])

@app.get("/")
async def root():
    return {"message": "Welcome to Wellness Quest AI API!"}
