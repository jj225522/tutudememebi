from telethon.sync import TelegramClient, events
import json
from config import config
from keywords import KEYWORDS
from collections import defaultdict

# 用你上传的 .session 文件
client = TelegramClient('meme', config["api_id"], config["api_hash"])

# 关键词频次计数
keyword_counter = defaultdict(int)

@client.on(events.NewMessage(chats=config["telegram_group_ids"]))
async def handler(event):
    text = event.message.message
    for keyword in KEYWORDS:
        if keyword.lower() in text.lower():
            keyword_counter[keyword] += 1

# 获取关键词频次
def get_telegram_counts():
    return dict(keyword_counter)

# 重置计数器
def reset_telegram_counts():
    keyword_counter.clear()

if __name__ == "__main__":
    print("启动 Telegram 监听器")
    client.start()
    client.run_until_disconnected()
