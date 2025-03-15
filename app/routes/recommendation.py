from fastapi import APIRouter

# ✅ Create an APIRouter instance
router = APIRouter()

@router.get("/", tags=["Recommendation"])
async def get_recommendation():
    return {"message": "Recommendation route is working!"}
