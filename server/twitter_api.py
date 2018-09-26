import json
import os
import twitter


api = None
authorized = False

def get_followers(user):
	authenticate()
	names = []
	followers = api.GetFollowers(screen_name=user)
	for follower in followers:
		names.append(follower.name)
	return names

# def get_user_tweets(user):

# def get_tweets(user):

def get_friends(user):
	authenticate()
	friends = api.GetFriends(screen_name=user)
	friend_names = []
	for friend in friends:
		friend_names.append(friend.name)
	return friend_names


def get_friend_num(user):
	authenticate()
	account = api.GetUser(screen_name=user)
	return account.friends_count


def authenticate():
	global authorized
	global api
	if not authorized:
		api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
                  consumer_secret=os.environ['CONSUMER_SECRET'],
                  access_token_key=os.environ['ACCESS_TOKEN'],
                  access_token_secret=os.environ['ACCESS_SECRET'],
                  sleep_on_rate_limit=True)
		authorized = True
		return
	else:
		return
