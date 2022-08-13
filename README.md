
```
     _____                       _____
    |_   _|                     /  ___|
      | |  ___  _ __  _ __ ___  \ `--.   ___  _ __  __ _  _ __    ___  _ __
      | | / _ \| '__|| '_ ` _ \  `--. \ / __|| '__|/ _` || '_ \  / _ \| '__|
      | ||  __/| |   | | | | | |/\__/ /| (__ | |  | (_| || |_) ||  __/| |
      \_/ \___||_|   |_| |_| |_|\____/  \___||_|   \__,_|| .__/  \___||_|
                                                         | |
                                                         |_|
```


## What is `termscraper`?

It's an in memory VTXXX-compatible terminal emulator.
*XXX* stands for a series of video terminals, developed by
[DEC](http://en.wikipedia.org/wiki/Digital_Equipment_Corporation) between
1970 and 1995. The first, and probably the most famous one, was VT100
terminal, which is now a de-facto standard for all virtual terminal
emulators.

`termscraper` follows the suit. It is a direct fork of
[pyte 0.8.1](http://github.com/selectel/pyte) which in turn it
is a fork of [vt102](http://github.com/samfoo/vt102).

`termscraper` aims to be used mostly for scraping terminal
apps like `htop` or very long logs from `tail` or `less`
in a *very efficient* way
so it may not support all the features that a full VT100 terminal
would have.


## Installation

If you have [pip](https://pip.pypa.io/en/stable) you can do the usual:

```shell
$ pip install termscraper
```

Otherwise, download the source from [GitHub termscraper](https://github.com/byexamples/termscraper)
and run:

```shell
$ python setup.py install
```

## Similar projects

`termscraper` is not alone in the weird world of terminal emulator libraries,
here's a few other options worth checking out:

 - [Termemulator](http://sourceforge.net/projects/termemulator/)
 - [pyqonsole](http://hg.logilab.org/pyqonsole/)
 - [webtty](http://code.google.com/p/webtty/)
 - [AjaxTerm](http://antony.lesuisse.org/software/ajaxterm/)
 - [pyte](http://github.com/selectel/pyte)
 - [vt102](http://github.com/samfoo/vt102)
