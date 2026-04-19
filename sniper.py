import os, asyncio, re
from telethon import TelegramClient, events

api_id = 26524317
api_hash = '977054238e89547d21d60762df7a527c'
phone = '+2348142773326'

client = TelegramClient('sniper_session', api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        print("Sending code to Telegram...")
        await client.send_code_request(phone)
        print("WAITING FOR code.txt FILE...")
        # Wait up to 5 minutes for you to create the file
        for _ in range(30): 
            if os.path.exists('code.txt'):
                with open('code.txt', 'r') as f:
                    val = f.read().strip()
                await client.sign_in(phone, val)
                print("✅ LOGGED IN!")
                os.remove('code.txt')
                break
            await asyncio.sleep(10)

    print("⚡ Sniper is LIVE!")
    @client.on(events.NewMessage(chats='https://t.me/SOLANA_TOKENS_CA'))
    async def h(e):
        if e.raw_text:
            cas = re.findall(r'[1-9A-HJ-NP-Za-km-z]{32,44}', e.raw_text)
            for ca in cas: await client.send_message('@BonkBot', ca)
    await client.run_until_disconnected()

asyncio.run(main())
