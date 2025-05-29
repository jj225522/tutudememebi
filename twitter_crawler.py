import requests
from config import config
from keywords import KEYWORDS

def get_twitter_counts():
    headers = {
        "Authorization": f"Bearer {config['twitter_bearer_token']}"
    }
    twitter_counts = {}

    for kw in KEYWORDS:
        query = f"{kw} lang:en"
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=100"
        try:
            res = requests.get(url, headers=headers)
            data = res.json()
            count = len(data.get("data", []))
        except Exception as e:
            count = 0
        twitter_counts[kw] = count
    return twitter_counts
