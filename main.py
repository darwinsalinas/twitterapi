from datetime import datetime
from typing import List

from fastapi import FastAPI, Body, Path, HTTPException

from schemas.tweets import Tweet, CreateTweet

app = FastAPI()

tweetsdb: List[Tweet] = []


@app.get('/about')
def about():
    return {
        'info': 'Tweeter API with FastAPI',
        'version': '0.0.1'
    }


@app.get('/')
def home():
    return {
        'data': tweetsdb,
        'total': len(tweetsdb)
    }


@app.post('/tweets')
def create_tweet(tweet: CreateTweet = Body(...)):
    tweet = Tweet(**tweet.dict(), id=len(tweetsdb) + 1, tweet_date=datetime.now())
    tweetsdb.append(tweet)


@app.delete('/tweets/{model_id}')
def delete_tweet(model_id: int = Path(..., ge=1)):
    tweet = list(filter(lambda t: t.id == model_id, tweetsdb))
    if tweet:
        tweetsdb.remove(tweet[0])
    else:
        raise HTTPException(status_code=404, detail='Tweet not found')
    return {
        'data': tweetsdb,
        'total': len(tweetsdb)
    }
