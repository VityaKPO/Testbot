import telebot
import random

greetings = ["Привет", "Дратути", "Здравствуй", ]
how_are_you = ["Отлично", "Ужасно", "Хорошо", " Супер Гуд ! Я выйграл в лотерее"]

token = "777744700:AAEyRbHe4UR4M8ttlgTMdUGoHrsZzKnw8j8"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, random.choice(greetings) + ", " + message.chat.first_name)
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, random.choice(how_are_you))


if __name__ == "__main__":
    bot.polling(none_stop=True)

