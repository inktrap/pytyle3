# Status/Changes

 - corrected some minor issues, spacing, …
 - pytyle3 doesn't need xcb anymore, I added a small line to use xpybutil's compat :)
 - one issue was in xpybutil's function that is called if a ``window`` is resized or moved, it expects integers but got some floats. Currently I am converting them.
 - another issue **is**/was in xpybutil's ``keybind.py``:

```
    if e.request == xproto.Mapping.Keyboard:
        changes = {}
        for kc in range(*get_min_max_keycode()):
            ...
```

This takes a long time to run and is CPU intensive. For the time being, I placed a return before the loop. However this is not ideal; the keycodes do indeed change.

I'll have a look [at other tilers and how they do it](https://github.com/qtile/qtile/blob/f6710b159b7b98925fbba8edfb169896433bedd3/libqtile/backend/x11/xcbq.py#L819) or maybe I'll ask BurntSushi.

 - when is ``update_keyboard_mapping`` called and why does it take so long?
 - I know that python2.7 and python3 ``range``s are not the same, but they are not very different either, so that's not it, right?
 - Do globals work diffently in python3? I know that for doesn't leak into the global namespace anymore …



# Preparations

Install xcffib:

~~~
sudo apt-get install libxcb-render0-dev
pip3 install xcffib
~~~


# Changes to support python3

Xpybutil should work with python3 (at least there are commits referencing python3);
nevertheless I ran 2to3:

```
git clone https://github.com/BurntSushi/xpybutil
2to3-2.7 -w -n **/*.py *.py
rm *.pyc **/*.pyc
```

## Use xcffib instead of xcb

Actually, don't do this!

~~~
sed 's/xcb/xcffib/g' -i *.py
sed 's/xcb/xcffib/g' -i **/*.py
~~~

xpybutil's ``compat.py`` imports xcffib and you can replace the remaining xcb imports in ``pt3/client.py`` by importing from there. Also, there are some exceptions: <https://github.com/tych0/xcffib>



## Tabs to spaces

```
find . -name '*.py' ! -type d -exec bash -c 'expand -t 4 "$0" > /tmp/e && mv /tmp/e "$0"' {} \;
```


# Install


Change to the pytyle3/xpybutil folder and run:

```
pip3 install .
```

I repeated the "Changes to support python3" and "Install" steps for pytyle3.


# Configure Pytyle3 and run it

Create/Edit these configs:

~~~
~/.config/pytyle3/keybind.py
~/.config/pytyle3/config.py
~~~

Run it:

```
python3 ./pytyle3
python3 ./pytyle3 --debug
```

