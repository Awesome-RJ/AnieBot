from sys import exit

import AnieBot.utils
from AnieBot import TOKEN, tbot

try:
    tbot.start(bot_token=TOKEN)
except Exception:
    print("Token Invalid.")
    exit(1)


tbot.run_until_disconnected()
