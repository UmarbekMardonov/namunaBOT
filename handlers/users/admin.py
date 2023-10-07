from datetime import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, back_to_main_menu
from loader import dp, db, bot
from states.admin_state import SuperAdminState


@dp.message_handler(text="/cleandb", user_id=2004861395)
async def delete_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="/ads", user_id=2004861395)
async def send_ads_all_users(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        if message.content_type == message.photo:
            file_id = message.photo[-1]['file_id']
            await bot.send_photo(chat_id=user_id, photo=file_id, caption=message.caption)
        if message.content_type == message.video:
            await bot.send_video(chat_id=user_id, video=message.video, caption=message.caption)
        if message.content_type == message.text:
            await bot.send_message(chat_id=user_id, text=message.text)
        if message.content_type == message.animation:
            await bot.send_animation(chat_id=user_id, animation=message.animation, caption=message.caption)
        time.sleep(0.5)


# Foydalanuvchilar SEND FUNC


@dp.callback_query_handler(user_id=2004861395, text="send_advertisement", state="*")
async def send_advertisement(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Reklamani yuboring...\n"
                                 "Yoki bekor qilish tugmasini bosing", reply_markup=back_to_main_menu)
    await SuperAdminState.SUPER_ADMIN_STATE_GET_ADVERTISEMENT.set()


@dp.message_handler(user_id=2004861395, state=SuperAdminState.SUPER_ADMIN_STATE_GET_ADVERTISEMENT,
                    content_types=types.ContentTypes.ANY)
async def send_advertisement_to_user(message: types.Message, state: FSMContext):
    count = await db.count_users()
    wait = await message.answer(f"📢 Reklama jo'natish boshlandi...\n"
                         f"📊 Foydalanuvchilar soni: {count} ta\n"
                         f"🕒 Kuting...\n")
    user = await db.select_all_users()
    for i in user:
        user_id = i[3]
        try:
            await bot.copy_message(chat_id=user_id, from_chat_id=message.chat.id,
                                   message_id=message.message_id, caption=message.caption,
                                   reply_markup=message.reply_markup, parse_mode=types.ParseMode.MARKDOWN)

            time.sleep(0.5)
        except Exception as e:
            print(e)

    await message.answer("✅ Reklama muvaffaqiyatli yuborildi!", reply_markup=main_menu_for_super_admin)
    await wait.delete()
    await state.finish()
# Foydalanuvchilar SEND FUNC

import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ContentTypes
from aiogram.utils import exceptions

from filters import IsSuperAdmin
from keyboards.inline.superAdminKeyboards import cancel, back
from loader import db, dp, bot


@dp.callback_query_handler(IsSuperAdmin(), text="superadmin:send_ads", state="*")
async def send_ads(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.answer("Xabarni yuboring:", reply_markup=cancel)
    await state.set_state("superadmin:ads:get")


@dp.message_handler(IsSuperAdmin(), state="superadmin:ads:get", content_types=ContentTypes.ANY)
async def send_message(message: Message):
    users = await db.select_all_table(table_name="users")

    success = 0
    removed = 0

    await message.answer(f"⚠️ Xabar {len(users)} ta foydalunvchiga yuborilmoqda...\n"
                         f"🕔 Bu jarayon bir oz vaqt olishi mumkin, iltimos kuting...")

    for user in users:
        user_id = user['telegram_id']
        try:
            await bot.copy_message(user_id, message.chat.id, message.message_id, reply_markup=message.reply_markup)
            success += 1
        except exceptions.BotBlocked:
            await db.delete(table_name='users', telegram_id=user_id)
            removed += 1
        except exceptions.ChatNotFound:
            await db.delete_user(telegram_id=user_id)
            removed += 1
        except exceptions.RetryAfter as e:
            await asyncio.sleep(e.timeout)
            await bot.copy_message(user_id, message.chat.id, message.message_id, reply_markup=message.reply_markup)
            success += 1
        except exceptions.UserDeactivated:
            await db.delete_user(telegram_id=user_id)
            removed += 1

    await message.answer(
        text=f"✅ Xabar {success} ta foydalanuvchiga yetkazildi.\n"
             f"❌ {removed} ta foydalanuvchi botdan o'chirildi."
        , reply_markup=back)