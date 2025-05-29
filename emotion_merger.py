from telegram_listener import get_telegram_counts, reset_telegram_counts
from twitter_crawler import get_twitter_counts
from birdeye_enricher import enrich_tokens
import json
import time

def merge_and_write():
    twitter = get_twitter_counts()
    telegram = get_telegram_counts()
    birdeye = enrich_tokens()

    merged = {}
    for k in set(twitter) | set(telegram) | set(birdeye):
        merged[k] = {
            "twitter": twitter.get(k, 0),
            "telegram": telegram.get(k, 0),
            "price": birdeye.get(k, {}).get("price", 0),
            "liquidity": birdeye.get(k, {}).get("liquidity", 0),
            "is_new": birdeye.get(k, {}).get("is_new", False),
            "near_ath": birdeye.get(k, {}).get("near_ath", False)
        }

    with open("emotion_enriched.json", "w") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    reset_telegram_counts()
    print("✅ emotion_enriched.json 已更新：", time.strftime("%H:%M:%S"))

if __name__ == "__main__":
    merge_and_write()
