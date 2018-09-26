# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import os

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)


def get_tweets():
    # Initiate the connection to Twitter Streaming API
    twitter_stream = TwitterStream(auth=oauth)

    # Get a sample of the public data following through Twitter
    iterator = twitter_stream.statuses.sample()

    tweets = []

    # Print each tweet in the stream to the screen 
    # Here we set it to stop after getting 1000 tweets. 
    # You don't have to set it to stop, but can continue running 
    # the Twitter API to collect data for days or even longer. 
    tweet_count = 20
    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter 
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        tweets.append(json.dumps(tweet))  
        
        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)
           
        if tweet_count <= 0:
            break 
    return tweets


def get_followers(user):
    followers = twitter.followers.ids(screen_name=user)
    print(followers)
    return followers

def get_user_tweets(user):
    tweets = twitter.statuses.user_timeline(screen_name=user)
    print(tweets)
    return tweets




