clear
pkg update && pkg upgrade
pkg install python python-pip git python-numpy python-pillow 

pip install --upgrade pip setuptools

# requirements
pip install telebot
pip install pyrogram
pip install TgCrypto

pip install tiktok_downloader
pip install moviepy

git clone https://github.com/fahrial2310/TtSaveBot.git
cd TtSaveBot

echo "-/TtSaveBot $ "
python ttsavebot.py
echo "-/TtSaveBot $ python ttsavebot.py"
