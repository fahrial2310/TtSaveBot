clear
pkg update && pkg upgrade
pkg install python python-pip git python-numpy python-pillow 

pip install --upgrade pip setuptools
pip install -r requirements.txt

git clone https://github.com/fahrial2310/TtSaveBot.git
cd TtSaveBot

echo "-/TtSaveBot $ "
python ttsavebot.py
echo "-/TtSaveBot $ python ttsavebot.py"
