import logging

logger = logging.getLogger(__name__)


def unknown(bot, update):
    chat_id = update.message.chat_id
    from_user = update.message.from_user
    text = update.message.text
    logger.info("Unknown command from user: " + str(from_user) + ", chat_id: " + str(chat_id) + " content: " + text)
