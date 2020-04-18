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
    bot.send_message(chat_id, "Здравствуй друг! Из какого ты города?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def next_city(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardRemove()
    if message.text == 'Лемтыбож':
        send = bot.send_message(chat_id, "Введите ваш номер телефона:", reply_markup=markup)
        bot.register_next_step_handler(send, next_phone)

def next_phone(message):
    try:
        chat_id = message.chat.id
        int(message.text)
        send = bot.send_message(chat_id, "Введите ваше имя: ")
        #bot.register_next_step_handler(send, next_)
    except Exception as err:
        msg = bot.send_message(chat_id, "Вы что-то ввели не так...")
        bot.register_next_step_handler(msg, next_phone)




if __name__ == '__main__':
    bot.polling(none_stop=True)