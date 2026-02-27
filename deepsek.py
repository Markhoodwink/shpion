import os
import logging
import random
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN_HERE")  # лучше положить токен в env var
bot = Bot(token="8441365299:AAHzbJYH3SY2yAtOB73ydso9mWepgqRmJuM")
dp = Dispatcher()

# Простой словарь — можно расширить
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

# Сессии в памяти: chat_id -> session
# session = {
#   'players': int,
#   'assignments': [word_for_player0, ...],
#   'current': int,
#   'awaiting_hide': bool,
#   'words': {'A': wordA, 'B': wordB}
# }
game_sessions = {}


def make_players_keyboard() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=4)
    buttons = [types.InlineKeyboardButton(text=str(i), callback_data=f"set_players:{i}") for i in range(3, 9)]
    kb.add(*buttons)
    return kb


def make_main_keyboard(state_waiting_hide: bool) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    if not state_waiting_hide:
        kb.add(types.InlineKeyboardButton(text="Готов", callback_data="action:ready"))
    else:
        kb.add(types.InlineKeyboardButton(text="Спрятать", callback_data="action:hide"))
    kb.add(types.InlineKeyboardButton(text="Завершить игру", callback_data="action:end"))
    return kb


@dp.message(Command(commands=["start", "help"]))
async def cmd_start(message: types.Message):
    text = (
        "Привет! Я бот для раздачи слов в игре «Шпион» на одном устройстве.\n\n"
        "Команды:\n"
        "/newgame — начать новую игру\n"
        "/end — завершить текущую игру\n\n"
        "Нажмите /newgame, чтобы начать."
    )
    await message.answer(text)


@dp.message(Command(commands=["newgame"]))
async def cmd_newgame(message: types.Message):
    await message.answer("Выберите количество игроков (3–8):", reply_markup=make_players_keyboard())


@dp.callback_query(Text(startswith="set_players:"))
async def process_set_players(cb: types.CallbackQuery):
    # убираем "часики"
    await cb.answer()
    chat = cb.message.chat
    chat_id = chat.id

    try:
        n = int(cb.data.split(":", 1)[1])
    except Exception:
        await cb.message.answer("Неправильное значение игроков.")
        return

    if not (3 <= n <= 8):
        await cb.message.answer("Количество игроков должно быть от 3 до 8.")
        return

    a, b = random.sample(VOCAB, 2)
    first_count = 1 if n <= 4 else 2
    assignments = [a] * first_count + [b] * (n - first_count)
    random.shuffle(assignments)

    game_sessions[chat_id] = {
        'players': n,
        'assignments': assignments,
        'current': 0,
        'awaiting_hide': False,
        'words': {'A': a, 'B': b}
    }

    # Отправляем/редактируем основное сообщение — теперь показываем кнопку "Готов"
    await cb.message.edit_text(
        f"Игра запущена для {n} игроков.\n\nИгрок 1 из {n}. Нажмите «Готов», когда будете готовы.",
        reply_markup=make_main_keyboard(False)
    )


@dp.callback_query(Text(startswith="action:"))
async def process_action(cb: types.CallbackQuery):
    # гасим спиннер
    await cb.answer()
    chat = cb.message.chat
    chat_id = chat.id
    action = cb.data.split(":", 1)[1]

    session = game_sessions.get(chat_id)
    if not session:
        # нет активной игры
        try:
            await cb.message.edit_text("Нет запущенной игры. Нажмите /newgame чтобы начать.")
        except Exception:
            pass
        return

    if action == "ready":
        if session['awaiting_hide']:
            await cb.answer("Сначала спрячьте текущее слово (нажмите «Спрятать»).", show_alert=False)
            return

        idx = session['current']
        n = session['players']
        if idx >= n:
            await cb.answer("Все слова уже выданы. Нажмите /newgame, чтобы начать заново.", show_alert=False)
            return

        word = session['assignments'][idx]
        # показываем слово только пользователю, который нажал (всплывающее окно)
        await cb.answer(text=f"Ваше слово:\n\n«{word}»", show_alert=True)

        # меняем основное сообщение — показываем кнопку "Спрятать"
        await cb.message.edit_text(
            f"Игрок {idx+1} просмотрел слово. Нажмите «Спрятать», когда будете готовы передать устройство следующему.",
            reply_markup=make_main_keyboard(True)
        )
        session['awaiting_hide'] = True
        return

    if action == "hide":
        if not session['awaiting_hide']:
            await cb.answer("Слово ещё не показывали. Нажмите «Готов», чтобы получить слово.", show_alert=False)
            return

        idx = session['current']
        n = session['players']
        session['current'] += 1
        session['awaiting_hide'] = False

        if session['current'] >= n:
            a = session['words']['A']
            b = session['words']['B']
            await cb.message.edit_text(
                f"Ход игрока {idx+1} завершён.\n\nВсе слова выданы.\n\nСлова в этой игре были:\n• {a}\n• {b}\n\nЕсли хотите — нажмите /newgame для новой игры.",
                reply_markup=None
            )
            # удаляем сессию
            del game_sessions[chat_id]
            return
        else:
            next_idx = session['current']
            await cb.message.edit_text(
                f"Ход игрока {idx+1} завершён.\n\nИгрок {next_idx+1} из {n}. Нажмите «Готов», когда будете готовы.",
                reply_markup=make_main_keyboard(False)
            )
            return

    if action == "end":
        if chat_id in game_sessions:
            del game_sessions[chat_id]
        await cb.message.edit_text("Игра принудительно завершена. Нажмите /newgame чтобы начать новую.", reply_markup=None)


@dp.message(Command(commands=["end"]))
async def cmd_end(message: types.Message):
    chat_id = message.chat.id
    if chat_id in game_sessions:
        del game_sessions[chat_id]
        await message.answer("Игра завершена.")
    else:
        await message.answer("Активной игры нет.")


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())