from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import saver_callback

aiogram_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎥 360p", callback_data="360"),
        InlineKeyboardButton(text="🎥 720p", callback_data="720"),
        InlineKeyboardButton(text="🎥 1080p", callback_data="1080"),
    ],
    [
        InlineKeyboardButton(text="🔊 AUDIO", callback_data="AUDIO")
    ],
    [
        InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="bot"),
    ],
])

aiogram_key = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎥 past sifatli", callback_data="360"),
        InlineKeyboardButton(text="🎥 o'rtacha sifatli", callback_data="720"),
        InlineKeyboardButton(text="🎥 yuqori sifatli", callback_data="1080"),
    ],
    [
        InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="bot"),
    ],
])
