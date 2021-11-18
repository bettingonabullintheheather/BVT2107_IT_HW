import telebot
from telebot import types

token = "2123011997:AAHC7Js79WXP1Tu9_xD20b_g358IaJ5EOpY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "/who")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я не умею')

@bot.message_handler(commands=['who'])
def start_message(message):
    bot.send_message(message.chat.id, 'БВТ2107 Канев Демид — мой автор.')

@bot.message_handler(commands=['42'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я не понимаю о чем вы')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "не хочу":
        bot.send_message(message.chat.id, 'Это печально')
    elif message.text.lower() == "42424242":
        bot.send_message(message.chat.id, '░░██╗██╗██████╗░')
        bot.send_message(message.chat.id, '░██╔╝██║╚════██╗')
        bot.send_message(message.chat.id, '██╔╝░██║░░███╔═╝')
        bot.send_message(message.chat.id, '███████║██╔══╝░░')
        bot.send_message(message.chat.id, '╚════██║███████╗')
        bot.send_message(message.chat.id, '░░░░░╚═╝╚══════╝')
    else:
        bot.send_message(message.chat.id, "Возможно, стоит опробоавть команду /help. Рекомендую.")