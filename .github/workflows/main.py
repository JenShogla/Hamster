import telebot

bot = telebot.TeleBot('6269264431:AAFoMVfVRYy2Ch-vLtZrbgwNJ51J7WAAjSw')


@bot.message_handler(content_types=['text'])
def delete_links(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    chat_member = bot.get_chat_member(chat_id, user_id)
    if chat_member.status not in ['administrator', 'creator']:
        for entity in message.entities:
            if entity.type == 'url':
                mess = f'<b>{message.from_user.first_name} <u>{message.from_user.last_name}' \
                       f'</u></b>, В цьому чаті заборонено ' \
                       f' розміщуваті будь-які посилання!'
                bot.delete_message(chat_id, message.id)
                bot.send_message(chat_id=message.chat.id, text=mess, parse_mode='HTML')
                break


bot.polling(none_stop=True)
