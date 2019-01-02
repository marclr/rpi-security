import glob
import os


def video(bot, update):
    # the most recent video in this particular folder of complete vids
    video1 = max(glob.iglob('/tmp/motion/*.mkv'), key=os.path.getctime)
    # send video, adapt the the first argument to your own telegram id
    bot.sendVideo(update.message.chat_id, video=open(video1, 'rb'), caption='last video')
