import os
from tiktok_downloader import snaptik
from moviepy import editor
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script
from config import config
from creator_only import config

import telebot

# get your bot token on @BotFather
BOT_TOKEN = "7086014869:AAHmiOpuyrzga0xS8Ol4VTSVnlkgrj_GNNc"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(chat_id=message.chat.id,
                     text=script.START_MSG.format(message.from_user.mention),
                     disable_web_page_preview=True,
                     reply_markup=InlineKeyboardMarkup(
                         [
                             [
                                 InlineKeyboardButton("Creator", url={CREATOR}),
                                 InlineKeyboardButton("Repo", url={REPO}),
                             ],
                             ),
                    ),

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
  
