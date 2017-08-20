import time
import re


def watch(fn, words):
    print('I am watching you -->', fn)
    fp = open(fn, 'r')
    fp.seek(0, 2)
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            for word in words:
                if _find_whole_word(word.lower())(new.lower()):
                    yield (word, new)
                    break
        else:
            time.sleep(0.5)


def _find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
