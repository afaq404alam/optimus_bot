from slackclient import *

# The secret token provided by slack for your bot.
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'


class SlackListener:
    def __init__(self, token, debug=False):
        self.client = SlackClient(token=token)
        self._connect()
        self._my_user_name = self.client.server.login_data['self']['id']
        self._debug = debug

    def _connect(self):
        self.client.rtm_connect()

    def notify_message(self, channel_name, msg):
        if not self.client.server.connected:
            self._connect()
        channel = self.client.server.channels.find(channel_name)
        channel.send_message(msg)
