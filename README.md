# Telegram Job-Filtering Bot 🤖

### Overview
The Telegram Job-Filtering Bot is designed to automate your job search by monitoring selected Telegram channels for job postings that match specific keywords. Built with Python and the Telethon library, the bot scans messages in real-time, filtering out the ones relevant to your job search, and then forwards them to a designated Telegram account or channel.

### Features
* 🛠 Monitors multiple Telegram channels for new job postings.
* 🎯 Case-insensitive keyword matching: “frontend”, “Frontend”, “фронтенд“, “Фронтенд“, etc.
* 🔄 Real-time message forwarding.
* ✅ Easy to set up and run.

### Prerequisites
Python 3.x
Telethon Python package
A .env file for storing Telegram API credentials

### Installation

1. Clone the Repository: Clone this repository to your local machine.

```
git clone https://github.com/your-repo/only-front.git
```
2. Install Dependencies: Navigate to the project directory and run:
```
pip install -r requirements.txt
```
3. Environment Setup: Create a .env file in the project directory and add your Telegram API ID and Hash.
```
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
```
4. Run the Bot: In the project directory, execute the Python script.
```
python3 telegram_forward_bot.py
```
5. Authorize: The first time you run the script, you’ll be asked to enter a Telegram authentication code. Follow the on-screen instructions.


### Usage

1. Channel Configuration: Add or remove Telegram channels in the channel_urls list in the Python script.

```
channel_urls = [
    ‘https://t.me/some_url’,
    ‘https://t.me/some_url’,
    # Add more channels here
]
```
2. Keyword Configuration: Add or remove job search keywords in the keywords list in the Python script.

```
keywords = [‘you_key_word’, ‘you_key_word_2’]
```

3. Forwarding Destination: Set the forward_to variable to the username or ID where you want to forward messages.

```
forward_to = ‘your_path_to_channel_or_bot’
```
