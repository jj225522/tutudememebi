import requests
from config import config
from keywords import KEYWORDS

def enrich_tokens():
    enriched_tokens = {}
    headers = {
        "X-API-KEY": config["birdeye_api_key"]
    }

    for kw in KEYWORDS:
        # 使用Birdeye的token_search接口查找代币
        url = f"https://public-api.birdeye.so/public/token_search?query={kw}&chain=solana"
        try:
            res = requests.get(url, headers=headers)
            data = res.json()
            token = data["data"][0]  # 取搜索到的第一个代币
            enriched_tokens[kw] = {
                "price": token.get("price_usd", 0),
                "liquidity": token.get("liquidity_usd", 0),
                "is_new": token.get("is_new", False),
                "near_ath": token.get("all_time_high", 0) > 1.2 * token.get("price_usd", 0)  # 简单逻辑判断是否接近历史高点
            }
        except Exception as e:
            enriched_tokens[kw] = {
                "price": 0,
                "liquidity": 0,
                "is_new": False,
                "near_ath": False
            }
    return enriched_tokens
