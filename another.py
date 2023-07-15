import telebot
from config import TOKEN, keys
from extensions import ExchangeException, Exchange

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text = f'Привет! Я Бот-Конвертер валют и я могу: \n'\
           f'- Показать список доступных валют через команду /values'\
           f'- Вывести конвертацию валюты через команду \n<имя валюты>'\
           '< в какую валюту перевести >'\
           '< количество переводимой валюты >'\
           f'\nЧтобы увидеть список всех доступных валют,введите команду: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message):
    text = '\nЧтобы начать конвертацию, введите команду боту в следующем формате: \n'\
           f'\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>'\
           f'\nЧтобы увидеть список всех доступных валют, введите команду\n/values'
    bot.reply_to(message, text)



@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты для перевода:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
        bot.reply_to(message, text)




@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ExchangeException('Введите команду или 3 параметра')

        quote, base, amount = values
        total_base = Exchange.get_price(quote, base, amount)
    except ExchangeException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с \n{e}')
    else:
        text = f'Цена <b>{amount} {quote} </b> в <b>{base}</b>-<b>{total_base}</b>'
        bot.send_message(message.chat.id, text, parse_mode='html')

# переделала нижнюю часть кода

bot.polling(none_stop=True)
# значение нон-стоп = True