from random import randint

from instagrapi import Client as IClient
from instagrapi.exceptions import ChallengeRequired, TwoFactorRequired
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def main():
    print("T E A M    D A N G E R B O T S   ! !")
    print("Hello!! Welcome to DangerCat Session Generator\n")
    print("Human Verification Required !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
            print("\nChoose the string session type: \n1. DangerBot (Telethon) \n2. Instagram Session")
            while True:
                library = input("\nYour Choice: ")
                if library == "1":
                    generate_telethon_session()
                    break
                elif library == "2":
                    generate_insta_session()
                    break
                else:
                    print("Please enter integer values.")
            break
        else:
            print("Verification Failed! Try Again:")

def generate_telethon_session():
    print("\nTelethon Session For DangerCat!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as DangerBot:
        print("\nYou Session Is sent in your Telegram Saved Messages.")
        DangerBot.send_message(
            "me",
            f"#DANGERCAT #DANGERBOT_SESSION #TELETHON \n\n\n`{DangerBot.session.save()}`",
        )


def generate_insta_session():
    print("Instagram Session For DangerCat!")
    cl = IClient()
    username = input("Enter your Instagram Username: ")
    password = input("Enter your Instagram Password: ")
    try:
        cl.login(username, password)
        xyz =  cl.get_settings()
        sessionid = xyz['authorization_data']['sessionid']
        print(f"Your Instagram Session is: \n>>> {sessionid}")
        print("\nCopy it from here and remember not to share it with anyone!")
    except (ChallengeRequired, TwoFactorRequired, Exception) as e:
        print(e)


def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


main()
