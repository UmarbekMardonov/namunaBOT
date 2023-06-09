from aiogram import types
from aiogram.types import InputMediaVideo

from loader import bot, dp
from aiogram.dispatcher.filters import Text
from insta import instadownloader


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media_insta(message: types.Message):
    link = message.text
    link1 = '<a href="https://t.me/Yukla_video_1_bot/">Video Yukla Bot</a> orqali yuklab olindi'
    data = instadownloader(link=link)
    if data == 'Bad':
        await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
    else:
        if data['type'] == 'video':
            await bot.send_video(chat_id=message.from_user.id, video=data['media'],
                                 caption=link1,
                                 parse_mode='HTML')
        elif data['type'] == 'image':
            await bot.send_photo(chat_id=message.from_user.id, photo=data['media'],
                                 caption=link1,
                                 parse_mode='HTML')
        elif data['type'] == 'carousel':
            for i in data['media']:
                await bot.send_document(chat_id=message.from_user.id, document=data['media'],
                                        caption=link1,
                                        parse_mode='HTML')
        else:
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
