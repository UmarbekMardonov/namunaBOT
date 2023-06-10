from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ChatActions, InputFile
from insta import instadownloader
from loader import bot, dp


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media_insta(message: types.Message):
    link = message.text
    xxx = await message.answer(text='⌛️')
    link1 = '🤖 <a href="https://t.me/Yukla_video_1_bot/">Video Yukla Bot</a> orqali yuklab olindi 📥'
    data = instadownloader(link=link)
    if data == 'Bad':
        await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
    else:
        if data['type'] == 'video':
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await bot.send_video(chat_id=message.from_user.id, video=data['media'],
                                 caption=link1,
                                 parse_mode='HTML')
            await xxx.delete()
        elif data['type'] == 'image':
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_PHOTO)
            await bot.send_photo(chat_id=message.from_user.id, photo=data['media'],
                                 caption=link1,
                                 parse_mode='HTML')
            await xxx.delete()
        elif data['type'] == 'carousel':
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_PHOTO)
            for i in data['media']:
                await bot.send_document(chat_id=message.from_user.id, document=i,
                                        caption=link1,
                                        parse_mode='HTML')
        else:
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
    await xxx.delete()

