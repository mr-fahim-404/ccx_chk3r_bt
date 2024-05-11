from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("7148878016:AAGUDd6Pe9HYDD2cEiHBG0bNxlTPS5DMwIk"))
API_HASH = input("3a730e2ea3e1f1aac71d268cc5244014") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
