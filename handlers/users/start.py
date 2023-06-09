import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests

from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    db.drop_users()
    await message.answer(
        f"Assalomu Alaykum, {message.from_user.full_name}! Ushbu bot yordamida Instagram dan video va rasm yuklab olishingiz mumkin.\n"
        f"\n"
        f"\n"
        f"/lang -> Bot tili || Bot language || Язык бота")

    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi :). \n Bazada {count} ta foydalanuvchi bor!"
    await bot.send_message(chat_id=ADMINS, text=msg)

