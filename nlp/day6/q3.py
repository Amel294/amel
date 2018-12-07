import tweepy
consumer_key = '0htEpfdbFuqgCvxrRXVFHYXGc'
consumer_secret = 'C6tFvHVT1MsH7YYrMqIxrdclwFECMGLhTQB3DMSBxZZETRAROu'

access_token = '199500984-5DaTlHtNGzb6DiDGtHBR0xrWgQiXg2YblkO9Mfd5'
access_token_secret = 'FyuaL0NGxNvHNoBFr9tM6q2mwMjranonSZbA5BDTH11tg'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets=api.user_timeline(screen_name='FIFAcom')
pos=0
neg=0
neu=0
for tweet in public tweets:
	t1=TextBlob(tweet.text)
	if t1.sentiment.polarity>0:
		print("Positive")
		pos=pos+1
	if t1.sentiment.polarity<0:
                print("Negative")
		neg=neg+1
        if t1.sentiment.polarity>0:
                print("Neutral")
		neu=neu+1
print("Positive"
