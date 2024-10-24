import asyncio

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from loader import bot
from handlers import dp

async def main():
    print("Start....")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())

