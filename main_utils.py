import os
from aiogram import types



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






