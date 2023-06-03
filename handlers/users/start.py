from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!. Ushbu bot yordamida Instagram, YouTube va TikTok dan video yuklab olishingiz mumkin."
                         f""
                         f"/lang -> Botning tili || Bot language || Язык бота")
