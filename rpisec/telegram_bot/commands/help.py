def help(bot, update):
    text = " The following commands are available:\n"

    commands = [
        ["/status", "Show state of alarm"],
        ["/enable", "Activate alarm"],
        ["/disable", "Disable alarm"],
        ["/photo", "Make a photo"],
        ["/help", "Show this help"]
    ]

    for command in commands:
        text += command[0] + " " + command[1] + "\n"

    bot.send_message(chat_id=update.message.chat_id, text=text)
