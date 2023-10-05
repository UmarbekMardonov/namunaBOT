from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .prefilter import IsPrivate
from .groupfilter import IsGroupo


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroupo)
    dp.filters_factory.bind(IsPrivate)

