import os
from dotenv import load_dotenv

# Load Reddit credentials from .env file
load_dotenv()

# Check if they were loaded
print("CLIENT ID:", os.getenv("REDDIT_CLIENT_ID"))
print("CLIENT SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))
print("USER AGENT:", os.getenv("REDDIT_USER_AGENT"))