import os  # Step 1: Import the os module

# Step 2: Get values from environment variables
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Only if you're using a news API

# Now you can use these keys when connecting to APIs
