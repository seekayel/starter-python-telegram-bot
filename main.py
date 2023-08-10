import os
from dotenv import load_dotenv
from fastapi import FastAPI
from telegram import Update, Bot
from pydantic import BaseModel

class TelegramUpdate(BaseModel):
    update_id: int
    message: dict

app = FastAPI()

# Load variables from .env file if present
load_dotenv()

# Read the variable from the environment (or .env file)
bot_token = os.getenv('BOT_TOKEN')

bot = Bot(token=bot_token)

@app.post("/webhook/")
async def handle_webhook(update: TelegramUpdate):
    chat_id = update.message["chat"]["id"]
    text = update.message["text"]

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="Welcome to my bot!")
    else:
        bot.send_message(chat_id=chat_id, text="Yo")

    return {"ok": True}
