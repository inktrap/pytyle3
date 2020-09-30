# Status

Currently, for me tiling doesn't work. The keypresses are recognized but I can't activate tiling.
Cycling through layouts, quitting pytyle aso. works, at least debugging output says so.
Xcffib supports python3 and xpybutil should too, I guess. Maybe something is wrong with my local config, I am going to investigate this and compare it to a python2 based-pytyle.


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

Use xcffib instead of xcb:

~~~
sed 's/xcb/xcffib/g' -i *.py
sed 's/xcb/xcffib/g' -i **/*.py
~~~

see: <https://pypi.org/project/xcffib/0.3.2/>


Tabs to spaces:

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

