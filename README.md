# redditscraperV2
updated and debugged scraper for reddit api that can proccess multiple threads in one run. 

**MAIN ISSUES**
Environment variables not loading correctly (I had a misnamed .env file — rookie mistake, I it redditcredentials.env instead of just ".env" )
NLTK’s vader_lexicon failing to download due to SSL certificate issues on macOS
Missing or improperly configured Reddit API credentials resulting in a MissingRequiredAttributeException from praw


**PROCESS**
Created a proper .env file in the project root.
Loaded it with dotenv (load_dotenv()).
Confirmed variables were accessible using os.getenv() debug prints.

2️⃣ NLTK Certificate Workaround
Verified the vader_lexicon was already in the local nltk_data folder.
Bypassed re-downloading by pre-checking the lexicon.
Documented potential macOS SSL issues so future users can either:
Manually download the lexicon.
Use nltk.data.path.append() to point to pre-downloaded NLTK data.

3️⃣ Multiple Post Scraping Upgrade
Enhanced the script to handle multiple Reddit post IDs instead of a single hard-coded one.
Added comment-by-comment sentiment analysis using VADER (Positive, Neutral, Negative).
Stored everything (including post IDs, comment IDs, sentiment scores, and categories) in a pandas DataFrame, saved as a timestamped CSV file.

4️⃣ Rate Limit Respect
Added time.sleep() pauses in the comment scraping loop to avoid hammering Reddit’s servers.
