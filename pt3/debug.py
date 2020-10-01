import sys

from . import config


def debug(s):
    if not config.debug:
        return
    print(s)
    sys.stdout.flush()


def debug_clients(clients):
    debug("%i clients:" % len(clients))
    clients_formatted = "\n     ".join(list(map(str, clients.keys())))
    debug(" " * 3 + clients_formatted)
