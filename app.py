import telebot
from TOKEN import TOKEN
from extensions import APIException, CurrencyConverter


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
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Invalid number of parameters, please check example in /values')

        base, quote, amount = values
        response = CurrencyConverter.get_price(quote, base, amount)

        if not amount.isdigit():
            raise APIException('Amount should be a valid number.')

    except APIException as errormessage:
        bot.reply_to(message, f'Input error.\n{errormessage}')
    except Exception as errormessage:
        bot.reply_to(message, f'Could not process a command, server error.\n{errormessage}')
    else:
        text = f'{amount} {base} is {response} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling()
