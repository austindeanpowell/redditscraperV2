import os
import ssl
import nltk
import warnings
from dotenv import load_dotenv
import praw

# ------------------------------
# 🪄 Fix SSL / NLTK issues for Mac
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# 🔧 Manually add your nltk_data path if needed
nltk.data.path.append("/Users/austinpowell/nltk_data")

# ------------------------------
# 🛠️ Load environment variables
print("Loading environment variables...")
load_dotenv()

# Debugging check - make sure vars are loading
print("REDDIT_CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
print("REDDIT_CLIENT_SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))
print("REDDIT_USER_AGENT:", os.getenv("REDDIT_USER_AGENT"))

# ------------------------------
# 🔬 Optional: Download VADER (shouldn't actually need it if you already have it)
try:
    nltk.download('vader_lexicon')
    print("VADER lexicon downloaded (or already exists).")
except Exception as e:
    print(f"VADER download error: {e}")

# ------------------------------
# 💻 Set up Reddit API (PRAW)
try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    print("✅ Reddit API setup completed.")
except Exception as e:
    print(f"❌ Reddit API setup failed: {e}")
    raise

# ------------------------------
# 🎉 Example usage (fetching comments or whatever you do next)
print("\nAll systems go, baby! Ready to scrape Reddit 🚀")
