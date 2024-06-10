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
# delete None and change with telegram username, example "@sengklek_ais"
# Don't forget to use the " sign
OWNER_DEV = "@sengklek_ais"
# can edit

# edit text here
class script(object):
  ERROR_MSG = """ ❌ Upload error, link salah, video dihapus atau aku tidak bisa menemukannya."""
  START_MSG = f""" 👋 Halo, saya adalah {BOT_NAME}
  saya akan membantu anda mengunduh video <b>TikTok</b>.
  /help - bantuan untuk menggunakan bot.
  
  <b> Creator :</b> <a href='{CREATOR_LINK}'>{CREATOR}</a>
  <b> Developing by :</b> <a href='{OWNER_LINK}'>{OWNER_DEV}</a> """
  HELP_MSG = """ ❓ Untuk mengunduh video dari <b>TikTok</b>, <b>kirim</b> link ke saya.
  <b>Link harus dimulai dari:</b>
  🔗 https://vt.tiktok.com/... """
# edit text here

import os
from tiktok_downloader import snaptik
from moviepy import editor
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import telebot

# get your bot token on @BotFather
BOT_TOKEN = "7086014869:AAHmiOpuyrzga0xS8Ol4VTSVnlkgrj_GNNc"

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
                                 InlineKeyboardButton("Creator", url=f'{CREATOR_LINK}'),
                                 InlineKeyboardButton("Repo", url=f'{REPO}'),
                             ],
                         ],
                     ),
                     user.message.reply_text(message_reply_text, reply_markup=reply_markup)
                    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(chat_id=message.chat.id, 
                    text=script.HELP_MSG, 
                    parse_mode='html')


if not os.path.exists('videos'):
    os.makedirs('videos')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == "private":
        if message.text.startswith('https://vt.tiktok.com') or message.text.startswith('http://vt.tiktok.com'):
            video_url = message.text

            try:
                bot.send_message(chat_id=message.chat.id, text='⏳ mohon menunggu...')

                snaptik(f"{video_url[:31]}").get_media()[0].download(f"./videos/result_{message.from_user.id}.mp4")
                path = f'./videos/result_{message.from_user.id}.mp4'
                
                with open(f'./videos/result_{message.from_user.id}.mp4', 'wb') as file:
                    bot.send_video(
                    chat_id=message.chat.id,
                    data=file,
                    caption=f"{video_url[:31]}\n\nDownloaded from {BOT_NAME}"
                    )
                os.remove(path)

            except:
                bot.send_message(chat_id=message.chat.id, text=script.ERROR_MSG)
               
        else:
            bot.send_message(chat_id=message.chat.id, 
                            text=" 😕 I didn't understand you, send me a link to a video from Tik Tok <b>TikTok</b>.", 
                            parse_mode='html')

if __name__ == "__main__":
    bot.polling(non_stop=True)
  
