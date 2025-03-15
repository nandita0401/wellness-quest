import pandas as pd
import numpy as np
import os
import joblib

# Collaborative Filtering Libraries
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

# XGBoost Libraries
import xgboost as xgb

# Define directory paths
dataset_dir = os.path.dirname(__file__)
model_dir = os.path.join(dataset_dir, "models")

# Load trained models
cf_model_path = os.path.join(model_dir, "optimized_collaborative_filtering_model.joblib")
xgb_model_path = os.path.join(model_dir, "optimized_xgboost_model.joblib")

model_cf = joblib.load(cf_model_path)
model_xgb = joblib.load(xgb_model_path)

print("Models Loaded Successfully!")

# Load Datasets for Testing
cf_dataset_path = os.path.join(dataset_dir, "cf_training_data.csv")
xgb_dataset_path = os.path.join(dataset_dir, "xgb_training_data.csv")

df_cf = pd.read_csv(cf_dataset_path)
df_xgb = pd.read_csv(xgb_dataset_path)

# Load Label Encoders for XGBoost
label_encoders = {}
for col in ["mood", "recent_activity", "suggested_activity"]:
    label_encoders[col] = joblib.load(os.path.join(model_dir, f"{col}_encoder.joblib"))

### 🔹 Test Collaborative Filtering Model (SVD) ###
def test_cf_model(user_id, activity_id):
    """Predict rating for a given user and activity using Collaborative Filtering."""
    print(f"\n🔍 Testing Collaborative Filtering Model for User {user_id} & Activity {activity_id}")

    # Make prediction
    prediction = model_cf.predict(user_id, activity_id)

    #The "Predicted Rating" refers to the score that the 
    # Collaborative Filtering (SVD) model assigns to an 
    # activity for a given user. This score estimates how 
    # much the user will like the activity based on past interactions.

    print(f"Predicted Rating: {prediction.est:.2f} (Scale: 1-5)")
    return prediction.est

### 🔹 Test XGBoost Model (Emotion-Based Recommendations) ###
def test_xgb_model(mood, recent_activity):
    """Predict suggested activity based on mood and recent activity."""
    print(f"\nTesting XGBoost Model for Mood: {mood} | Recent Activity: {recent_activity}")

    # Encode input using stored label encoders
    mood_encoded = label_encoders["mood"].transform([mood])[0]
    activity_encoded = label_encoders["recent_activity"].transform([recent_activity])[0]

    # Make prediction
    prediction = model_xgb.predict(np.array([[mood_encoded, activity_encoded]]))[0]

    # Decode suggested activity
    suggested_activity = label_encoders["suggested_activity"].inverse_transform([prediction])[0]

    print(f"Suggested Activity: {suggested_activity}")
    return suggested_activity

### 🔹 Run Tests ###
if __name__ == "__main__":
    print("\nRunning Model Tests...")

    # Select a random user & activity for testing Collaborative Filtering
    test_user = int(df_cf["user_id"].sample().values[0])
    test_activity = df_cf["activity_id"].sample().values[0]
    test_cf_model(test_user, test_activity)

    # Select a random mood & activity for testing XGBoost Model
    test_mood = df_xgb["mood"].sample().values[0]
    test_recent_activity = df_xgb["recent_activity"].sample().values[0]
    test_xgb_model(test_mood, test_recent_activity)

    print("\nModel Testing Completed!")
