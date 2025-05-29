import asyncio
import json
from telethon.sync import TelegramClient
from emotion_merger import merge_and_write

# 读取 config.json 配置文件
with open('config.json', 'r') as f:
    config = json.load(f)

# 使用配置文件中的 api_id 和 api_hash 创建 Telegram 客户端
client = TelegramClient('meme', config["api_id"], config["api_hash"])

async def run():
    # 启动 Telegram 客户端
    await client.start()
    print("🔁 开始运行监听器和合并器")
    
    # 每 3 分钟更新一次数据
    while True:
        merge_and_write()
        await asyncio.sleep(180)  # 每3分钟更新一次

# 启动客户端并运行
with client:
    client.loop.run_until_complete(run())
