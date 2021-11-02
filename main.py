from fastapi import FastAPI

from database.memorydb import tweetsdb

from routers import tweets
app = FastAPI()

app.include_router(tweets.router, tags=["Tweets"])


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
