from aiogram import Bot, Dispatcher

import datetime,time

from decouple import config

API_TOKEN = config('API_TOKEN')

# bot = Bot(token=API_TOKEN)

import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold



dp = Dispatcher()


users = []

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, доступные комманды /hello, /time!")
    
    
    
@dp.message(Command("hello"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    
    
    
    
@dp.message(Command("time"))
async def command_time_handler(message: Message) -> None:
    time = datetime.datetime.now()
    await message.answer(str(time))


@dp.message()
async def message_handler(message: types.Message) -> None:
    await message.answer('Я не розумію вас. Доступні команди: /hello, /time')



async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())