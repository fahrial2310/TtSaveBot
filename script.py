from config import Config
from creator_only import Config

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
