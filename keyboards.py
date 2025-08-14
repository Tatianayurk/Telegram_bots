from telebot.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,KeyboardButton,InlineKeyboardButton

def registration_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Регистрация',callback_data='registration'))
    return keyboard

def command_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Запись',callback_data='order'))
    keyboard.add(InlineKeyboardButton('Удалить аккаунт',callback_data='delete_account'))
    return keyboard

def request_contact_keyboard():
    keyboard = ReplyKeyboardMarkup()
    keyboard.add(KeyboardButton('Данные',True))
    return keyboard

def services_keyboard(buttons):
    keyboard = InlineKeyboardMarkup()
    for element in buttons:
        keyboard.add(InlineKeyboardButton(element[1],callback_data=f'service:{element[0]}'))
    keyboard.add(InlineKeyboardButton('Назад',callback_data=''))
    return keyboard
