import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('6607352864:AAEphPnsSaaa8zMXRBV097S_pNuVqCrXc4A')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/name')
    btn3 = types.KeyboardButton('/uname')
    btn4 = types.KeyboardButton('/id')
    btn5 = types.KeyboardButton('/ping')
    btn6 = types.KeyboardButton('/version')
    markup.row(btn2, btn3, btn4)
    markup.row(btn1, btn5, btn6)
    bot.reply_to(message, f'<b>Hello</b> {message.from_user.first_name}<b>!</b>\n\n/help <b>- shows all commands</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['name'])
def name(message):
    bot.reply_to(message,
        f"<b>First Name:</b> {message.from_user.first_name or 'None'}\n"
        f"<b>Last Name</b>: {message.from_user.last_name or 'None'}\n",
        parse_mode='html'
    )

@bot.message_handler(commands=['uname'])
def uname(message):
    bot.reply_to(message,
        f"<b>Username</b>: @{message.from_user.username or 'None'}\n",
        parse_mode='html'
    )

@bot.message_handler(commands=['id'])
def id(message):
    bot.reply_to(message,
        f"<b>ID</b>: <code>{message.from_user.id}</code>",
        parse_mode='html'
    )

@bot.message_handler(commands=['version'])
def version(message):
    bot.reply_to(message, f"<b>Bot version:</b> <code>1.0.1</code>", parse_mode='html')

@bot.message_handler(commands=['ping'])
def ping(message):
    start = datetime.datetime.now()
    end = datetime.datetime.now()
    pong = (end-start).microseconds / 0.1
    pinging = f"**{pong}**"
    bot.reply_to(message, f'<b>Bot ping:</b> <code>{pong}</code> ms', parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,
        f'/name <b>- shows your first name and last name</b>\n'
        f'/uname <b>- shows your username</b>\n'
        f'/id <b>- shows your id</b>\n'
        f'/ping <b>- shows bot ping</b>\n'
        f'/version <b>- shows bot version</b>\n\n'
        f'<b>Bot creator:</b> <code>@poslan1e</code>, <code>@p0slan1e</code>\n'
        f'<b>Source:</b> https://github.com/kezuh1ro/InformationBot/blob/main/InformationBot.py',
        parse_mode='html'
    )

    
bot.infinity_polling()
