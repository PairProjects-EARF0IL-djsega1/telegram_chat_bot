from os import environ
from asyncio import get_event_loop
from logging import basicConfig, INFO
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import register

load_dotenv()


async def main():
    bot = Bot(environ.get("BOT_TOKEN"))
    dispatcher = Dispatcher()
    print_hello_world()
    dispatcher.include_router(register.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    basicConfig(level=INFO)
    loop = get_event_loop()
    loop.run_until_complete(main())
