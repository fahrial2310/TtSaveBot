import os

class config(object):
  BOT_NAME = os.environ.get("BOT_NAME", "Alvinttsavebot")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alvinttsavebot")
  BOT_TOKEN = os.environ.get("BOT_TOKEN","7086014869:AAHJCpJ2vHqbSp32tVFqOkKdtsmE461pIVo")
# for owner development(owner_dev)
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
  OWNER_DEV = os.environ.get("OWNER_DEV", "@sengklek_ais")
