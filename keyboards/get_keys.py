from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB
from main_utils import *



def gen_btn_key(user_id):
    main_keyboard = IB()
    user = get_user(user_id)
    
    if user:
        referrals = get_referrals(user['referral_code'])

        if referrals != 0:
            if referrals == 2:
                callback_data = "True"
                
            elif referrals % 5 == 0:
                callback_data = "True"
            else:
                refferals = int(5 - referrals // 5)
                callback_data = "False"
        else:
            callback_data = "none"
    
    #make sure the key is issued only once
    
    main_keyboard.row(types.InlineKeyboardButton(text="Получить ключ🎁", callback_data=callback_data))
    return main_keyboard 

