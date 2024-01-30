import openai
import telebot


openai.api_key = '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'
bot = telebot.TeleBot( '6594685393:AAFaC6WXPofT3FEpWhnAVxkNsHgimGeQUGA')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, я ChatGPT в телерамм')

@bot.message_handler(func=lambda _: True)
def handler_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling(none_stop=True)
