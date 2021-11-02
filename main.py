from schemas.tweets import Tweet
from schemas.user import LoginUser


def print_hi(name):
    user = LoginUser(id=1, username='admin', password='12345678', email='asdasd@sdfs.com')
    tweet = Tweet(id=1, user_id=user.id, tweet_text='hola es mi tweet')
    print(user)
    print(tweet)
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
