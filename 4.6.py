import os
import requests
from telegram.ext import Updater, CommandHandler

# Токен бота Telegram
TOKEN = os.getenv('6594448229:AAH1Ogdv7FCluMlZ5T8rD3vpQTbt_54FsHM')

# API-ключ Unsplash
UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может отправлять тебе случайные картинки. Используй команду /pic, чтобы получить новое изображение.")

def get_random_image(update, context):
    # Получение случайной картинки через API Unsplash
    response = requests.get(
        "https://api.unsplash.com/photos/random",
        headers={"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    ).json()
    image_url = response['urls']['regular']

    # Отправка картинки пользователю
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pic", get_random_image))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
