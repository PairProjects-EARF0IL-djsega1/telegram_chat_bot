from os import environ
from asyncio import get_event_loop
from logging import basicConfig, INFO
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv
from redis import Redis

from handlers import register

load_dotenv()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
redis_connection = Redis(host=environ.get("REDIS_HOST"),
                             port=int(environ.get("REDIS_PORT")),
                             password=environ.get("REDIS_PASSWORD"),
                             db=0)


async def stop_bot(*args, **kwargs):
    redis_connection.close()


async def main():
    bot = Bot(environ.get("BOT_TOKEN"))

    storage = RedisStorage(redis_connection)
    dispatcher = Dispatcher(storage=storage)
    dispatcher.include_router(register.router)
    dispatcher.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    basicConfig(level=INFO)
    asyncio.run(main())
