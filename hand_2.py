from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart 
import random
import kb
import words, phrases, words_ez, people, films, english, clash_royale, dota

user = Router()
smile = ''

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать 🕵️‍♀️', reply_markup=kb.menu)

@user.message(F.text == 'начать игру сложно 🎃')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🎃'
    word_list = words.WORDS_HARD
    await message.answer('🎃 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.message(F.text == 'начать игру легко 🍉')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🍉'
    word_list = words_ez.WORDS_EZ
    await message.answer('🍉 выбери кол-во участников:',
                         reply_markup=kb.catalog)

@user.message(F.text == 'начать игру интересно 🍥')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🍥'
    word_list = phrases.PHRASES
    await message.answer('🍥 выбери кол-во участников:',
                         reply_markup=kb.catalog)

@user.message(F.text == 'start game english 💂‍♀️')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '💂‍♀️'
    word_list = english.ENGLISH_WORDS
    await message.answer('💂‍♀️ выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.message(F.text == 'начать игру clash royale 🃏')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🃏'
    word_list = clash_royale.clash_royale_cards
    await message.answer('🃏 выбери кол-во участников:',
                         reply_markup=kb.catalog)

@user.message(F.text == 'начать игру dota 2 🐦‍🔥')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🐦‍🔥'
    word_list = dota.dota_2_heroes
    await message.answer('🐦‍🔥 выбери кол-во участников:',
                         reply_markup=kb.catalog)

@user.message(F.text == 'начать игру персонажи 👀')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '👀'
    word_list = people.PEOPLE_WORDS
    await message.answer('👀 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.message(F.text == 'начать игру кино 🎥')
async def start(message: Message):
    await message.delete()
    global word_list, smile
    smile = '🎥'
    word_list = films.MOVIES_WORDS
    await message.answer('🎥 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data.startswith('restart'))
async def cmd_hello(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(f'{smile} выбери кол-во участников:',
                         reply_markup=kb.catalog)

@user.callback_query(F.data.startswith('players'))
async def chek_pl(callback: CallbackQuery):
    await callback.message.delete()
    global spisok, num_players, n
    spisok = []
    num_players = 0
    n = 1
    num_players = int(callback.data.split('_')[1])
    first_word, sec_word = random.sample(word_list, 2)
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
    await callback.message.answer(f'`{n}` игрок',
    reply_markup=kb.game_show, parse_mode='Markdown')

@user.callback_query(F.data.startswith('show'))
async def chek_word(callback: CallbackQuery):
    await callback.message.delete()
    global n
    n += 1
    await callback.message.answer(f'`{n}` игрок',
    reply_markup=kb.game_show, parse_mode='Markdown')


@user.callback_query(F.data.startswith('hide'))
async def hide_word(callback: CallbackQuery):
    await callback.message.delete()
    if n < num_players:
        await callback.message.answer(f"`{n}` {spisok[n - 1]}",
                              reply_markup=kb.game_hide, parse_mode='Markdown')
    else:
        await callback.message.answer(f"`{n}` {spisok[n - 1]}",
                              reply_markup=kb.game_again, parse_mode='Markdown')

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)