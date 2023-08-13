# импорт библиотеки

import telebot
import pymongo

# import emoji


# импорт части библиотеки, опр типы
from telebot import types
from bson import ObjectId

# from emoji import emojize

# подключение к бд
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["TelegramBotDb"]
collection = db["users"]


# подключение уникального токина к переменной bot при помощи класса
bot = telebot.TeleBot("6451327207:AAHWO8JFIziH3q9dSnnWDQrm-_5pDVAPYU8")


# реагирует сообщение
@bot.message_handler(func=lambda message: not message.text.startswith("/"))

# объявление функции text, которая принимает сообщение от пользователя
def text(message):
    # переменной присвоенно сообщение
    user_mess = message.text

    # вставка данныхых в колекцию
    collection.insert_one({"message": user_mess})


# bot.infinity_polling()


# реагирует сообщение
@bot.message_handler(commands=["all"])
def send_card(message):
    # Получение всех документов из коллекции
    all_documents = collection.find()

    # Формирование строки с данными
    data_string = ""

    markup = types.InlineKeyboardMarkup()

    # Вывод всех документов
    for document in all_documents:
        if "message" in document:
            text_with_checkmark = "✅ " + document["message"]
            # button_all =
            button_yes = types.InlineKeyboardButton(
                text_with_checkmark,
                callback_data=f"delete_{document['_id']}",  # Используем _id документа как метку
            )
            markup.add(button_yes)

        # отправка данных пользователю
    bot.send_message(message.chat.id, "Продукты", reply_markup=markup)


# Обработчик нажатия на кнопку
# события происходят при нажатии на кнопку и при наличие delete
@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_"))
# функция работает при нажатии на кнопку
def delete_data(call):
    # Получаем _id документа из метки
    data_id = call.data.split("_")[1]
    # удаляем
    collection.delete_one({"_id": ObjectId(data_id)})

    # Отправляем подтверждение удаления
    bot.answer_callback_query(call.id, "купленно")


# клава
@bot.message_handler(commands=["START"])
def first(message):
    service = types.ReplyKeyboardMarkup(True, True)
    service.row("/что надо купить?")
    service.row("/купленно всё")

    bot.send_message(message.chat.id, "твои действия", reply_markup=service)
    print("yzv")


# вывод списка после нажатия на кнопку "что надо купить"
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "/что надо купить?":
        send_card(message)


# Запуск бота
bot.infinity_polling()
