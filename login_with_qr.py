import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 23738275  # 替换为你的 API ID
api_hash = '13360c57615d2f14ee7f727170bb761'  # 替换为你的 API Hash

async def main():
    print("📱 生成二维码中，请用 Telegram 扫码登录")
    
    # 使用 StringSession 来存储会话
    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        qr_code = await client.qr_login()
        
        # 显示二维码
        qr_code.show_qr()
        print("📷 打开 Telegram 手机端，扫码以下二维码 👇")

        await qr_code.wait()  # 等待扫码完成
        print("✅ 登录成功，正在保存会话文件...")

        # 保存会话文件
        client.session.save('meme.session')
        print("💾 会话已保存到 meme.session")

        # 获取并显示用户信息
        me = await client.get_me()
        print(f"你已登录为：{me.first_name}（ID: {me.id}）")

asyncio.run(main())
