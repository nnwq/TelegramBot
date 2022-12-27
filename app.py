import telebot
import requests
import json
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def hello(message: telebot.types.Message):
    text = f'Hello, {message.chat.username}. I can show you the currency exchange rate of USD/EUR/RUB '\
            ''\
            'To begin, please use this format: "Currency" "Convert to" "Amount". Example: USD RUB 1500 '
    bot.reply_to(message, text)


bot.polling()
