from aiogram.types import (ReplyKeyboardMarkup,  KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

menu = ReplyKeyboardMarkup(
    keyboard =  [
        [KeyboardButton(text='построить дом')],
        [KeyboardButton(text='пойти в шахту'), KeyboardButton(text='пвп 1 на 1')]
    ], 
    resize_keyboard=True,
    input_field_placeholder='че поделать в майнкрафте'
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='посмотреть референс в ютубе', callback_data='action_включай впн')],
        [InlineKeyboardButton(text='построить хижину из земли', callback_data='action_зато быстро')],
        [InlineKeyboardButton(text='остатья жить в пещере', callback_data='action_дело вкуса')]
    ]
)

get_number =  ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='send a number', request_contact=True)]
    ]
)