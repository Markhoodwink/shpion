from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart
import random, kb
import words, phrases, words_ez, people, films, english, clash_royale, dota, brends, math_formuls
user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать 🕵️‍♀️\n\nВыберите тип игры:', reply_markup=kb.restart)

@user.callback_query(F.data == 'diff_hard')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = words.WORDS_HARD
    await callback.message.answer('🎃 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_easy')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = words_ez.WORDS_EZ
    await callback.message.answer('🍉 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_int')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = phrases.PHRASES
    await callback.message.answer('🍥 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_eng')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = english.ENGLISH_WORDS
    await callback.message.answer('💂‍♀️ выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_royale')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = clash_royale.clash_royale_cards
    await callback.message.answer('🃏 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_dota')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = dota.dota_2_heroes
    await callback.message.answer('🐦‍🔥 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_persons')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = people.PEOPLE_WORDS
    await callback.message.answer('👀 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_cinema')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = films.MOVIES_WORDS
    await callback.message.answer('🎥 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_brends')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = brends.brands
    await callback.message.answer('💰 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data == 'diff_math')
async def start(callback: CallbackQuery):
    await callback.message.delete()
    global word_list
    word_list = math_formuls.math_concepts
    await callback.message.answer('📐 выбери кол-во участников:',
                         reply_markup=kb.catalog, parse_mode='Markdown')

@user.callback_query(F.data.startswith('restart'))
async def cmd_hello(callback: CallbackQuery):
    global type_of_game, id
    type_of_game = callback.data.split('_')[1]
    await callback.message.delete()
    await callback.message.answer('начать игру:', reply_markup=kb.menu)

@user.callback_query(F.data.startswith('choose_type'))
async def cmd_hello(callback: CallbackQuery):
    await callback.message.delete()
    my_list = list(range(1, num_players + 1))
    random.shuffle(my_list)
    l = ' '.join(str(x) for x in my_list)
    await callback.message.answer(f'{l} `{" - порядок"}`\n\nВыбери тип игры 🕵️‍♀️:',
                         reply_markup=kb.restart, parse_mode='Markdown')

@user.callback_query(F.data.startswith('players'))
async def chek_pl(callback: CallbackQuery):
    await callback.message.delete()
    global spisok, num_players, n
    spisok = []
    n = 1
    num_players = int(callback.data.split('_')[1])
    if type_of_game == 'nobody':
        first_word, sec_word = random.sample(word_list, 2)
    else:
        first_word = random.choice(word_list)
        sec_word = 'ТЫ ШПИОН 🥷'
    for i in range(num_players):
        spisok.append(first_word)
    if num_players < 5:
        ind  = random.randint(0, num_players - 1)
        spisok[ind] = sec_word
    elif num_players < 8:
        ind1, ind2 = random.sample(range(0, num_players - 1), 2)
        spisok[ind1] = sec_word
        spisok[ind2] = sec_word
    else:
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