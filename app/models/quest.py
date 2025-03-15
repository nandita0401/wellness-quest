from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Quest(BaseModel):
    user_id: str
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.utcnow()
