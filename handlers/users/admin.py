from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/message", user_id=2004861395)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="...")



