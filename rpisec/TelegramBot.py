# -*- coding: utf-8 -*-
import logging
from threading import Thread

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from rpisec.telegram_bot.commands import unknown, status, enable, disable, help, photo, video
from rpisec.telegram_bot.filters.filter_chat_id import FilterChatId
from rpisec.telegram_bot.utils.Webcontrol import Webcontrol

logging.getLogger("telegram").setLevel(logging.ERROR)

logger = logging.getLogger()


class TelegramBot(Thread):
    def __init__(self, configuration):
        self.bot = configuration.bot
        self.allowed_chats = configuration.allowed_chats
        self.updater = Updater(configuration.telegram_bot_token)

        self.webcontrol = Webcontrol(configuration)

        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher
        super().__init__()
        self.daemon = True

    def run(self):
        try:
            # Instance the custom filters
            filter_chat_id = FilterChatId(self.allowed_chats)

            # on different commands - answer in Telegram
            self.dp.add_handler(
                CommandHandler(("estat", "status"),
                               (lambda bot, update: status(bot, update, self.webcontrol)),
                               filter_chat_id))
            self.dp.add_handler(
                CommandHandler(("activar", "enable"),
                               (lambda bot, update: enable(bot, update, self.webcontrol)),
                               filter_chat_id))
            self.dp.add_handler(
                CommandHandler(("desactivar", "disable"),
                               (lambda bot, update: disable(bot, update, self.webcontrol)),
                               filter_chat_id))
            self.dp.add_handler(
                CommandHandler(("foto", "photo"),
                               (lambda bot, update: photo(bot, update, self.webcontrol)),
                               filter_chat_id))
            self.dp.add_handler(CommandHandler("video", video, filter_chat_id))
            self.dp.add_handler(CommandHandler("help", help, filter_chat_id))

            self.dp.add_handler(MessageHandler(Filters.command, unknown))
            self.dp.add_handler(MessageHandler(Filters.all, unknown))

            self.updater.start_polling(timeout=1)

        except Exception as e:
            logger.error('Telegram Updater failed to start with error {0}'.format(repr(e)))

    def send_message(self, image):
        for chat_id in self.allowed_chats:
            try:
                self.bot.sendPhoto(chat_id=chat_id, photo=open(image, 'rb'), timeout=10)
            except Exception as e:
                print(e)
