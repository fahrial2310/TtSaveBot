import os

class Config(object):
  BOT_NAME = os.environ.get("BOT_NAME", "Alvinttsavebot")
  
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alvinttsavebot")

  OWNER_LINK = os.environ.get("OWNER_LINK", "t.me/sengklek_ais")

  OWNER_DEV = os.environ.get("OWNER_DEV", "@sengklek_ais")
# for owner development(owner_dev)
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign
  
# add bot token in ttsavebot.py file
