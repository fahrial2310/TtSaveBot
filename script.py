from creator_only import Config

import os

class Configs(object):
  BOT_NAME = os.environ.get("BOT_NAME", "Alvinttsavebot")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alvinttsavebot")
# for owner development(owner_dev)
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign 
  OWNER_DEV = os.environ.get("OWNER_DEV", "@sengklek_ais")
  OWNER_LINK = os.environ.get("OWNER_LINK", "t.me/sengklek_ais")

# add bot token in ttsavebot.py file

class script(object):
  ERROR_MSG = """ ❌ Upload error, link salah, video dihapus atau aku tidak bisa menemukannya."""
  START_MSG = """ 👋 Halo, saya adalah {BOT_NAME}
  saya akan membantu anda mengunduh video <b>TikTok</b>.
  /help - bantuan untuk menggunakan bot.
  
  <b> Creator :</b> <a href='{CREATOR_LINK}'>{CREATOR}</a>
  <b> Developing by :</b> <a href='{OWNER_LINK}'>{OWNER_DEV}</a> """
  HELP_MSG = """ ❓ Untuk mengunduh video dari <b>TikTok</b>, <b>kirim</b> link ke saya.
  <b>Link harus dimulai dari:</b>
  🔗 https://vt.tiktok.com/... """
