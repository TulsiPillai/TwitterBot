CONSUMER_KEY = ""
CONSUMER_SECRET =  ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twts = api.search(q=”#games”, since_id =”hashmisrk”)
for s in twts:
sn = s.user.screen_name
print sn
m = “@%s Check out my new poll on games – https://twitter.com/PollStreak/status/674359048066600960&#8221; % (sn)
s = api.update_status(status=m)
