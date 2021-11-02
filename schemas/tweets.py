from datetime import datetime

from pydantic import BaseModel, Field


class Tweet(BaseModel):
    id: int
    user_id: int = Field(example=1)
    tweet_text: str = Field(min_length=1, max_length=250)
    tweet_date: datetime = Field(default=datetime.now())


class CreateTweet(BaseModel):
    user_id: int = Field(gt=0, example=1)
    tweet_text: str = Field(min_length=1, max_length=250, example="Hello World")


class UpdateTweet(BaseModel):
    tweet_text: str = Field(min_length=1, max_length=250, example="New tweet text")
