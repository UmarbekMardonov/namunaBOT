from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbek"),
            KeyboardButton(text="English"),
            KeyboardButton(text="Русский"),
        ]
    ]
)
