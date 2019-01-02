import logging
import os
import time
from threading import Thread

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from rpisec.Signal import Signal

logging.getLogger("folder_listener").setLevel(logging.ERROR)

logger = logging.getLogger()


class SendCreatedImage(PatternMatchingEventHandler):
    def __init__(self, patterns, changed):
        self.changed = changed
        super().__init__(patterns=patterns)

    def on_created(self, event):
        print(event.src_path)
        self.changed.fire(event.src_path)


class FolderListener(Thread):
    def __init__(self, bot, configuration):
        self.path = configuration.camera_save_path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.changed = Signal()
        self.changed.connect(bot.send_message)
        self.event_handler = SendCreatedImage("[*.jpg]", self.changed)
        super().__init__()
        self.daemon = True

    def run(self):
        observer = Observer()
        observer.schedule(self.event_handler, self.path, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        except Exception as e:
            logger.error('FolderListener has a crash: {0}'.format(repr(e)))
            observer.stop()
        observer.join()
