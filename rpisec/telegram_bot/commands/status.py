def status(bot, update, webcontrol):
    chat_id = update.message.chat_id
    code, text = webcontrol.execute('detection', 'status')
    if code == 200:
        bot.sendMessage(chat_id=chat_id, text=text)
    else:
        bot.sendMessage(chat_id=chat_id, text="Try it later")


