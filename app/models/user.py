from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schema
class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.utcnow()
