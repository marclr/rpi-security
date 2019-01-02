import glob
import os


def photo(bot, update, webcontrol):
    chat_id = update.message.chat_id
    code, text = webcontrol.execute("action", "snapshot")
    if code == 200:
        path = "/tmp/motion/"
        newest = max(glob.iglob(path + '*-snapshot.jpg'), key=os.path.getctime)
        bot.sendPhoto(chat_id=chat_id, photo=open(newest, 'rb'), timeout=10)
    else:
        bot.sendMessage(chat_id=chat_id, text="Try it later")
