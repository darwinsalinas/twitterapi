from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {
        'info': 'Tweeter API with FastAPI',
        'version': '0.0.1'
    }
