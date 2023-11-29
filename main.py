import telebot

bot = telebot.TeleBot('6627040703:AAFB2sQGsKC0988zrS3vsTjjJ7E5sSDtCf8')


@bot.message_handler(commands=['/start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет, это бот на Python по урокам Умскул. /n Для получения списка команд напиши /help_list',
                     parse_mode='Markdown')


@bot.message_handler(commands=['/joke'])
def main(message):
    bot.send_message(message.chat.id,
                     'Никогда не выявляйте в программе ошибки, если не знаете, что с ними дальше делать.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['/help_list'])
def main(message):
    bot.send_message(message.chat.id,
                     '/start - начать работу /n /joke - получить шутку /n /help_list - список команд /n /link - тестовая ссылка /n /pay - произвести оплату',
                     parse_mode='Markdown')


@bot.message_handler(commands=['/link'])
def main(message):
    bot.send_message(message.chat.id, 'Это ссылка на [Умскул](https://umschool.net/)', parse_mode='Markdown')


@bot.message_handler(commands=['/pay'])
def main(message):
    bot.send_message(message.chat.id, '*С ВАС СПИСАНО 5000 РУБЛЕЙ*', parse_mode='Markdown')


bot.infinity_polling()
