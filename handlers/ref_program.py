from aiogram import Router,F,types


from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from decouple import config
from pathlib import Path

from keyboards.get_keys import gen_btn_key
from main_utils import *


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    referral_code = f"{user_id}"
    referral_link = f"http://t.me/Superskins_bot?start={user_id}"
    args = message.text.split()

    user = get_user(user_id)

    if user is None:  
        if len(args) > 1:
            referred_by = args[1]
            referred_user = get_user(int(referred_by))
            if referred_user:
                add_user(user_id, referral_code, referred_by)
                add_key_to_user(int(referred_by))  
                await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Вы зарегистрированы. Вот ваша реферальная ссылка: {referral_link}. Вы были приглашены пользователем с ID {referred_by}.")
            else:
                await message.answer("Неверный реферальный код.")
        else:
            add_user(user_id, referral_code)
            await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Вы зарегистрированы. Вот ваша реферальная ссылка: {referral_link}.")
    else:
        await message.answer(f"Вы уже зарегистрированы. Вот ваша реферальная ссылка: {referral_link}.")


@router.message(Command("key"))
async def give_key(message: Message) -> None:
    markup = gen_btn_key(message.from_user.id)

    photo_path = Path('DALLE_2024-10-24_16.01.02_-_A_dynamic_digital_poster_with_a_logo_inspired_by_the_Steam_logo_featuring_the_text_Free_Key_in_bold_futuristic_lettering._The_background_shows_cha.webp')
    photo = types.FSInputFile(str(photo_path))
    
    
    await message.answer_photo(photo, caption="1 реферал - 1 ключ, 5 рефералов - 1 ключ", reply_markup=markup.as_markup())

@router.message(Command("help"))
async def support(message: Message) -> None:
    await message.answer("По вопросам пишите сюда - https://t.me/freesteamacoounts_bot")



    

@router.message(Command("referrals"))
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


    
    
@router.callback_query(F.data.startswith("True"))
async def courses_handler(call: types.CallbackQuery):
    await call.message.answer("ok")