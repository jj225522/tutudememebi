import asyncio
import json
from telethon.sync import TelegramClient
from emotion_merger import merge_and_write

# 读取配置文件
with open('config.json') as f:
    config = json.load(f)

client = TelegramClient('meme', config["api_id"], config["api_hash"])

async def run():
    await client.start()
    print("🔁 开始运行监听器和合并器")
    while True:
        merge_and_write()
        await asyncio.sleep(180)  # 每3分钟更新一次

with client:
    client.loop.run_until_complete(run())
