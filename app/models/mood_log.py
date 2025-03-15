from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MoodLog(BaseModel):
    user_id: str
    mood: str
    notes: Optional[str] = None
    timestamp: datetime = datetime.utcnow()
