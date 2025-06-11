import tweepy
import pandas as pd

API_KEY = "H3ZXoFlWowClLBTleajWF62cI"
API_SECRET = "edxvkpvYNtYIS6AOwpEUU3J5YZywDYReUuemZFT58oeXvS2QRE"
ACCESS_TOKEN = "1897956794003066881-G0TwAJbrenxUpBOWZPxFA9qdO8KEiI"
ACCESS_SECRET = "SAAKoBL3NHteEjDTMzARoy8aFTLuMxO6hXEonkoo1cHzc"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJkezwEAAAAAlpBiKQoq4VH12pdNY%2FpSs6Xw7hM%3DDIuhHUZm1WMQN3Ew4AaxPnkgRIicgwdnUUoXnHFmorKokuMZxY"


client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_tweets_v2(keyword, count=10):
    tweets = client.search_recent_tweets(query=keyword, tweet_fields=["created_at"], max_results=count)
    return [tweet.text for tweet in tweets.data] if tweets.data else []

tweets = get_tweets_v2("politics", 10)
df_twitter = pd.DataFrame(tweets, columns=["Tweet"])
print(df_twitter.head())