import telebot

TOKEN = '1493436800:AAF1Eult9X13lyLQGGdScK63MbGOJyGqGbk'
bot = telebot.TeleBot(TOKEN)

keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
    'эфириум': 'ETH',
    'биткоин': 'BTC'
}

# исправление в строке доллар на корректное значение ключа, так же добавление основных криптовалют
# импорт библиотеки телебот
