import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="0l2IygeV5HM-_WH47aoZOw",
    client_secret="iXpXAW3JZ_WmwJsBlXqmmrWFJ_TD_Q",
    user_agent="political_pulse"
)

def get_reddit_posts(subreddit, keyword, count=50):
    subreddit = reddit.subreddit(subreddit)
    posts = []
    
    for post in subreddit.search(keyword, limit=count):  
        posts.append(post.title + " " + post.selftext)   
    
    return posts

reddit_posts = get_reddit_posts("politics", "India", 50)

df_reddit = pd.DataFrame(reddit_posts, columns=["Post"])

print(df_reddit.head())