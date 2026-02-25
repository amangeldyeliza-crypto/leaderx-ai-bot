import os
import telebot
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are LeaderX AI — жастарға мотивация беретін, лидерлікке бағыттайтын ассистент. Қазақ тілінде жауап бер."},
                {"role": "user", "content": message.text}
            ]
        )

        bot.reply_to(message, response["choices"][0]["message"]["content"])

    except Exception as e:
        bot.reply_to(message, "Қате шықты 😢 Кейін қайта көріңіз.")

bot.polling()
