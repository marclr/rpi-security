import argparse
import logging
import logging.handlers
import signal
import sys

import rpisec
from rpisec.FolderListener import FolderListener
from rpisec.TelegramBot import TelegramBot


def parse_arguments():
    p = argparse.ArgumentParser(description='A simple security system to run on a Raspberry Pi.')
    p.add_argument('-c', '--config_file', help='Path to config file.', default=r'./config/rpi-security.conf')
    p.add_argument('-d', '--debug', help='To enable debug output to stdout', action='store_true', default=False)
    return p.parse_args()


def setup_logging(debug_mode, log_to_stdout):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if log_to_stdout:
        stdout_level = logging.DEBUG
        stdout_format = logging.Formatter(
            "%(asctime)s %(levelname)-7s %(filename)s:%(lineno)-12s %(threadName)-25s %(message)s", "%Y-%m-%d %H:%M:%S")
    else:
        stdout_level = logging.CRITICAL
        stdout_format = logging.Formatter("ERROR: %(message)s")
    if debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(stdout_format)
    stdout_handler.setLevel(stdout_level)
    logger.addHandler(stdout_handler)
    return logger


if __name__ == "__main__":
    args = parse_arguments()
    logger = setup_logging(debug_mode=False, log_to_stdout=args.debug)
    logger.info("rpi-security running")

    configuration = rpisec.Configuration(args.config_file)
    # Start the telegram_bot
    telegram = TelegramBot(configuration)
    folder_listener = FolderListener(telegram, configuration)

    telegram.run()
    folder_listener.run()
