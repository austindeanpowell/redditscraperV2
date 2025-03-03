import praw
import os
import time
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import datetime

# Load env variables (client_id, client_secret, user_agent)
load_dotenv()

# Download VADER lexicon if not already present
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Reddit API setup
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# 🔥 List of post IDs you want to scrape (add as many as you want)
post_ids = ["kurhm6", "wl5ft2","k4q7wl"]  # <<< Add all the post IDs here

# To hold all comments from all posts
all_comments_data = []

# Loop through each post and scrape comments
for post_id in post_ids:
    print(f"Scraping post: {post_id}")
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=None)  # Get all comments

    for comment in submission.comments.list():
        sentiment_score = sia.polarity_scores(comment.body)["compound"]

        # Categorize sentiment
        if sentiment_score > 0.5:
            sentiment_category = "Positive"
        elif -0.5 <= sentiment_score <= 0.5:
            sentiment_category = "Neutral"
        else:
            sentiment_category = "Negative"

        # Collect data
        all_comments_data.append([
            post_id,
            comment.id,
            comment.body,
            sentiment_score,
            sentiment_category
        ])
        time.sleep(1)  # Sleep to avoid rate limiting

# Convert to DataFrame
df = pd.DataFrame(all_comments_data, columns=["Post_ID", "Comment_ID", "Text", "Sentiment_Score", "Sentiment_Category"])

# Save to CSV with timestamp
filename = f"reddit_multi_post_sentiment_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False)

print(f"✅ CSV file saved: {filename}")
