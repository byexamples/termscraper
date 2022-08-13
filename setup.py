#! /usr/bin/env python

import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = "Simple VTXXX-compatible terminal emulator scraper."

try:
    with open(os.path.join(here, "README")) as f:
        LONG_DESCRIPTION = f.read()
except IOError:
    LONG_DESCRIPTION = ""


CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Terminals :: Terminal Emulators/X Terminals",
]


setup(name="termscraper",
      version="0.8.1",
      packages=["termscraper"],
      install_requires=["wcwidth"],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      platforms=["any"],

      author="Martin Di Paola",
      author_email='use-github-issues@example.com',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      classifiers=CLASSIFIERS,
      keywords=["vt102", "vte", "terminal emulator"],
      url="https://github.com/byexamples/termscraper")
