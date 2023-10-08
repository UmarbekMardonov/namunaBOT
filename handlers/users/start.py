import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests

from data.config import ADMINS
from keyboards.inline.main_menu_super_admin import main_menu_for_admin, main_menu_for_super_admin
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    count = await db.count_users()
    msg = f"{user[1], user[3]}, @{user[2]} bazaga qo'shildi :). \n Bazada {count} ta foydalanuvchi bor!"
    await bot.send_message(chat_id=2004861395, text=msg)
    if message.from_user.id == 2004861395:
        await message.answer(f"Assalomu Alaykum Admin, {message.from_user.full_name}!.",
                             reply_markup=main_menu_for_super_admin)
    else:
        await message.answer(
            f"Assalomu Alaykum, {message.from_user.full_name}☺️! \nUshbu bot yordamida Instagram dan video va rasm yuklab olishingiz mumkin.\n"
            f"Menga video yoki rasm linkini yuboring👇")
