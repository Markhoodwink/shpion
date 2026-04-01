from aiogram.types import (ReplyKeyboardMarkup,  KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

menu = InlineKeyboardMarkup(
    inline_keyboard =  [
        [InlineKeyboardButton(text='сложно 🎃', callback_data='diff_hard'), InlineKeyboardButton(text='легко 🍉', callback_data='diff_easy')],
        [InlineKeyboardButton(text='интересно 🍥', callback_data='diff_int'),InlineKeyboardButton(text='english 💂‍♀️', callback_data='diff_eng')], 
        [InlineKeyboardButton(text='clash royale 🃏', callback_data='diff_royale'), InlineKeyboardButton(text='dota 2 🐦‍🔥', callback_data='diff_dota')],
        [InlineKeyboardButton(text='персонажи 👀', callback_data='diff_persons'), InlineKeyboardButton(text='кино 🎥', callback_data='diff_cinema')],
        [InlineKeyboardButton(text='бренды 💰', callback_data='diff_brends'), InlineKeyboardButton(text='математика 📐', callback_data='diff_math')]
    ], 
)

restart = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='никто не знает кто шпион ❔', callback_data='restart_nobody')],
        [InlineKeyboardButton(text='шпион знает, что он шпион 🥷', callback_data='restart_knows')]
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
        [InlineKeyboardButton(text='cкрыть 🔄️', callback_data='choose_type')],
    ]
)