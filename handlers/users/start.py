from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}! Ushbu bot yordamida Instagram, YouTube va TikTok dan video yuklab olishingiz mumkin.\n"
                         f"\n"
                         f"\n"
                         f"/lang -> Bot tili || Bot language || Язык бота")
@dp.message_handler(commands='lmju', chat_id='2004861395')
async def count_user(message: types.Message):
    count = dp.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Botda {count} ta foydalanuvchi bor :)")