import os
from aiogram import types



def add_user(user_id: int, referral_code: str, referred_by: str = None) -> None:
    with open('users.txt', 'a') as f:
        f.write(f"{user_id},{referral_code},{referred_by},0\n")





def get_user(user_id: int) -> dict[str, int | None] | None:
    if not os.path.exists('users.txt'):
        return None
    with open('users.txt', 'r') as f:
        for line in f:
            uid, referral_code, referred_by,keys = line.strip().split(',')
            if int(uid) == user_id:
                return {
                    'user_id': int(uid),
                    'referral_code': referral_code,
                    'referred_by': int(referred_by) if referred_by != 'None' else None,
                    'keys' : int(keys)
                }
    return None




def get_referrals(referral_code: str) -> int:
    referrals = 0
    if not os.path.exists('users.txt'):
        return referrals
    with open('users.txt', 'r') as f:
        for line in f:
            if len(line) > 1:
                uid, user_referral_code, referred_by,keys = line.strip().split(',')
                if referred_by == referral_code:
                    referrals += 1
    return referrals




def add_key_to_user(user_id: int) -> None:
    users = []
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as f:
            users = [line.strip().split(',') for line in f]

    for user in users:
        if int(user[0]) == user_id:
            user[3] = str(int(user[3]) + 1)  
            break

    with open('users.txt', 'w') as f:
        for user in users:
            f.write(','.join(user) + '\n')



