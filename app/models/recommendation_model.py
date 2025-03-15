from fastapi import APIRouter, HTTPException
import joblib
import numpy as np
import os
import pandas as pd

# ✅ Define FastAPI router
router = APIRouter()

# ✅ Define directory paths
model_dir = os.path.join(os.path.dirname(__file__), "models")

# ✅ Load trained models
cf_model_path = os.path.join(model_dir, "optimized_collaborative_filtering_model.joblib")
xgb_model_path = os.path.join(model_dir, "optimized_xgboost_model.joblib")

try:
    model_cf = joblib.load(cf_model_path)
    model_xgb = joblib.load(xgb_model_path)
except Exception as e:
    print(f"⚠️ Warning: Failed to load models: {e}")
    model_cf = None
    model_xgb = None

# ✅ Load label encoders for XGBoost
label_encoders = {}
for col in ["mood", "recent_activity", "suggested_activity"]:
    encoder_path = os.path.join(model_dir, f"{col}_encoder.joblib")
    try:
        label_encoders[col] = joblib.load(encoder_path)
    except Exception as e:
        print(f"⚠️ Warning: Failed to load encoder {col}: {e}")
        label_encoders[col] = None

csv_path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))

# ✅ Load datasets for better recommendations
cf_dataset_path = os.path.join(csv_path_dir, "cf_training_data.csv")
xgb_dataset_path = os.path.join(csv_path_dir, "xgb_training_data.csv")

df_cf = pd.read_csv(cf_dataset_path)
df_xgb = pd.read_csv(xgb_dataset_path)

### 🔹 Route 1: Predict Rating (Collaborative Filtering) ###
#The "Predicted Rating" refers to the score that the Collaborative 
# Filtering (SVD) model assigns to an activity for a given user. 
# This score estimates how much the user will like the activity 
# based on past interactions.
@router.get("/predict_rating")
async def predict_rating(user_id: int, activity: str):
    """Predict how much a user will like a given activity (scale: 1-5)."""
    try:
        if model_cf is None:
            raise HTTPException(status_code=500, detail="Collaborative Filtering model not loaded.")

        if activity not in df_cf["activity_id"].values:
            raise HTTPException(status_code=404, detail=f"Activity '{activity}' not found.")

        # Make prediction
        prediction = model_cf.predict(user_id, activity)
        return {
            "user_id": user_id,
            "activity": activity,
            "predicted_rating": round(prediction.est, 2),
            "rating_scale": "1 (Low) - 5 (High)"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


### 🔹 Route 2: Get Personalized Activity (XGBoost) ###
@router.get("/recommend_activity")
async def recommend_activity(mood: str, recent_activity: str):
    """Recommend an activity based on user's mood and recent activity."""
    try:
        if model_xgb is None:
            raise HTTPException(status_code=500, detail="XGBoost model not loaded.")

        if label_encoders["mood"] is None or label_encoders["recent_activity"] is None or label_encoders["suggested_activity"] is None:
            raise HTTPException(status_code=500, detail="Encoders not loaded correctly.")

        # Encode input using stored label encoders
        if mood not in label_encoders["mood"].classes_:
            raise HTTPException(status_code=400, detail="Invalid mood selection.")

        if recent_activity not in label_encoders["recent_activity"].classes_:
            raise HTTPException(status_code=400, detail="Invalid recent activity.")

        mood_encoded = label_encoders["mood"].transform([mood])[0]
        activity_encoded = label_encoders["recent_activity"].transform([recent_activity])[0]

        # Make prediction
        prediction = model_xgb.predict(np.array([[mood_encoded, activity_encoded]]))[0]

        # Decode predicted activity
        suggested_activity = label_encoders["suggested_activity"].inverse_transform([prediction])[0]

        return {
            "mood": mood,
            "recent_activity": recent_activity,
            "suggested_activity": suggested_activity
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
