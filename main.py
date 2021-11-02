from typing import List

from fastapi import FastAPI, Body

from schemas.tweets import Tweet

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
def create_tweet(tweet: Tweet = Body(...)):
    print(tweet)
    tweetsdb.append(tweet)
