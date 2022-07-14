import tweepy
import sys


class MyStream(tweepy.Stream):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


consumer_key = "yD32tucpwHEAWCbRHE9SHo8YV"
consumer_secret = "KPMqzb81NfBsvhByIwH5NY5CcWACiCpiS1o4WYsCobywwh0ENE"
access_token = "1464596046630293509-24aqOFZCD4O06ZqiswDmTBfQLl1cJC"
access_token_secret = "YvRgfesHjRUjPgr1Aj4xEBypOwRVHqDvMukNs69TkU0ED"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

myStream = MyStream()
myStream = tweepy.Stream(auth=api.auth, listener=myStream)
myStream.filter(track=["news"])

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)
