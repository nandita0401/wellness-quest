from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Suggestion(BaseModel):
    user_id: str
    suggestion_text: str
    generated_at: datetime = datetime.utcnow()
    dismissed_at: Optional[datetime] = None  # Null if not dismissed
