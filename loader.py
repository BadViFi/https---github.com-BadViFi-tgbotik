from decouple import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


API_TOKEN = config('API_TOKEN')


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()