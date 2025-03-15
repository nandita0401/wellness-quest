import pandas as pd
import numpy as np
import os
import joblib

# Collaborative Filtering Libraries
from surprise import SVD, Dataset, Reader
from surprise.model_selection import GridSearchCV, train_test_split as surprise_train_test_split

# XGBoost Libraries
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV as sklearn_GridSearchCV, train_test_split

# Define directory paths
dataset_dir = os.path.dirname(__file__)
model_dir = os.path.join(dataset_dir, "models")
os.makedirs(model_dir, exist_ok=True)  # Ensure models directory exists

### 🔹 Step 1: Train Optimized Collaborative Filtering Model (SVD) ###
def train_cf_model():
    print("🚀 Training Optimized Collaborative Filtering Model...")

    # Load Collaborative Filtering dataset
    cf_dataset_path = os.path.join(dataset_dir, "cf_training_data.csv")
    df_cf = pd.read_csv(cf_dataset_path)

    # Prepare data for Surprise library
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df_cf[['user_id', 'activity_id', 'rating']], reader)

    # Hyperparameter tuning for SVD
    param_grid = {
        "n_factors": [50, 100, 150],
        "n_epochs": [20, 30, 40],
        "lr_all": [0.002, 0.005, 0.01],
        "reg_all": [0.02, 0.05, 0.1]
    }

    gs = GridSearchCV(SVD, param_grid, measures=["rmse", "mae"], cv=3, n_jobs=-1)
    gs.fit(data)

    # Get best parameters
    best_params = gs.best_params["rmse"]
    print(f"Best SVD Parameters: {best_params}")

    # Train optimized SVD model
    model_cf = SVD(n_factors=best_params["n_factors"], n_epochs=best_params["n_epochs"],
                   lr_all=best_params["lr_all"], reg_all=best_params["reg_all"])

    trainset = data.build_full_trainset()
    model_cf.fit(trainset)

    # Save trained model
    cf_model_path = os.path.join(model_dir, "optimized_collaborative_filtering_model.joblib")
    joblib.dump(model_cf, cf_model_path)
    print(f"Optimized Collaborative Filtering Model Saved: {cf_model_path}")

### 🔹 Step 2: Train Optimized XGBoost Model (Emotion-Based Recommendations) ###
def train_xgb_model():
    print("🚀 Training Optimized XGBoost Model...")

    # Load XGBoost dataset
    xgb_dataset_path = os.path.join(dataset_dir, "xgb_training_data.csv")
    df_xgb = pd.read_csv(xgb_dataset_path)

    # Encode categorical variables
    label_encoders = {}
    for col in ['mood', 'recent_activity', 'suggested_activity']:
        label_encoders[col] = LabelEncoder()
        df_xgb[col] = label_encoders[col].fit_transform(df_xgb[col])

    # Save label encoders for future use
    for col, encoder in label_encoders.items():
        joblib.dump(encoder, os.path.join(model_dir, f"{col}_encoder.joblib"))

    # Prepare X and y
    X = df_xgb[['mood', 'recent_activity']]
    y = df_xgb['suggested_activity']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Hyperparameter tuning for XGBoost
    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [3, 5],
        "learning_rate": [0.01, 0.1],
        "subsample": [0.7, 1.0],
        "colsample_bytree": [0.7, 1.0]
    }

    grid_search = sklearn_GridSearchCV(xgb.XGBClassifier(), param_grid, scoring="accuracy", cv=3, verbose=1, n_jobs=4, pre_dispatch="2*n_jobs")
    grid_search.fit(X_train, y_train)

    # Get best parameters
    best_params = grid_search.best_params_
    print(f"Best XGBoost Parameters: {best_params}")

    # Train final XGBoost model with best parameters
    model_xgb = xgb.XGBClassifier(n_estimators=best_params["n_estimators"], max_depth=best_params["max_depth"],
                                  learning_rate=best_params["learning_rate"], subsample=best_params["subsample"],
                                  colsample_bytree=best_params["colsample_bytree"])
    model_xgb.fit(X_train, y_train)

    # Save trained model
    xgb_model_path = os.path.join(model_dir, "optimized_xgboost_model.joblib")
    joblib.dump(model_xgb, xgb_model_path)
    print(f"Optimized XGBoost Model Saved: {xgb_model_path}")

### 🔹 Run Both Training Functions ###
if __name__ == "__main__":
    print("Training AI Models...")
    train_cf_model()
    train_xgb_model()
    print("All Models Trained and Saved Successfully!")
