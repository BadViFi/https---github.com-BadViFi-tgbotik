from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB
from main_utils import *



def gen_btn_key(user_id):
    main_keyboard = IB()
    user = get_user(user_id)
    print(user)
    
    if user:
        keys = user['keys']
        print(keys)
        if keys > 0:
            if keys == 3:
                callback_data =  "True"
        else:
            callback_data = "none"
            # if keys == 1:
            #     callback_data = "True"
                
            # elif keys % 5 == 0:
            #     callback_data = "True"
            # else:
            #     refferals = int(5 - keys // 5)
            #     callback_data = "False"

    #make sure the key is issued only once
    
    main_keyboard.row(types.InlineKeyboardButton(text="Получить ключ🎁", callback_data=callback_data))
    return main_keyboard 

