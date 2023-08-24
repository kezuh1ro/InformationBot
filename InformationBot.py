import telebot

bot = telebot.TeleBot('6607352864:AAEphPnsSaaa8zMXRBV097S_pNuVqCrXc4A')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message.chat.id, f'Hello {message.from_user.first_name}!')

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message.chat.id,
        f"<b>First Name:</b> {message.from_user.first_name or 'None'}\n"
        f"<b>Last Name</b>: {message.from_user.first_name or 'None'}\n"
        f"<b>Username</b>: @{message.from_user.username or 'None'}\n"
        f"<b>ID</b>: <code>{message.from_user.id}</code>"
    )
    
    
bot.infinity_polling()
