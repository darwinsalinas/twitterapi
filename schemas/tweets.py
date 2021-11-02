from datetime import datetime

from pydantic import BaseModel, Field


class Tweet(BaseModel):
    id: int
    user_id: int
    tweet_text: str = Field(min_length=1, max_length=250)
    tweet_date: datetime = Field(default=datetime.now())
