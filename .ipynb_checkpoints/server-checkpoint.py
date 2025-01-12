from os import environ
from flask import Flask
import twitter_bot

app = Flask(__name__)

@app.route("/")
def home():
    twitter_bot.tweet_headline()
    return "Tweeting a headline..."

app.run(host='0.0.0.0', port=environ.get('PORT'))
