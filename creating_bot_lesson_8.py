# from telebot import TeleBot
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# from grabing_rate import rate_list

# TOKEN = '7752082132:AAFkimn4-dvgiRDRvilZOYKnYECMDBXOc5g'
# bot = TeleBot(token=TOKEN)

# stopped_users = set()
# user_amount = {}
# messages = {}


# def yes_no_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Yes ✅", callback_data='Yes'), InlineKeyboardButton('No ❌', callback_data='No'))
#     return markup


# def usd_eu_rur_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 3
#     markup.add(InlineKeyboardButton('USD 💵', callback_data='USD'), InlineKeyboardButton('EU 💶', callback_data='EU'), InlineKeyboardButton('RUR 💴', callback_data='RUR'))
#     return markup


# @bot.message_handler(commands=['start'])
# def start(message):
#     global stopped_users
#     stopped_users.clear()
#     bot.send_message(message.chat.id, 'Welcome to one of the best exchange in Armenia(🇦🇲): \nDo you want to exchange your dram(“֏”)?: ', reply_markup = yes_no_markup())


# @bot.message_handler()
# def communication(message):
#     if message.from_user.id in stopped_users:
#         bot.send_message(message.chat.id, 'You already stopped bot. If you change your mind, restart the bot 🤔.')
#         return
#     elif 'quit' in message.text.lower() or 'exit' in message.text.lower() or 'stop' in message.text.lower():
#         stopped_users.add(message.from_user.id)
#         bot.send_message(message.chat.id, 'Thank you Bye!!!👋🏾')
#         return

#     bot.send_message(message.chat.id, 'Please enter the amount you want to exchange 💸:')
#     bot.register_next_step_handler(message, get_amount)


# @bot.callback_query_handler(func=lambda call: call.data in ['Yes', 'No'])
# def callback(call):
#     if call.data == 'No':
#         stopped_users.add(call.from_user.id)
#         bot.send_message(call.message.chat.id, 'Thank you Bye!!!👋🏾')
#         bot.answer_callback_query(call.id, 'Thank you Bye!!!👋🏾')
#     else:
#         bot.send_message(call.message.chat.id, "Please enter the amount you want to exchange 💸:")
#         bot.register_next_step_handler(call.message, get_amount)


# def get_amount(message):
#     if 'quit' in message.text.lower() or 'exit' in message.text.lower() or 'stop' in message.text.lower():
#         stopped_users.add(message.from_user.id)
#         bot.send_message(message.chat.id, 'Thank you Bye!!!👋🏾')   
#         return     
#     try:
#         amount = float(message.text)
#         user_amount[message.from_user.id] = amount
#         bot.send_message(message.chat.id, f"Got it! 💰 You entered: {amount}֏\nNow choose the currency you want to exchange to:", reply_markup=usd_eu_rur_markup())
#     except ValueError:
#         bot.send_message(message.chat.id, "Please enter a valid number. ")
#         bot.register_next_step_handler(message, get_amount)


# @bot.callback_query_handler(func=lambda call: call.data in ['USD', 'EU', 'RUR'])
# def currency_chooseing(call):
#     if call.data == 'USD':
#         sign = '$'
#     elif call.data == 'EU':
#         sign = '€'
#     else:
#         sign = '₽'

#     currency = rate_list(call.data)
#     amount = user_amount.get(call.from_user.id)
    
#     if amount and currency:
#         exchange = amount / currency
#         bot.send_message(call.message.chat.id, f"You'll get approximately {exchange:.2f}{sign} 💸.With {currency} {call.data} currency.")
#     else:
#         bot.send_message(call.messahe.chat.id, "Something went wrong, please try again.")
    
#     bot.send_message(call.message.chat.id, "Want to make another exchange? 🔁", reply_markup=yes_no_markup())
    
        


# bot.polling()
