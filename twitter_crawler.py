import requests
import json
import os
from keywords import KEYWORDS

# 读取 config_data.json 配置文件
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_data.json')
with open(config_path, 'r') as f:
    config = json.load(f)

def get_twitter_counts():
    headers = {
        "Authorization": f"Bearer {config['twitter_bearer_token']}"
    }
    twitter_counts = {}

    for kw in KEYWORDS:
        query = f"{kw} lang:en"
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=100"  # 确保没有无效字符
        try:
            res = requests.get(url, headers=headers)
            data = res.json()
            count = len(data.get("data", []))
        except Exception as e:
            count = 0
        twitter_counts[kw] = count
    return twitter_counts
