import telebot
from telebot import types

bot = telebot.TeleBot("1265196638:AAF2-KYTc-6y1JWy1F3A-GjDw95qHRJfTuM")

@bot.message_handler(commands=['start','help'])
def messag(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Вуктыл')
    btn2 = types.KeyboardButton('Лемтыбож')
    btn3 = types.KeyboardButton('Лемты')
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "Здравствуй другc!", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)