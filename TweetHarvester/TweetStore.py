#==== header here ===================================================
# Team 16 - city: Atlanta
# Student number: 656982 | Student name: Zhenya Li    | Surname: Li 
# Student number: 616805 | Student name: Meng Li      | Surname: Li
# Student number: 650382 | Student name: Ming Yu      | Surname: Chang
# Student number: 548771 | Student name: Hao Duan     | Surname: Duan
# Student number: 629341 | Student name: Yu Sun       | Surname: Sun
# Student number: 705077 | Student name: Yuxiang Zhou | Surname: Zhou
# ===================================================================
import couchdb
import couchdb.design

USERNAME = ''
PASSWORD = ''

class TweetStore(object):
	#def __init__(self, dbname, url=COUCH_SERVER):
	def __init__(self, dbname, url):
		try:
			self.server = couchdb.Server(url)
			self.db = self.server.create(dbname)
			self._create_views()
		except couchdb.http.PreconditionFailed:
			self.db = self.server[dbname]

	def _create_views(self):
		count_map = 'function(doc) { emit(doc.id, 1); }'
		count_reduce = 'function(keys, values) { return sum(values); }'
		view = couchdb.design.ViewDefinition('twitter', 'count_tweets', count_map, reduce_fun=count_reduce)
		view.sync(self.db)

		get_tweets = 'function(doc) { emit(("0000000000000000000"+doc.id).slice(-19), doc); }'
		view = couchdb.design.ViewDefinition('twitter', 'get_tweets', get_tweets)
		view.sync(self.db)

	def save_tweet(self, tw):
		tw['_id'] = tw['id_str']
		try:
			self.db.save(tw)
		except Exception:
			print "Duplication file_to_db.py"
			pass

	def count_tweets(self):
		for doc in self.db.view('twitter/count_tweets'):
			return doc.value

	def get_tweets(self):
		return self.db.view('twitter/get_tweets')
