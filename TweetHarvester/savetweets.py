#==== header here ===================================================
# Team 16 - city: Atlanta
# Student number: 656982 | Student name: Zhenya Li    | Surname: Li 
# Student number: 616805 | Student name: Meng Li      | Surname: Li
# Student number: 650382 | Student name: Ming Yu      | Surname: Chang
# Student number: 548771 | Student name: Hao Duan     | Surname: Duan
# Student number: 629341 | Student name: Yu Sun       | Surname: Sun
# Student number: 705077 | Student name: Yuxiang Zhou | Surname: Zhou
# ===================================================================
from TweetStore import TweetStore
from TwitterAPI.TwitterAPI import TwitterAPI

city_bound_googleV3 = [-84.5518189, 33.648079, -84.289389,33.8876179]

chunks_bound = [[-84.5518189, 33.648079, -84.42060395, 33.76784845], \
                [-84.5518189, 33.76784845, -84.42060395, 33.8876179], \
                [-84.42060395, 33.648079, -84.289389, 33.76784845],\
                [-84.42060395, 33.76784845, -84.289389, 33.8876179]]

COUCH_DATABASE = 'test_db'
TWITTER_ENDPOINT = 'statuses/filter'
TWITTER_PARAMS = {'locations':chunks_bound[0]}

API_KEY = "lSjoTqZ4ofmtCr0uh7aJZRQcp"
API_SECRET = "qfkI0RjyOetHNDE6EJhojNlqRf4B7lbZj2rTQBmTZYHT9sRjlc"
ACCESS_TOKEN = "3186003008-eAzy3mSzxHRYuWzji65Xi0JrjTFqJTO81MU2cKK"
ACCESS_TOKEN_SECRET = "Rvvo931v0hbMyRX8sg8QG51cVlY8LQuij8zXuA9aP1hIh"

storage = TweetStore(COUCH_DATABASE)

api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


for item in api.request(TWITTER_ENDPOINT, TWITTER_PARAMS):
	if 'text' in item:
		print('%s -- %s\n' % (item['user']['screen_name'], item['text']))
		storage.save_tweet(item)
	elif 'message' in item:
		print('ERROR %s: %s\n' % (item['code'], item['message']))
