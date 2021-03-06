
# Requirements

Install [xcffib](https://github.com/tych0/xcffib) and libxcb-render0-dev (Ubuntu, Debian):

```
sudo apt-get install libxcb-render0-dev
pip3 install xcffib
```

Install [xpybutil](https://github.com/inktrap/xpybutil):

~~~
git clone https://github.com/inktrap/xpybutil
cd xpybutil
pip3 install .
~~~


# Install pytyle3

For the time being, just install it from the repository:

~~~
git clone https://github.com/inktrap/pytyle3
cd pytyle3
pip3 install .
mkdir ~/.config/pytyle3
cp config.py keybind.py ~/.config/pytyle3/
~~~

Now you can run it with or without debugging enabled:

```
python3 ./pytyle3
python3 ./pytyle3 --debug
```

If you disabled debugging in ``~/.config/pytyle3`` but still see debugging output, check ``xpybutil/xpybutil/config.py``.


# Uninstall pytyle3 and/or xpybutil

Just run pip to uninstall pytyle3 or xpybutil:

```
pip3 uninstall pytyle3 xpybutil
```

