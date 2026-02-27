from aiogram import Bot, Dispatcher
from hand_2 import user

async def main():
    print("Запуск...")
    bot = Bot(token='8782062863:AAE95PVHH94D5y7rJvtS45iJklRZnwsml3s')
    dp = Dispatcher()
    dp.include_router(user)
    print("БОТ ЗАПУЩЕН! Нажмите Ctrl+C для остановки")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(),
        poll_timeout=10 )

if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass