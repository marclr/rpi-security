from telegram.ext import BaseFilter


class FilterChatId(BaseFilter):
    def __init__(self, allowed):
        self.allowed = allowed

    def filter(self, message):
        chat_id = message.chat_id
        return chat_id in self.allowed
