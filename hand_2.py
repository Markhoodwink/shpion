from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart 
import random
import kb as kb
import words

user = Router()
n = 1

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.restart)

@user.message(F.text == 'начать игру 🎃')
async def start(message: Message):
    await message.delete()
    global num_players, n
    num_players = 0
    n = 1
    await message.answer('выбери кол-во участников 🍟:',
                         reply_markup=kb.catalog)

@user.callback_query(F.data.startswith('restart'))
async def cmd_hello(callback: CallbackQuery):
    await callback.message.delete()
    global num_players, n
    num_players = 0
    n = 1
    await callback.message.answer('выбери кол-во участников 🍟:',
                         reply_markup=kb.catalog)

@user.callback_query(F.data.startswith('players'))
async def chek_pl(callback: CallbackQuery):
    await callback.message.delete()
    global spisok
    global num_players
    spisok = []
    num_players = int(callback.data.split('_')[1])
    first_word, sec_word = random.sample(words.WORDS, 2)
    if num_players < 5:
        for i in range(num_players):
            spisok.append(first_word)
        ind  = random.randint(0, num_players - 1)
        spisok[ind] = sec_word
    elif num_players < 8:
        for i in range(num_players):
            spisok.append(first_word)
        ind1, ind2 = random.sample(range(0, num_players - 1), 2)
        spisok[ind1] = sec_word
        spisok[ind2] = sec_word
    else:
        for i in range(num_players):
            spisok.append(first_word)
        ind1, ind2, ind3 = random.sample(range(0, num_players - 1), 3)
        spisok[ind1] = sec_word
        spisok[ind2] = sec_word
        spisok[ind3] = sec_word
    await callback.message.answer(f'{n} игрок',
    reply_markup=kb.game_show)

@user.callback_query(F.data.startswith('show'))
async def chek_word(callback: CallbackQuery):
    await callback.message.delete()
    global n
    n += 1
    await callback.message.answer(f'{n} игрок',
    reply_markup=kb.game_show)


@user.callback_query(F.data.startswith('hide'))
async def hide_word(callback: CallbackQuery):
    await callback.message.delete()
    if n < num_players:
        await callback.message.answer(f"{n} {spisok[n - 1]}",
                              reply_markup=kb.game_hide)
    else:
        await callback.message.answer(f"{n} {spisok[n - 1]}",
                              reply_markup=kb.game_again)

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)