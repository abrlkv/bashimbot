# -*- coding: utf-8 -*-
import os

import telebot

from bashim import Bashim

api_token = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(api_token, parse_mode="MARKDOWN")

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button = telebot.types.KeyboardButton('Показать еще')
keyboard.row(button)

hello_message ='''
Бот позволяет получать цитаты с сайта bash.im
Для получения рандомной цитаты, отправьте боту любое сообщение или нажмите на кнопку "Показать еще".
Для получения конкретной цитаты отправьте id цитаты.
'''
quote_format = "[#{}]({}quote/{})\n{}\n_{}_    👍 {}"

bash_quote =  Bashim()

def get_quote(id):
    img = None
    if id.isdigit():
        quote = bash_quote.get_quote(str(id))
    else:
        quote = bash_quote.get_random_quote()

    if quote == '404':
        message = 'Такой цитаты не существует'
    elif quote == 'error':
        message = 'Ошибка получения цитаты'
    else:
        message = quote_format.format(quote['id'],
                                    bash_quote.bashim_url,
                                    quote['id'],
                                    quote['text'],
                                    quote['date'],
                                    quote['raiting'])
        img = quote['img']
    
    return {'message': message, 'img': img}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,
                    hello_message,
                    reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def send_quote(message):
    quote = get_quote(message.text)
    if quote['img'] is not None:
        bot.send_photo(message.chat.id,
                        quote['img'],
                        quote['message'],
                        reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id,
                        quote['message'],
                        disable_web_page_preview=True,
                        reply_markup=keyboard)

bot.polling()