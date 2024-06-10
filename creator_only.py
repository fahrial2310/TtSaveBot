import os

class Config(object):
  CREATOR = os.environ.get("CREATOR", "@sengklek_ais")
  CREATOR_LINK = os.environ.get("CREATOR_LINK", "t.me/sengklek_ais")
  REPO = os.environ.get("REPO", "https://github.com/fahrial2310/TtSaveBot")
