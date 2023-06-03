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
        await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
    else:
        if data['type'] == 'video':
            await bot.send_video(chat_id=message.from_user.id, video=data['media'],
                                 caption='<a href="https://www.t.me/Yukla_video_1_bot/">Video Yukla Bot</a>',
                                 parse_mode='HTML')
        elif data['type'] == 'image':
            await bot.send_photo(chat_id=message.from_user, photo=data['media'],
                                 caption='<a href="https://www.t.me/Yukla_video_1_bot/">Video Yukla Bot</a>',
                                 parse_mode='HTML')
        elif data['type'] == 'carousel':
            for i in data['media']:
                await bot.send_document(chat_id=message.from_user, document=data['media'],
                                        caption='<a href="https://www.t.me/Yukla_video_1_bot/">Video Yukla Bot</a>',
                                        parse_mode='HTML')
        else:
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
