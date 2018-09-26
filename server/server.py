import random
import json
from flask import Flask, render_template, Response, abort, request
import twitter_api

app = Flask(__name__, static_folder='../static', template_folder='../templates/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
	res = json.dumps("hello")
	r = Response(res, status=200)
	return r

@app.route("/followers", methods=['POST'])
def followers():
	print(request.values)
	user = request.values.get('user')
	try:
		print(user)
		followers = twitter_api.get_followers(user)
		res = json.dumps(followers)
		r = Response(res, status=200)
		return r
	except Exception as e:
		print(e)
		abort(429)

@app.route("/friends", methods=['POST'])
def friends():
	user = request.values.get('friend')
	try:
		friends = twitter_api.get_friends(user)
		res = json.dumps(friends)
		r = Response(res, status=200)
		return r
	except Exception as e:
		print(e)
		abort(429)

@app.route("/friend_number", methods=['POST'])
def friend_number():
	user = request.values.get('name')
	try:
		friend_num = twitter_api.get_friend_num(user)
		res = json.dumps(friend_num)
		r = Response(res, status=200)
		return r
	except Exception as e:
		print(e)
		abort(429)

@app.route("/common", methods=['POST'])
def find_common():
	friends = json.loads(request.values.get('friends'))
	print("finding common of {friends}".format(friends=friends))
	recs = []
	try:
		for friend in friends:
			associations = twitter_api.get_friends(friend)
			recs.append(associations)
		result = set(recs[0])
		for s in recs[1:]:
			result.intersection_update(s)
		res = json.dumps(list(result))
		r = Response(res, status=200)
		return r
	except Exception as e:
		print(e)
		abort(429)

@app.route("/user_tweets", methods=['POST'])
def user_tweets():
	user = request.values.get('user')
	try:
		tweets = twitter_api.get_user_tweets(user)
	except Exception as e:
		print(e)
		abort(429)
	res = json.dumps(tweets)
	r = Response(res, status=200)
	return r

if __name__ == '__main__':
    app.run(debug=True)
