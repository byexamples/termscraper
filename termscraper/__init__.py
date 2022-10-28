"""
    termscraper
    ~~~~

    `termscraper` implements a mix of VT100, VT220 and VT520 specification,
    and aims to support most of the `TERM=linux` functionality.

    Two classes: :class:`~termscraper.streams.Stream`, which parses the
    command stream and dispatches events for commands, and
    :class:`~termscraper.screens.Screen` which, when used with a stream
    maintains a buffer of strings representing the screen of a
    terminal.

    .. warning:: From ``xterm/main.c`` "If you think you know what all
                 of this code is doing, you are probably very mistaken.
                 There be serious and nasty dragons here" -- nothing
                 has changed.

    :copyright: (c) 2011-2012 by Selectel.
    :copyright: (c) 2012-2017 by pyte authors and contributors,
                    see AUTHORS for details.
    :copyright: (c) 2022-... by termscraper authors and contributors,
                    see AUTHORS for details.
    :license: LGPL, see LICENSE for more details.
"""

__all__ = (
    "Screen", "HistoryScreen", "DebugScreen", "LinearScreen", "Stream",
    "WSPassthroughStream"
)

import io

from .screens import Screen, HistoryScreen, DebugScreen, LinearScreen
from .streams import Stream, WSPassthroughStream

from .version import __version__


def dis(chars):
    """A :func:`dis.dis` for terminals.

    >>> from termscraper import dis
    >>> dis(b"\x07")       # byexample: +norm-ws
    ["bell", [], {}]

    >>> dis(b"\x1b[20m")   # byexample: +norm-ws
    ["select_graphic_rendition", [20], {}]
    """
    if isinstance(chars, str):
        chars = chars.encode("utf-8")

    with io.StringIO() as buf:
        Stream(DebugScreen(to=buf)).feed_binary(chars)
        print(buf.getvalue())
