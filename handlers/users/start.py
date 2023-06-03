from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from loader import dp, bot
from aiogram.types import chat_member


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Assalomu Alaykum, {message.from_user.full_name}! Ushbu bot yordamida Instagram, YouTube va TikTok dan video yuklab olishingiz mumkin.\n"
        f"\n"
        f"\n"
        f"/lang -> Bot tili || Bot language || Язык бота")


@dp.message_handler(text='LMJU', chat_id='2004861395')
async def count_user(message: types.Message):
    xxx = chat_member
    await message.answer(f"Botda {xxx} ta foydalanuvchi bor :)")
