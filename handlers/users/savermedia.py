import json
from keyboards.inline.courses import aiogram_keys, aiogram_key
import aiogram.utils.exceptions
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ChatActions, InputFile, Message, CallbackQuery, ReplyKeyboardRemove, message
from insta import instadownloader
from loader import bot, dp
from youtube import youtube
from tiktok import Downloads


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media_insta(message: types.Message):
    link = message.text
    xxx = await message.answer(text='Yuklanmoqda 🔍')
    data = await Downloads.instagram_1(link=link)
    x = data['result'][0]
    media = x['url']
    link1 = f"\n" \
            f"\n" \
            '🤖 @rapidsaverbot '
    try:

        if data == 'Bad':
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
        else:
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await bot.send_document(chat_id=message.from_user.id, document=media,
                                    caption=link1)
        await xxx.delete()
        """    await xxx.delete()
            elif data['type'] == 'image':
                await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_PHOTO)
                await bot.send_photo(chat_id=message.from_user.id, photo=data['media'],
                                     caption=link1)
                await xxx.delete()
            elif data['type'] == 'carousel':
                await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_PHOTO)
                for i in data['media']:
                    await bot.send_document(chat_id=message.from_user.id, document=i,
                                            caption=link1)
            else:
                await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
        await xxx.delete() """
    except aiogram.utils.exceptions.InvalidHTTPUrlContent:
        await message.answer("Bu linkda hech qanday post topilmadi😞\n"
                             "Iltimos boshqa link yuboring👇")


@dp.message_handler(Text(startswith='https://youtu'))
async def send_media_youtube(message: types.Message):
    global context
    link = message.text
    load = await message.answer(text='Yuklanmoqda 🔍')
    data = youtube(link=link)
    if data['360videoSize'] or data['720videoSize'] or data['1080videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   360p:  {data['360videoSize']} \n" \
                  f"📺   720p:  {data['720videoSize']} \n" \
                  f"📺   1080p: {data['1080videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    if data['360videoSize'] or data['720videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   360p:  {data['360videoSize']} \n" \
                  f"📺   720p:  {data['720videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    if data['360videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   360p:  {data['360videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    if data['720videoSize'] or data['1080videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   720p:  {data['720videoSize']} \n" \
                  f"📺   1080p: {data['1080videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    if data['1080videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   1080p: {data['1080videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    if data['720videoSize']:
        context = f"🎥 {data['title']} \n" \
                  f"👤 {data['desc']}\n" \
                  f"\n" \
                  f"📺   720p:  {data['720videoSize']} \n" \
                  f"\n" \
                  f"Yuklab olish uchun o'zizga qulay formatni tanlang 👇"
    try:
        if data == 'Bad':
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
        else:
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_PHOTO)
            x1 = await bot.send_photo(chat_id=message.from_user.id, photo=data['mediaAvatar'],
                                      reply_markup=aiogram_keys,
                                      caption=context,
                                      parse_mode='HTML')
            # else:
            #   await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
        await load.delete()
    except aiogram.utils.exceptions.InvalidHTTPUrlContent:
        await message.answer("Bu linkda hech qanday post topilmadi😞\n"
                             "Iltimos boshqa link yuboring👇")

    @dp.callback_query_handler()
    async def send_video(call: types.CallbackQuery):
        if call.data == '360':
            link1 = f"🎥 {data['title']} \n" \
                    f"\n" \
                    f"👤 {data['desc']}\n" \
                    f"\n" \
                    f"🤖 @rapidsaverbot  📺 {data['360videoSize']}"
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await call.message.answer_video(video=data['360video'], caption=link1)
            await x1.delete()
        if call.data == '720':
            link1 = f"🎥 {data['title']} \n" \
                    f"\n" \
                    f"👤 {data['desc']}\n" \
                    f"\n" \
                    f"🤖 @rapidsaverbot  📺 {data['720videoSize']}"
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await call.message.answer_video(video=data['720video'], caption=link1)
            await x1.delete()
        if call.data == '1080':
            link1 = f"🎥 {data['title']} \n" \
                    f"\n" \
                    f"👤 {data['desc']}\n" \
                    f"\n" \
                    f"🤖 @rapidsaverbot  📺 {data['1080videoSize']}"
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await call.message.answer_video(video=data['1080video'], caption=link1)
            await x1.delete()
        if call.data == 'AUDIO':
            if data['audio']:
                link1 = f"🎥 {data['title']} \n" \
                        f"\n" \
                        f"👤 {data['desc']}\n" \
                        f"\n" \
                        f"🤖 @rapidsaverbot"
                await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_AUDIO)
                await call.message.answer_audio(audio=data['audio'], caption=link1)
                await x1.delete()
            else:
                await message.answer(text="Bu videoni audiosi yuq")


@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def send_media_tiktok(message: types.Message):
    link = message.text
    link1 = f"\n" \
            f"\n" \
            '🤖 @rapidsaverbot '
    load = await message.answer(text='Yuklanmoqda 🔍')
    data = await Downloads.tiktok(url=link)
    try:
        if data == 'Bad':
            await message.answer("Bu link orqali hech narsa topilmadi 😔 ")
        else:
            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)
            await bot.send_video(chat_id=message.from_user.id, video=data['video2'], caption=link1)
        await load.delete()

    except aiogram.utils.exceptions.InvalidHTTPUrlContent:
        await message.answer("Bu linkda hech qanday post topilmadi😞\n"
                             "Iltimos boshqa link yuboring👇")
        await load.delete()
