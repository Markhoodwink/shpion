from aiogram.types import (ReplyKeyboardMarkup,  KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(
    keyboard =  [
        [KeyboardButton(text='начать игру сложно 🎃'), KeyboardButton(text='начать игру легко 🍉')],
        [KeyboardButton(text='начать игру интересно 🍥'),KeyboardButton(text='start game english 💂‍♀️')], 
        [KeyboardButton(text='начать игру clash royale 🃏'), KeyboardButton(text='начать игру dota 2 🐦‍🔥')]
        [KeyboardButton(text='начать игру персонажи 👀'), KeyboardButton(text='начать игру кино 🎥')]
    ], 
    resize_keyboard=True,
    input_field_placeholder='Выберите тип игры'
)

restart = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='начать игру 🕵️‍♀️', callback_data='restart')],
    ]
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='3', callback_data='players_3'), 
         InlineKeyboardButton(text='4', callback_data='players_4'), 
         InlineKeyboardButton(text='5', callback_data='players_5')],
         [InlineKeyboardButton(text='6', callback_data='players_6'), 
         InlineKeyboardButton(text='7', callback_data='players_7'), 
         InlineKeyboardButton(text='8', callback_data='players_8')]
    ]
)

game_show = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='посмотреть 👁️', callback_data='hide')],
    ]
)

game_hide = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='скрыть 🔒', callback_data='show')],
    ]
)

game_again = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='cкрыть 🔄️', callback_data='restart')],
    ]
)