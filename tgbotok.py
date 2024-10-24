from aiogram import Bot, Dispatcher
import os
import asyncio
import logging
import sys
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import InlineKeyboardBuilder
from decouple import config
from pathlib import Path

API_TOKEN = config('API_TOKEN')

dp = Dispatcher()

def add_user(user_id, referral_code, referred_by=None):
    with open('users.txt', 'a') as f:
        f.write(f"{user_id},{referral_code},{referred_by}\n")

def get_user(user_id):
    if not os.path.exists('users.txt'):
        return None
    with open('users.txt', 'r') as f:
        for line in f:
            uid, referral_code, referred_by = line.strip().split(',')
            if int(uid) == user_id:
                return {
                    'user_id': int(uid),
                    'referral_code': referral_code,
                    'referred_by': int(referred_by) if referred_by != 'None' else None

                }
    return None

def get_referrals(referral_code):
    referrals = 0
    if not os.path.exists('users.txt'):
        return referrals
    with open('users.txt', 'r') as f:
        for line in f:
            if len(line) > 1:
                uid, user_referral_code, referred_by = line.strip().split(',')
                if referred_by == referral_code[4:]:
                    referrals += 1


    return referrals

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    referral_code = f"ref_{user_id}"
    args = message.text.split()

    if get_user(user_id) is None:
        if len(args) > 1:
            referred_by = args[1]
            referred_user = get_user(int(referred_by))
            if referred_user:
                add_user(user_id, referral_code, referred_by)
                await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Вы зарегистрированы с реферальным кодом {referral_code}. Вы были приглашены пользователем с ID {referred_by}.")
            else:
                await message.answer("Неверный реферальный код.")
        else:
            add_user(user_id, referral_code)
            await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Вы зарегистрированы с реферальным кодом {referral_code}.")
    else:
        await message.answer("Вы уже зарегистрированы.")

@dp.message(Command("referrals"))
async def view_referrals(message: Message) -> None:
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        referrals = get_referrals(user['referral_code'])

        if referrals != 0:
        
            await message.answer(f"количество рефералов - {referrals} ")
        else:
            await message.answer("У вас пока нет рефералов.")
    else:
        await message.answer("Вы еще не зарегистрированы в системе.")

def gen_button_orders_list(user_id):
    markup = InlineKeyboardBuilder()
    user = get_user(user_id)
    
    # if user:
    #     referrals = get_referrals(user['referral_code'])

    #     if referrals != 0:
    #         if referrals == 1:
    #             callback_data = True
                
    #         elif referrals % 5 == 0:
    #             callback_data = True
    #         else:
    #             refferals = int(5 - referrals // 5)
    #             callback_data = False
    #     else:
    #         callback_data = "none"
    #make sure the key is issued only once
    
    markup.row(types.InlineKeyboardButton(text="Получить ключ🎁", callback_data="present"))
    return markup 

@dp.message(Command("key"))
async def give_key(message: Message) -> None:
    markup = gen_button_orders_list(message.from_user.id)

    photo_path = Path('path_to_your_image.jpg')
    photo = types.FSInputFile(str(photo_path))
    
    
    await message.answer_photo(photo, caption="1 реферал - 1 ключ, 5 рефералов - 1 ключ", reply_markup=markup.as_markup())

@dp.message(Command("help"))
async def support(message: Message) -> None:
    await message.answer("По вопросам пишите сюда - https://t.me/freesteamacoounts_bot")






async def main() -> None:
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
