from os import environ

from aiogram import Router
from aiogram.types import Message
from aiogram import F

router = Router()


@router.message(F.content_type.in_({'text'}))
async def echo(message: Message):
    await message.answer(message.text)
