from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(Text(startswith="#reklama"), user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    reklama = message.text
    users = await db.select_all_users()
    for user in users:
        user_id = user[3]
        if message.photo:
            photo_file_id = message.photo[-1].file_id
            photo_captain = message.caption or ""
            await bot.send_photo(chat_id=user_id, photo=photo_file_id, caption=f"{reklama}\n{photo_captain}")
        else:
            await bot.send_message(chat_id=user_id, text=reklama)



