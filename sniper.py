import os
import asyncio
from telethon import TelegramClient, events

# --- CONFIGURATION ---
api_id = 26524317
api_hash = '977054238e89547d21d60762df7a527c'
phone_number = '+2348142773326'

# This script will save the session to a file automatically
client = TelegramClient('sniper_session', api_id, api_hash)

async def main():
    print("Connecting to Telegram...")
    await client.connect()
    
    if not await client.is_user_authorized():
        print(f"Sending code to {phone_number}...")
        # This sends the code to your Telegram app
        sent_code = await client.send_code_request(phone_number)
        
        print("!!! ACTION REQUIRED !!!")
        print("Check your Telegram app for a 5-digit code.")
        print("Since your keyboard is blocked, you have 2 minutes to")
        print("write the code in a file named 'code.txt' in this repo.")
        
        # We wait for you to create a file named code.txt with the digits
        for _ in range(20): # Wait 2 minutes
            if os.path.exists('code.txt'):
                with open('code.txt', 'r') as f:
                    code = f.read().strip()
                try:
                    await client.sign_in(phone_number, code)
                    print("✅ Successfully Logged In!")
                    os.remove('code.txt')
                    break
                except Exception as e:
                    print(f"Error: {e}")
            await asyncio.sleep(10)
    
    print("⚡ Sniper is LIVE!")
    # ... rest of your sniper code here ...

asyncio.run(main())

