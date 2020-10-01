import sys
from pprint import pprint

from . import config


def debug(s):
    if not config.debug:
        return
    print(s)
    sys.stdout.flush()


def debug_object(o):
    if not config.debug:
        return
    pprint(o)
    sys.stdout.flush()
