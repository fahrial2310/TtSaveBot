import os

class config(object):
  bot_name = os.environ.get("bot_name", "Alvinttsavebot")
  bot_username = os.environ.get("bot_username", "Alvinttsavebot")
  
# for owner development 
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
  owner_dev = os.environ.get("owner_dev", "@sengklek_ais")
  BOT_TOKEN = "6713777196:AAH2nhHvxA61iceQfZZccNJ6jkwSGQ2mc-0"

