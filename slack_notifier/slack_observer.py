from .observer import Observer
from .slack_bot import SlackListener, TOKEN
from .config_mgmt.config_reader import ConfigReader

SLACK_CHANNEL_NAME_SECTION = 'SLACK_CHANNEL_NAME'


class SlackObserver(Observer):
    def __init__(self):
        self.bot = SlackListener(TOKEN)
        self._config_reader = ConfigReader()

    def update(self, subject):
        channel_name = self._config_reader.read_key(SLACK_CHANNEL_NAME_SECTION, 'NAME')
        self.bot.notify_message(channel_name, subject.data)
