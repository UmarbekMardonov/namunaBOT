from states.menuKeybords import menu
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, Message
from loader import dp


@dp.message_handler(Command("lang"))
async def show_menu(message: Message):
    await message.answer(reply_markup=menu)
