import json
from configparser import ConfigParser
import logging

from telegram import Bot as TelegramBot

logger = logging.getLogger()


class Configuration:
    class __Configuration:

        default_config = {
            'camera_save_path': '/tmp/motion',
            'debug_mode': 'False',
            'allowed_chats': [],
            'ip': '127.0.0.1',
            'port': '8080'
        }

        def __init__(self, config_file):
            self.config_file = config_file
            self.__parse_config_file()
            try:
                self.bot = TelegramBot(token=self.telegram_bot_token)
            except Exception as e:
                raise Exception('Failed to connect to Telegram with error: {0}'.format(repr(e)))

            logger.debug('Initialised: {0}'.format(vars(self)))

        def __str__(self):
            return repr(self) + self.val

        def __parse_config_file(self):
            def _str2bool(v):
                return v.lower() in ("yes", "true", "t", "1")

            cfg = ConfigParser(defaults=self.default_config)
            cfg.read(self.config_file)

            for k, v in cfg.items('main'):
                setattr(self, k, v)

            self.debug_mode = _str2bool(self.debug_mode)
            self.allowed_chats = json.loads(
                cfg.get('main', 'allowed_chats', fallback=self.default_config['allowed_chats']))

    instance = None

    def __init__(self, arg):
        if not Configuration.instance:
            Configuration.instance = Configuration.__Configuration(arg)
        else:
            Configuration.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)
