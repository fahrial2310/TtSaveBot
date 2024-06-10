import os

class config(object):
  bot_name = os.environ.get("bot_name", "Alvinttsavebot")
  bot_username = os.environ.get("bot_username", "Alvinttsavebot")
  owner_dev = os.environ.get("owner_dev", "@sengklek_ais")
  BOT_TOKEN = os.environ.get("BOT_TOKEN","6713777196:AAH2nhHvxA61iceQfZZccNJ6jkwSGQ2mc-0")

# for owner development(owner_dev)
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
