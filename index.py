from telethon import TelegramClient, events
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
client = TelegramClient('anon', api_id, api_hash)

# Your list of channel URLs
channel_urls = [
    'https://t.me/Remoteit',
    'https://t.me/Relocats',
    'https://t.me/remote',
    'https://t.me/europe_hiring',
    'https://t.me/lalatestchannelforfiltering',
    'https://t.me/g_jobbot'
]

# Extract usernames from URLs
channels = [urllib.parse.urlparse(url).path.lstrip('/') for url in channel_urls]

# Forwarding destination
# Note: Here forward_to should be the ID or username where you want to forward messages,
# not the URL.
forward_to = 'filter_for_job_bot' 

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    # Convert message to lower-case
    message_text_lower = event.raw_text.lower()
    
    # List of keywords, converted to lower-case
    keywords = ['frontend', 'фронтенд']
    keywords_lower = [keyword.lower() for keyword in keywords]
    
    # Check for keywords
    if any(keyword in message_text_lower for keyword in keywords_lower):
        # Forward the message
        await client.forward_messages(forward_to, event.message)

# Start the client
with client:
    client.run_until_disconnected()

