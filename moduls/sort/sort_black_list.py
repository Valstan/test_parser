import re

from config import delete_msg_blacklist


def sort_black_list(msg):
    msg['text'].lower()
    for sample in delete_msg_blacklist:
        if re.search(sample, msg['text']):
            return True


if __name__ == '__main__':
    pass
