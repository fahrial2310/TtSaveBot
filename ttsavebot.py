# don't edit
CREATOR = "Rii?"
CREATOR_LINK = "t.me/sengklek_ais"
REPO = "https://github.com/fahrial2310/TtSaveBot"
# don't edit

# can edit
BOT_NAME = "Alvinttsavebot"  
BOT_USERNAME = "Alvinttsavebot"
OWNER_LINK = "t.me/sengklek_ais"
# for owner development(owner_dev)
# delete None and change with telegram username without @, example "sengklek_ais"
# Don't forget to use the " sign
OWNER_DEV = "sengklek_ais"
# can edit

# edit text here
class script(object):
  ERROR_MSG = """ ❌ Upload error, link salah, video dihapus atau aku tidak bisa menemukannya."""
  START_MSG = f"""👋 Halo, saya adalah {BOT_NAME}.
  Saya akan membantu anda untuk mengunduh video <b>TikTok</b>.
  /help - untuk bantuan menggunakan bot.
  
  <b>Creator :</b> <a href='{CREATOR_LINK}'>{CREATOR}</a>
  <b>Developing by :</b> @{OWNER_DEV} """
  HELP_MSG = """❓ Kirim link untuk mengunduh video dari <b>TikTok</b>.
  <b>Link harus dimulai dari:</b>
  🔗 https://vt.tiktok.com/... """
  ABOUT_MSG = f"""{BOT_NAME} adalah bot telegram yang dapat mengunduh video <b>Tiktok</b>.
  Kirim link TikTok maka akan dikonversikan menjadi video.
  
  Klik tombol repo untuk membuat bot."""
  LOST_MSG = """  😕 Aku tidak mengerti, tolong kirimkan link <b>TikTok</b>. 
  /help jika butuh bantuan. """
# edit text here

import os
from tiktok_downloader import snaptik
from moviepy import editor
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import telebot

# get your bot token on @BotFather
BOT_TOKEN = "7143183623:AAEns2ba5tBwVWO-b96E9dinw5p1lMkXZII"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
  bot.send_message(chat_id=message.chat.id,
                   text=script.START_MSG,
                   parse_mode='html',
                   disable_web_page_preview=True,
                   reply_markup=InlineKeyboardMarkup(
                     [
                       [
                         InlinekeyboardButton("Help", callback_data="help_data")
                       ],
                       [
                         InlineKeyboardButton("About", callback_data="about_data")
                       ],
                     ],
                   ))

@bot.message_handler(commands=['about'])
def about_command(message):
  bot.send_message(chat_id=message.chat.id,
                   text=script.ABOUT_MSG,
                   parse_mode='html',
                   desable_web_page_preview=True,
                   reply_markup=InlineKeyboardMarkup(
                     [
                       [
                         InlineKeyboardButton("Start" , callabck_data="start_data"),
                         InlineKeyboardButton("Help" , callback_data="help_data")
                       ],
                       [
                         InlineKeyboardButton("Creator", url=f"{CREATOR_LINK}"),
                         InlineKeyboardButton("Repo", url=f"{REPO}")
                       ],
                     ],
                   ))
  
@bot.message_handler(commands=['help'])
def help_command(message):
  bot.send_message(chat_id=message.chat.id, 
                   text=script.HELP_MSG, 
                   parse_mode='html', 
                   desable_web_page_preview=True, 
                   reply_markup=InlineKeyboardMarkup(
                     [
                       [
                         InlineKeyboardButton("About", callback_data="about_data")
                       ],
                       [
                         InlineKeyboardButton("◀ Back", callback_data="start_data")
                       ],
                     ],
                   ))


if not os.path.exists('videos'):
    os.makedirs('videos')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == "private":
        if message.text.startswith('https://vt.tiktok.com') or message.text.startswith('http://vt.tiktok.com'):
            video_url = message.text

            try:
                bot.send_message(chat_id=message.chat.id, text='⏳ mohon menunggu...')

                snaptik(f"{video_url}").get_media()[0].download_media(f"./videos/result_/{message.from_user.id}.mp4")
                path = f"./videos/result_/{message.from_user.id}.mp4"
                
                with open(f"./videos/result_/{message.from_user.id}.mp4", "wb") as file:
                    bot.send_video(
                    chat_id=message.chat.id,
                    video=file,
                    caption=f"{video_url}\n\n Diunduh dari @{BOT_USERNAME}"
                    )
                os.remove(path)

            except:
                bot.send_message(chat_id=message.chat.id, text=script.ERROR_MSG)
               
        else:
            bot.send_message(chat_id=message.chat.id, 
                            text=script.LOST_MSG, 
                            parse_mode='html')

if __name__ == "__main__":
    bot.polling(non_stop=True)
  
