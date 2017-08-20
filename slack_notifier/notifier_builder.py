from .config_mgmt.config_reader import ConfigReader
from .subject import Data
from .slack_observer import SlackObserver
from threading import Thread
from .file_watcher import watch
import os

FILE_PATHS_SECTION = 'FILE_PATHS'
KEYWORDS_TO_WATCH_FOR_SECTION = 'KEYWORDS_TO_WATCH_FOR'


class NotifierBuilder:
    def __init__(self):
        self._slack_observer = SlackObserver()
        self._config_reader = ConfigReader()

    def build(self):
        file_paths = self._config_reader.get_section(FILE_PATHS_SECTION)
        keywords = list(map(str.strip,
                            self._config_reader.read_key(KEYWORDS_TO_WATCH_FOR_SECTION, 'KEYWORDS').split(',')))

        for k, v in file_paths.items():
            if os.path.isfile(v):
                thread = Thread(target=self.create_notifier, args=(k, v, keywords, self._slack_observer))
                thread.start()
            else:
                print('Key: {key}, Path: {path} - File does not exists.'.format(key=k, path=v))

    @staticmethod
    def create_notifier(key_name, file_path, keywords, observer):
        data = Data(name=key_name)
        data.attach(observer)
        for hit_word, hit_sentence in watch(file_path, keywords):
            data.data = '```Found %r in %r: %r```' % (hit_word, data.name, hit_sentence)
