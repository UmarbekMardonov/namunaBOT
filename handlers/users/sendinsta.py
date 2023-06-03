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
            video = InputMediaVideo(data['video'],caption="@yukla_video_1_bot")
            await message.answer_media_group(media=[video])
        elif data['type'] == 'image':
            image = InputMediaVideo(data['image'], caption="@yukla_video_1_bot")
            await message.answer_media_group(media=[image])
         elif data['type'] == 'carousel':
            for i in data['media']:
                i = InputMediaVideo(data['carousel'], caption="@yukla_video_1_bot")
                await message.answer_media_group(media=[i])
        else:
            await message.answer("Bu link orqali hech narsa topilmadi 😔 \n @yukla_video_1_bot")
