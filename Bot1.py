import telebot

bot = telebot.TeleBot('1985745406:AAFayRTUAfJUI0gm1fuqRCXMWuQ7eZZDxww')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess=f"<b>Привет {massage.from_user.first_name}</b>\nКакая высота дома?"
    bot.send_message(message.chat_id, send_mess,parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(messege):
    get_message_bot =2* messege.text.strip().lower()

bot.send_message(message.chat_id, get_message_bot,parse_mode='html')

bot.polling(none_stop=True)