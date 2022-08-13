"""
    history
    ~~~~~~~

    A tiny example to show how pagination works.

    :copyright: (c) 2011-2013 by Selectel, see AUTHORS for details.
    :copyright: (c) 2022-... by termscraper authors and contributors,
                    see AUTHORS for details.
    :license: LGPL, see LICENSE for more details.
"""

import os
import random
import string
import sys

import termscraper
from termscraper import modes as mo


def print_screen(screen, text):
    print(termscraper.control.ESC + termscraper.escape.RIS)

    for idx, line in enumerate(screen.display, 1):
        print("{0:2d} {1} ¶".format(idx, line))

    input(os.linesep + os.linesep + text)


def random_string(n, alphabet=string.ascii_letters + " "):
    return "".join(random.choice(alphabet) for _ in range(n))


if __name__ == "__main__":
    # ``ratio=1`` means scroll the whole screen.
    screen = termscraper.HistoryScreen(80, 12, ratio=1)
    screen.set_mode(mo.LNM)
    stream = termscraper.Stream(screen)

    pages = 3
    stream.feed(os.linesep.join(random_string(screen.columns)
                                for _ in range(screen.lines * pages)))
    screen.prev_page()

    print_screen(screen, "Hit ENTER to move up!")
    screen.prev_page()
    print_screen(screen, "Hit ENTER to move back down!")
    screen.next_page()
    print_screen(screen, "OK?")
