import os

class config(object):
  BOT_NAME = os.environ.get("BOT_NAME", "Alvinttsavebot")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alvinttsavebot")
# for owner development(owner_dev)
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
  OWNER_DEV = os.environ.get("OWNER_DEV", "@sengklek_ais")

# get your bot token on @BotFather
  BOT_TOKEN = "7086014869:AAHmiOpuyrzga0xS8Ol4VTSVnlkgrj_GNNc"
