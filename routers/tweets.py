from datetime import datetime
from typing import List

from fastapi import APIRouter, Body, Path, HTTPException

from database.memorydb import tweetsdb
from schemas.tweets import CreateTweet, Tweet, UpdateTweet

router = APIRouter()


@router.post('/tweets')
def create_tweet(tweet: CreateTweet = Body(...)):
    tweet = Tweet(**tweet.dict(), id=len(tweetsdb) + 1, tweet_date=datetime.now())
    tweetsdb.append(tweet)

    return {
        'data': tweet,
        'total': len(tweetsdb),
        'message': 'Successfully created'
    }


@router.delete('/tweets/{model_id}')
def delete_tweet(model_id: int = Path(..., ge=1, example=1)):
    tweet = filter_tweets_by_id(model_id)
    if tweet:
        tweetsdb.remove(tweet[0])
    else:
        raise HTTPException(status_code=404, detail='Tweet not found')
    return {
        'data': tweet,
        'total': len(tweetsdb),
        'message': 'Successfully deleted'
    }


@router.get('/tweets/{model_id}')
def show_tweet(model_id: int = Path(..., ge=1, example=1)):
    tweet = filter_tweets_by_id(model_id)

    if not tweet:
        raise HTTPException(status_code=404, detail='Tweet not found')

    return {
        'data': tweet[0],
        'total': 1,
        'message': 'Success'
    }


@router.put('/tweets/{model_id}')
def update_tweet(model_id: int = Path(..., ge=1, example=1), tweet: UpdateTweet = Body(...)):
    tweet_in_db = filter_tweets_by_id(model_id)

    if not tweet_in_db:
        raise HTTPException(status_code=404, detail='Tweet not found')

    tweet_in_db[0].tweet_text = tweet.tweet_text

    return {
        'data': tweet_in_db[0],
        'total': 1,
        'message': 'Successfully updated'
    }


def filter_tweets_by_id(model_id: int) -> List[Tweet]:
    return list(filter(lambda t: t.id == model_id, tweetsdb))
