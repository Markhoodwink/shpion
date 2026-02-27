from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart, Command

import keybords as kb
from states import Reg

user = Router()

VOCAB = [
    "кошка", "собака", "самолёт", "телефон", "яблоко",
    "космос", "река", "гора", "тачка", "музей",
    "замок", "супермаркет", "шоколад", "робот", "кинотеатр",
    "пират", "шпион", "бот", "карта сокровищ", "тайник",
    "призрак", "магнитофон", "карандаш", "лифт", "мост",
    "футбол", "гитара", "телескоп", "лампа", "кружка",
    "ледник", "ледокол", "старое фото", "письмо", "секретный знак",
    "ледяной меч", "сказка", "кафе", "библиотека", "зонтик"
]

@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Welcome@!!!!\n\nВвеидте ваше имя')

#@user.message(Command('help'))
#async def cmd_help(message: Message):
#    await message.answer('You wrote a comm /help')

#@user.message(F.photo)
#async def cmd_photo(message: Message):
#    await message.answer(f'You send me a photo!\n\nHis id: {message.photo[-1].file_id}')
#    await message.answer_photo(photo=message.photo[-2].file_id)
    
@user.message(F.text == 'Самамалекум')
async def cmd_hello(message: Message):
    await message.answer('валейкувасалам')

@user.message(F.text == 'построить дом')
async def cmd_hello(message: Message):
    await message.answer('выбери как именно:',
                         reply_markup=kb.catalog)

@user.callback_query(F.data.startswith('action_'))
async def chek_action(callback: CallbackQuery):
    act_name = callback.data.split('_')[1]
    await callback.answer(f'{act_name.capitalize()}!!!')#, show_alert=True)
    await callback.message.answer(f'{act_name.capitalize()}')
    
@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)