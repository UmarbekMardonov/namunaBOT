from aiogram import types
from aiogram.types import InputMediaVideo

from loader import bot, dp
from aiogram.dispatcher.filters import Text
from insta import instadownloader


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media_insta(message: types.Message):
    link = message.text
    data = instadownloader(link=link)
    if data == 'Bad':
        await message.answer("Bu link orqali hech narsa topilmadi 😔 \n @yukla_video_1_bot")
    else:
        if data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=data['media'])
        else:
            await message.answer("Bu link orqali hech narsa topilmadi 😔 \n @yukla_video_1_bot")
