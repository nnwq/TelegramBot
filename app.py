import telebot
import requests
import json
from config import keys
import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def hello(message: telebot.types.Message):
    text = f'Hello, {message.chat.username}. I can show you the currency exchange rate. '\
            '\n'\
            'To begin, please use this format: "Currency" "Convert to" "Amount". Example: USD RUB 1500'\
            '\n'\
            'Available commands: Values - shows available currencies.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.reply_to(message, 'Available currencies: Euro, Rub, USD')


bot.polling()
