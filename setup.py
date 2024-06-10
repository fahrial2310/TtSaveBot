import os, sys

os.system("pkg update && pkg upgrade -y")
os.system("pkg install python -y")
os.system("pkg install python-pip -y")
os.system("pkg install python-numpy -y")
os.system("pkg install python-pillow -y")
os.system("pip install --upgrade pip setuptools")
os.system("pip install tiktok_downloader")
os.system("pip install moviepy")
os.system("pip install pyrogram")
os.system("pip install TgCrypto")
os.system("sleep 5")
