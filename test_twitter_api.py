import os
import requests
from dotenv import load_dotenv

# Load .env file to securely fetch the Bearer Token
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def search_recent_tweets(query):
    """Fetch recent tweets based on a query."""
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "query": query,       # Your search term (e.g., trending topic)
        "max_results": 10     # Number of tweets to fetch (max: 100 per request)
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        tweets = response.json()
        print(f"\nRecent Tweets for '{query}':")
        for tweet in tweets["data"]:
            print(f"- {tweet['text']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # Example search term: Replace with any keyword or hashtag
    trending_topic = input("Enter a topic to search tweets for: ")
    search_recent_tweets(trending_topic)

