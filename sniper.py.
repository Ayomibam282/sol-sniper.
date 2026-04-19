import re
from telethon import TelegramClient, events

# Configuration
api_id = 38332852
api_hash = '8026e47ad6f1f81686c93e5fb5cb526a'
source_id = -10017915667 
dest_id = 6376176715      

client = TelegramClient('sniper_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_id))
async def handler(event):
    # Extracts Solana address
    match = re.search(r'[1-9A-HJ-NP-Za-km-z]{32,44}', event.raw_text)
    if match:
        address = match.group(0)
        await client.send_message(dest_id, address)
        print(f"🚀 Sent to BONKbot: {address}")

print("⚡ Sniper is LIVE!")
client.start(phone='+2348142773326')
client.run_until_disconnected()
