from fastapi import APIRouter, HTTPException
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl

# ✅ Create an APIRouter instance
router = APIRouter()

@router.get("/", tags=["Recommendation"])
async def get_recommendation():
    return {"message": "Recommendation route is working!"}

@router.get("/wolfram-insights", tags=["Recommendation"])
async def get_wolfram_insights():
    """
    Runs the Wolfram Language script and fetches insights.
    """
    # ✅ Specify the correct Wolfram Kernel path
    kernel_path = "/usr/local/bin/WolframKernel"

    try:
        # ✅ Start a Wolfram session using the correct kernel path
        session = WolframLanguageSession(kernel_path)

        # ✅ Load and evaluate the Wolfram script
        result = session.evaluate(wl.Import("./app/models/WellnessQuest.nb"))

        # ✅ Close the session
        session.terminate()

        return {"status": "success", "data": result}

    except Exception as e:
        return {"error": f"Error running Wolfram script: {str(e)}"}
