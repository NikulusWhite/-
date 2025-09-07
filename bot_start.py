import telebot
from filework import FileOpener

bot = telebot.TeleBot("YOUR API")

opener = FileOpener()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    q = message.text.strip()

    if not q.isdigit():
        bot.send_message(message.chat.id, "Ошибка: введите цифру.")
        return

    answer = opener.get_answer(q)

    if answer is None:
        bot.send_message(message.chat.id, "Ошибка: маркеры не найдены или файл пустой.")
    else:
        bot.send_message(message.chat.id, answer)

print("Бот запущен...")
bot.infinity_polling()
