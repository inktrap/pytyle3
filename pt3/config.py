import os
import os.path
import sys

xdg = os.getenv("XDG_CONFIG_HOME") or os.path.join(os.getenv("HOME"), ".config")
conffile = os.path.join(xdg, "pytyle3", "config.py")

if not os.access(conffile, os.R_OK):
    conffile = os.path.join("/", "etc", "xdg", "pytyle3", "config.py")
    if not os.access(conffile, os.R_OK):
        print(
            "UNRECOVERABLE ERROR: " "No configuration file found at %s" % conffile,
            file=sys.stderr,
        )
        sys.exit(1)

exec(compile(open(conffile, "rb").read(), conffile, "exec"))
