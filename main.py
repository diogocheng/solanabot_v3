import logging
from telegram.ext import Application, CommandHandler
from dexscreener import fetch_tokens
from filter import token_meets_criteria
from telegram_bot import send_alert
import os
from dotenv import load_dotenv
from telegram_handler import TelegramHandler  # Import the custom Telegram handler

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a Telegram handler
tg_handler = TelegramHandler(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)
tg_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
tg_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(tg_handler)

# Define the callback function for the job
async def check_and_alert(context):
    tokens = fetch_tokens()
    for token in tokens:
        if token_meets_criteria(token):
            base = token.get("baseToken", {})
            message = (
                f"Token Alert: {base.get('name', 'Unknown')} ({base.get('symbol', 'N/A')})\n"
                f"Market Cap: {token.get('marketCap', 'N/A')}\n"
                f"24h Volume: {token.get('volume', {}).get('24h', 'N/A')}\n"
                f"24h Price Change: {token.get('priceChange', {}).get('24h', 'N/A')}%\n"
                f"Liquidity: {token.get('liquidity', {}).get('usd', 'N/A')} USD"
            )
            await send_alert(context, message)

# Define the start command handler
async def start(update, context):
    await update.message.reply_text("Bot started!!! You will receive updates every minute.")

def main():
    # Initialize the application with your bot's token
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add the start command handler
    app.add_handler(CommandHandler("start", start))

    # Schedule the check_and_alert function to run every 5 minutes
    job_queue = app.job_queue
    job_queue.run_repeating(check_and_alert, interval=60)  # 60 1minute

    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
