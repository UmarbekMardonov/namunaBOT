from states.menuKeybords import menu
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, Message
from loader import dp


@dp.message_handler(Command("lang"))
async def show_menu(message: Message):
    await message.answer("Tilni tanlang || Choose a language || Выберите язык", reply_markup=menu)


@dp.message_handler(text="O'zbek 🇺🇿")
async def link_send(message: Message):
    await message.answer("Men ishlashim uchun menga Instagram, YouTube va TikTok dan "
                         "video link yuboring", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="English 🇬🇧")
async def link_send2(message: Message):
    await message.answer("Send me a video or photo link from Instagram"
                         " for me to work on",  reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Русский 🇷🇺")
async def link_send3(message: Message):
    await message.answer("Из Instagram, YouTube и TikTok отправить ссылку на видео"
                         " мне на работу",  reply_markup=ReplyKeyboardRemove())
