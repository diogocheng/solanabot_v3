import os
from telegram import Bot
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the token and chat ID from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Initialize the bot
bot = Bot(token=TELEGRAM_TOKEN)

async def send_alert(context, message):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        logging.error(f"Error sending alert: {e}")
