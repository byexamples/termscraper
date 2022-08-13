"""
    termscraper
    ~~~~

    Command-line tool for "disassembling" escape and CSI sequences::

        $ echo -e "\\e[Jfoo" | python -m termscraper
        ERASE_IN_DISPLAY 0
        DRAW f
        DRAW o
        DRAW o
        LINEFEED

        $ python -m termscraper foo
        DRAW f
        DRAW o
        DRAW o

    :copyright: (c) 2011-2012 by Selectel.
    :copyright: (c) 2012-2017 by pyte authors and contributors,
                    see AUTHORS for details.
    :copyright: (c) 2022-... by termscraper authors and contributors,
                    see AUTHORS for details.
    :license: LGPL, see LICENSE for more details.
"""

if __name__ == "__main__":
    import sys
    import termscraper

    if len(sys.argv) == 1:
        termscraper.dis(sys.stdin.read())
    else:
        termscraper.dis("".join(sys.argv[1:]))