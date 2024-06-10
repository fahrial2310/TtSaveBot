import os

class config(object):
  bot_name = os.environ.get("bot_name", "Alvinttsavebot")
  bot_username = os.environ.get("bot_username", "Alvinttsavebot")
  creator = os.environ.get("creator", "@sengklek_ais")
  repo = os.environ.get("repo", "https://github.com/fahrial2310/TtSaveBot")
  
# for owner development 
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
  owner_dev = os.environ.get("owner_dev", "@sengklek_ais")
  
