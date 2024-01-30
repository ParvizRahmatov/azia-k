import telebot
import wikipedia

wikipedia.set_lang('ru')

TOKEN = '6594685393:AAFaC6WXPofT3FEpWhnAVxkNsHgimGeQUGA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcom(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я тестовый бот Парвиза, я могу отвечать на ваши вопросы.')
    


@bot.message_handler(content_types=['text'])
def talk(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Здравствуйте, как у вас дела?')
    elif message.text == 'Хорошо спасибо':
         bot.send_message(message.chat.id, 'Отлично, рад за вас!')
    if message.text == 'Можешь ли ты мне помочь':
        bot.send_message(message.chat.id, 'С удовольствием, готов вам помочь?')
    else:
        low_r = message.text
        low_r = low_r.replace(" ", "_")
        page = wikipedia.page(low_r)
        bot.send_message (message.chat.id, page.summary)

bot.polling(none_stop=True)
