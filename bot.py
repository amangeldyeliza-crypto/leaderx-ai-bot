import telebot
import openai
import os
from flask import Flask

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are LeaderX AI — youth leadership assistant."},
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, response['choices'][0]['message']['content'])
    except Exception as e:
        bot.reply_to(message, "Қате шықты: " + str(e))

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.polling, kwargs={'none_stop': True}).start()
    app.run(host="0.0.0.0", port=10000)
pyTelegramBotAPI
openai==0.28.0
flask

