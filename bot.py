import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['TelegramBotDb']
collection = db['users']



# импорт библиотеки
import telebot

# подключение уникального токина к переменной botTimeWeb при помощи класса 
botTimeWeb = telebot.TeleBot('6451327207:AAHWO8JFIziH3q9dSnnWDQrm-_5pDVAPYU8')

# импорт части библиотеки, опр типы 
from telebot import types



# реагирует сообщение
# @botTimeWeb.message_handler(content_types=['text'])
@botTimeWeb.message_handler(commands=['start'])


# объявление функции startBot, которая принимает сообщение от пользователя
def text(message):

    #переменной присвоенно сообщение 
    user_mess=message.text

    # вставка данныхых в колекцию
    collection.insert_one({"message": user_mess})

    #интерактивная клава
    markup = types.InlineKeyboardMarkup()
    
    # кнопка ДА
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    
    #для отображение как клавиутура в боте
    markup.add(button_yes)

    # отправляет сообщение конкретному пользователю пользователю
    botTimeWeb.send_message(message.chat.id, user_mess,  parse_mode='html', reply_markup=markup)





# реагирует сообщение
@botTimeWeb.message_handler(commands=['all'])

def send_card(message):
       # Получение всех документов из коллекции
    all_documents = collection.find()
    # Вывод всех документов
    for document in all_documents:
       if 'message' in document:
        print(document['message'])


# включает режим ожидания новых сообщений
botTimeWeb.infinity_polling()