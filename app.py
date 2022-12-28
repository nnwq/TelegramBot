import telebot
import requests
import json
from config import keys
from APIKEY import APIKey
from TOKEN import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def hello(message: telebot.types.Message):
    text = f'Hello, {message.chat.username}. I can show you the currency exchange rate. '\
            '\n'\
            'To begin, please use this format: "Currency" "Convert to" "Amount". Example: USD EUR 1500'\
            '\n'\
            'Available commands: Values - shows available currencies.'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.reply_to(message, 'Available currencies: Euro, Great Britain Pound(GBP), USD')


@bot.message_handler(content_types=['text', ])
def exchange(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    url = requests.get(f'https://anyapi.io/api/v1/exchange/convert?apiKey={APIKey}&base={keys[base]}&to={keys[quote]}&amount={amount}')
    response = json.loads(url.content)['converted']
    text = f'{amount} {quote} is {response} {base}'
    bot.send_message(message.chat.id, text)


bot.polling()
