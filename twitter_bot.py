import json, random, tweepy, credentials, sys
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def get_headlines():
    with open('headlines.json') as f:
        headlines = json.load(f)
    return headlines['headlines']

def get_random_headline():
    headlines = get_headlines()
    random_headline = random.choice(headlines)
    return random_headline['headline']

def post_headline():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    headline = get_random_headline()
    api.update_status(headline)
    
if __name__ == "__main__":
    post_headline()