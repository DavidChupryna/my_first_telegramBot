import telebot
import random
from info import bot_responses, main_character, message_templates

token = '6852148800:AAG0BTjqt1S-RUMQW7zjEChho85xqPPHdfE'
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, f"{random.choice(bot_responses["hello"])}.\n"
                                      f"Я бот визитка главного персонажа из серии книг и игр Metro!\n"
                                      f"Для полного ознакомления с ботом напишите команду: /help")


@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.chat.id, "Вот список команд которые помогут тебе познакомиться со мной:\n"
                                      "/name - моё имя;\n"
                                      "/age - мой возраст;\n"
                                      "/skills - мои скилы;\n"
                                      "/photo - моё фото;\n"
                                      "/city - узнать откуда я;\n"
                                      "/wife - информация о моей супруге;\n"
                                      "/about_me - вся информация обо мне.\n"
                                      "Так-же вы можете позадавать мне разные "
                                      "вопросы(как дела, что нового, чем занят),"
                                      "поздароваться или попрощаться,"
                                      "попросить рассказать вам анекдот или шутку!")


@bot.message_handler(commands=['name'])
def send_name(message):
    bot.send_message(message.chat.id, f'Меня зовут {main_character["name"]}.')


@bot.message_handler(commands=['age'])
def send_age(message):
    bot.send_message(message.chat.id, f'Мне {main_character["age"]} лет.')


@bot.message_handler(commands=['skills'])
def send_skills(message):
    bot.send_message(message.chat.id, f'Мои лучшие скилы это:')
    for skill in main_character["skills"]:
        bot.send_message(message.chat.id, f'- {skill}')


@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.send_photo(message.chat.id, open(main_character["photos"][0], "rb"))


@bot.message_handler(commands=['city'])
def send_city(message):
    bot.send_message(message.chat.id, "Я из Московского метрополитена")


@bot.message_handler(commands=['about_me'])
def send_portfolio(message):
    bot.send_photo(message.chat.id, open(main_character["photos"][1], "rb"))
    bot.send_message(message.chat.id, f"{main_character['about_me']}")


@bot.message_handler(commands=['wife'])
def send_wife(message):
    bot.send_photo(message.chat.id, open(main_character["wife"]["photo"], "rb"))
    bot.send_message(message.chat.id, f"{main_character['wife']['name']}, "
                                      f"возраст: {main_character['wife']['age']} лет, "
                                      f"{main_character['wife']['about_ann']}")


@bot.message_handler(content_types=['text'])
def bot_send(message):
    if message.text.lower() in message_templates['anecdote_ms']:
        bot.send_message(message.chat.id, f"{bot_responses["anecdote"]}")
    elif message.text.lower() in message_templates['jokes_ms']:
        bot.send_message(message.chat.id, f"{random.choice(bot_responses["jokes"])}")
    elif message.text.lower() in message_templates['hello_ms']:
        bot.send_message(message.chat.id, f"{random.choice(bot_responses["hello"])}")
    elif message.text.lower() in message_templates['buy_ms']:
        bot.send_message(message.chat.id, f"{random.choice(bot_responses["buy"])}")
    elif message.text.lower() in message_templates['hay_ms']:
        bot.send_message(message.chat.id, f"{random.choice(bot_responses["how_are_you"])}")
    elif message.text.lower() in message_templates['do_work_ms']:
        bot.send_message(message.chat.id, f"{random.choice(bot_responses["do_work"])}")
    elif message.text.lower() in message_templates['help_ms']:
        bot.send_message(message.chat.id, "Воспользуйтесь командой /help")
    else:
        bot.send_message(message.chat.id, "Задайте другой вопрос или воспользуйтесь командой /help")


bot.infinity_polling()