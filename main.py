from os import environ
from asyncio import get_event_loop
from logging import basicConfig, INFO
from aiogram import Bot, Dispatcher
from dotenv import  load_dotenv

load_dotenv()


async def main():
    pass


if __name__ == '__main__':
    basicConfig(level=INFO)
    get_event_loop().run_until_complete(main())