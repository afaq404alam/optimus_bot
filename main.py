#!/usr/bin/env python3.5
from slack_notifier.notifier_builder import NotifierBuilder

if __name__ == '__main__':
    notifier_builder = NotifierBuilder()
    notifier_builder.build()
    print('Slack notifier is running...')
