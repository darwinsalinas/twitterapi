from datetime import datetime
from typing import List

from fastapi import FastAPI, Body, Path, HTTPException

from schemas.tweets import Tweet, CreateTweet, UpdateTweet

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
def delete_tweet(model_id: int = Path(..., ge=1, example=1)):
    tweet = filter_tweets_by_id(model_id)
    if tweet:
        tweetsdb.remove(tweet[0])
    else:
        raise HTTPException(status_code=404, detail='Tweet not found')
    return {
        'data': tweetsdb,
        'total': len(tweetsdb)
    }


@app.get('/tweets/{model_id}')
def show_tweet(model_id: int = Path(..., ge=1, example=1)):
    tweet = filter_tweets_by_id(model_id)

    if not tweet:
        raise HTTPException(status_code=404, detail='Tweet not found')

    return {
        'data': tweet[0],
        'total': 1
    }


@app.put('/tweets/{model_id}')
def update_tweet(model_id: int = Path(..., ge=1, example=1), tweet: UpdateTweet = Body(...)):
    tweet_in_db = filter_tweets_by_id(model_id)

    if not tweet_in_db:
        raise HTTPException(status_code=404, detail='Tweet not found')

    tweet_in_db[0].tweet_text = tweet.tweet_text

    return {
        'data': tweet_in_db[0],
        'total': 1
    }


def filter_tweets_by_id(model_id: int) -> List[Tweet]:
    return list(filter(lambda t: t.id == model_id, tweetsdb))
