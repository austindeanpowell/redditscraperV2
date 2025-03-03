import os
import ssl
import certifi
import nltk
import praw
import warnings
from dotenv import load_dotenv

# Load Reddit credentials from .env file
load_dotenv()
 

# Force Python to use certifi for SSL verification
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Check NLTK data path to make sure it's seeing the correct folder
print("NLTK data paths:", nltk.data.path)

# Load VADER lexicon (if it's missing, try to download — otherwise just load from your existing nltk_data folder)
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
    print("VADER lexicon already exists!")
except LookupError:
    print("VADER lexicon not found, attempting download...")
    nltk.download('vader_lexicon')

# Silence any unnecessary warnings (optional)
warnings.filterwarnings("ignore", category=UserWarning)

# Print versions just to make sure your environment is good
print(f"nltk version: {nltk.__version__}")
print(f"praw version: {praw.__version__}")

# Example PRAW setup (you'll still need to check if your environment variables are set correctly)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

print("Reddit API setup completed (assuming credentials are correct).")