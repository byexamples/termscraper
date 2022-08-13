"""
    helloworld
    ~~~~~~~~~~

    A minimal working example for :mod:`termscraper`.

    :copyright: (c) 2011-2013 by Selectel, see AUTHORS for details.
    :copyright: (c) 2022-... by termscraper authors and contributors,
                    see AUTHORS for details.
    :license: LGPL, see LICENSE for more details.
"""

import termscraper


if __name__ == "__main__":
    screen = termscraper.Screen(80, 24)
    stream = termscraper.Stream(screen)
    stream.feed("Hello World!")

    for idx, line in enumerate(screen.display, 1):
        print("{0:2d} {1} ¶".format(idx, line))
