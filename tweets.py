import os
import tweepy
import requests
from dotenv import load_dotenv
from tweepy import OAuth1UserHandler


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def tweet_dog_fact(tweepy_client):
   dog_facts_api = 'http://dog-api.kinduff.com/api/facts'

   print('fetching dog facts...')
   res = requests.get(dog_facts_api)

   print('tweeting a dog fact...')
   tweet_text = res.json()['facts'][0]
   tweepy_client.create_tweet(text=tweet_text)


# # Authenticate with OAuth 1.0a
# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object
# api = tweepy.API(auth)
tweet_dog_fact(client)

