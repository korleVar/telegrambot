
# импорт библиотеки
import telebot

# подключение уникального токина к переменной botTimeWeb при помощи класса 
botTimeWeb = telebot.TeleBot('6451327207:AAHWO8JFIziH3q9dSnnWDQrm-_5pDVAPYU8')

# импорт части библиотеки, опр типы 
from telebot import types



# реагирует сообщение
@botTimeWeb.message_handler(commands=['start'])

# объявление функции startBot, которая принимает сообщение от пользователя
def startBot(message):

    #переменной присвоенно сообщение с именем и фамилией пользователя
    first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о тебе?"
    
    #интерактивная клава
    markup = types.InlineKeyboardMarkup()
    
    # кнопка ДА
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    button_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    
    #для отображение как клавиутура в боте
    markup.add(button_yes, button_no)

    # отправляет сообщение конкретному пользователю пользователю
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


 

# включает режим ожидания новых сообщений
botTimeWeb.infinity_polling()
