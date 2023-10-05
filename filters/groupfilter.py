from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroupo(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )
