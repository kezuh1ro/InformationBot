import telebot

bot = telebot.TeleBot('6607352864:AAEphPnsSaaa8zMXRBV097S_pNuVqCrXc4A')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Hello</b> {message.from_user.first_name}<b>!</b>\n/help <b>- shows all commands</b>', parse_mode='html')

@bot.message_handler(commands=['name'])
def name(message):
    bot.send_message(message.chat.id,
        f"<b>First Name:</b> {message.from_user.first_name or 'None'}\n"
        f"<b>Last Name</b>: {message.from_user.last_name or 'None'}\n",
        parse_mode='html'
    )

@bot.message_handler(commands=['uname'])
def uname(message):
    bot.send_message(message.chat.id,
        f"<b>Username</b>: @{message.from_user.username or 'None'}\n",
        parse_mode='html'
    )

@bot.message_handler(commands=['id'])
def id(message):
    bot.send_message(message.chat.id,
        f"<b>ID</b>: <code>{message.from_user.id}</code>",
        parse_mode='html'
    )

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
        f'/name <b>- shows your first name and last name</b>'
        f'/uname <b>- shows your username</b>'
        f'/id <b>- shows your id</b>',
        parse_mode='html'
    )

    
bot.infinity_polling()
