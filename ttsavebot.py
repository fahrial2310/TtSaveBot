import os
from tiktok_downloader import snaptik
from moviepy import editor
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script
from config import config

import telebot

TOKEN = "6713777196:AAH2nhHvxA61iceQfZZccNJ6jkwSGQ2mc-0"

bot = telebot.TeleBot(TOKEN)

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.start_msg.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Creator", url={creator}),
                        InlineKeyboardButton("repo", url={repo}),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(chat_id=message.chat.id, 
                    text=script.help_msg, 
                    parse_mode='html')


if not os.path.exists('videos'):
    os.makedirs('videos')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == "private":
        if message.text.startswith('https://vm.tiktok.com') or message.text.startswith('http://vm.tiktok.com'):
            video_url = message.text

            try:
                bot.send_message(chat_id=message.chat.id, text='⏳ mohon menunggu...')

                snaptik(f"{video_url[:31]}").get_media()[0].download(f"./videos/result_{message.from_user.id}.mp4")
                path = f'./videos/result_{message.from_user.id}.mp4'
                
                with open(f'./videos/result_{message.from_user.id}.mp4', 'wb') as file:
                    bot.send_video(
                    chat_id=message.chat.id,
                    data=file,
                    caption=f'{video_url[:31]}\n\nDownloaded from {bot_name}'
                    )
                os.remove(path)

            except:
                bot.send_message(chat_id=message.chat.id, text=f'❌ Upload error, link salah, video dihapus atau aku tidak bisa menemukannya.')
               
        else:
            bot.send_message(chat_id=message.chat.id, 
                            text='😕 I didn\'t understand you, send me a link to a video from Tik Tok <b>TikTok</b>.', 
                            parse_mode='html')

if __name__ == "__main__":
    bot.polling(non_stop=True)
  
