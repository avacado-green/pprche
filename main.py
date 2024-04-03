import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7092745767:AAFMrVnh38yhDRHIQBY5bdgUWTqJLLbJpT0')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('http://dzevetckiy.tilda.ws/page46023723.html#rec724940576')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')



@bot.message_handler(commands=['help'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Switch to specialist?')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Ask a Question?')
    markup.row(btn2)
    btn3 = types.KeyboardButton('In what year was Porsche founded?')
    markup.row(btn3)
    btn4 = types.KeyboardButton('Do you have a Web site ?')
    markup.row(btn4)
    btn5 = types.KeyboardButton('May I know about your company services?')
    markup.row(btn5)
    bot.send_message(message.chat.id, 'How can I help', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text.lower() == 'Do you have a Web site ?':
        bot.send_message(message.chat.id, 'You can go to the chat bot menu')
    elif message.text == 'Switch to specialist?':
        bot.send_message(message.chat.id, 'A specialist will contact you in a minute')
    elif message.text == 'Ask a Question?':
        bot.send_message(message.chat.id, 'Of course ask)')
    elif message.text == 'In what year was Porsche founded?':
        bot.send_message(message.chat.id, '1931')
    elif message.text == 'May I know about your company services?':
        bot.send_message(message.chat.id, 'You can view the services on our website')
    elif message.text == 'Do you have a Web site ?':
        bot.send_message(message.chat.id, 'Yes,You can go to our website through the chat bot menu')



@bot.message_handler(commands=['presentation',])
def presentation(message):
    file = open('./Frame 1_merged.pdf', 'rb')
    bot.send_document(message.chat.id, file)



bot.polling(non_stop=True)
