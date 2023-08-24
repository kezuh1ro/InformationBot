import telebot
import asyncio

bot = telebot.TeleBot('6607352864:AAEphPnsSaaa8zMXRBV097S_pNuVqCrXc4A')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}!')

@bot.message_handler(commands=['info'])
async def info(message):
    reply = await message.get_reply_message
    if reply:
        await bot.send_message(message.chat.id,
            f"<b>First Name:</b> {reply.sender.first_name or 'None'}\n"
            f"<b>Last Name</b>: {reply.sender.last_name or 'None'}\n"
            f"<b>Username</b>: @{reply.sender.username or 'None'}\n"
            f"<b>ID</b>: <code>{reply.sender.id}</code>",
            parse_mode='html'
        )
    else:
        await bot.send_message(message.chat.id,
            f"<b>First Name:</b> {message.from_user.first_name or 'None'}\n"
            f"<b>Last Name</b>: {message.from_user.last_name or 'None'}\n"
            f"<b>Username</b>: @{message.from_user.username or 'None'}\n"
            f"<b>ID</b>: <code>{message.from_user.id}</code>",
            parse_mode='html'
        )
    
    
bot.infinity_polling()
