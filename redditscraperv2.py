import os
import time
import pandas as pd
import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import praw

# === Step 1: Load environment variables ===
print("Loading environment variables...")
load_dotenv()

client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

print(f"REDDIT_CLIENT_ID: {client_id}")
print(f"REDDIT_CLIENT_SECRET: {client_secret}")
print(f"REDDIT_USER_AGENT: {user_agent}")

# === Step 2: Ensure VADER lexicon is available ===
nltk_data_paths = nltk.data.path
print(f"NLTK data paths: {nltk_data_paths}")

try:
    nltk.download('vader_lexicon', quiet=False)
    print("✅ VADER lexicon downloaded (or already exists).")
except Exception as e:
    print(f"⚠️ Error downloading VADER lexicon: {e}")

sia = SentimentIntensityAnalyzer()

# === Step 3: Reddit API setup ===
try:
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    print("✅ Reddit API setup completed.")
except Exception as e:
    print(f"❌ Error initializing Reddit API: {e}")
    exit(1)

# === Step 4: Scrape comments and analyze sentiment ===
post_id = "kurhm6"  # You can change this as needed

print(f"Fetching submission: {post_id}")
submission = reddit.submission(id=post_id)

# Load all comments (including nested ones)
submission.comments.replace_more(limit=None)

comments_data = []

for comment in submission.comments.list():
    sentiment_score = sia.polarity_scores(comment.body)["compound"]

    if sentiment_score > 0.5:
        sentiment_category = "Positive"
    elif -0.5 <= sentiment_score <= 0.5:
        sentiment_category = "Neutral"
    else:
        sentiment_category = "Negative"

    comments_data.append([comment.id, comment.body, sentiment_score, sentiment_category])

    # Be polite to Reddit's servers 🫡
    time.sleep(1)

# === Step 5: Save results to CSV ===
df = pd.DataFrame(comments_data, columns=["Comment_ID", "Text", "Sentiment_Score", "Sentiment_Category"])

filename = f"reddit_sentiment_analysis_v2{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df.to_csv(filename, index=False)

print(f"✅ CSV file saved as: {filename}")
