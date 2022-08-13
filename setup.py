# https://packaging.python.org/en/latest/distributing.html
# https://github.com/pypa/sampleproject

from setuptools import setup, find_packages
from codecs import open
from os import path, system

import sys, re

here = path.abspath(path.dirname(__file__))

# load __version__, _doc, _author, _license and _url
exec(open(path.join(here, 'termscraper', 'version.py')).read())

try:
    system('''pandoc -f markdown-raw_html -o '%(dest_rst)s' '%(src_md)s' ''' % {
                'dest_rst': path.join(here, 'README.rst'),
                'src_md':   path.join(here, 'README.md'),
                })

    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    # strip out any HTML comment|tag
    long_description = re.sub(r'<!--.*?-->', '', long_description,
                                                flags=re.DOTALL|re.MULTILINE)
    long_description = re.sub(r'<img.*?src=.*?>', '', long_description,
                                                flags=re.DOTALL|re.MULTILINE)

    with open(path.join(here, 'README.rst'), 'w', encoding='utf-8') as f:
        f.write(long_description)

except:
    print("Generation of the documentation failed. " + \
          "Do you have 'pandoc' installed?")

    long_description = _doc

# the following are the required dependencies
install_deps = [
        'wcwidth==0.2.5',
    ]

setup(
    name='termscraper',
    version=__version__,

    description=_doc,
    long_description=long_description,

    url=_url,

    # Author details
    author=_author,
    author_email='use-github-issues@example.com',

    license=_license,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
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
    ],

    python_requires='>=3.6',
    install_requires=install_deps,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    platforms=["any"],

    keywords=["scraper", "pyte", "vt102", "vte", "terminal emulator"],

    packages=['termscraper'],
    data_files=[("", ["LICENSE"])]
)

