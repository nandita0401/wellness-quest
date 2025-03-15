from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.database import database
from passlib.hash import bcrypt
from jose import jwt
import os
from app.config import SECRET_KEY

router = APIRouter()

# Hash password
def hash_password(password: str):
    return bcrypt.hash(password)

# Verify password
def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

# JWT Token generation
def create_jwt_token(email: str):
    payload = {"sub": email}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@router.post("/register")
async def register_user(user: User):
    existing_user = await database["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_password(user.password)
    user.password = hashed_password
    await database["users"].insert_one(user.dict())

    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(email: str, password: str):
    user = await database["users"].find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_jwt_token(email)
    return {"access_token": token}
