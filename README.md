python-crocodoc
===============
http://github.com/mikexstudios/python-crocodoc
by Michael Huynh (mike@mikexstudios.com)

Purpose:
-------

A very simple wrapper for Crocodoc's API based off of crocodoc.rb by
jeremy ruten (https://github.com/yjerem/crocodoc).


How to use
----------

1.  Install python-crocodoc using pip:

        pip install -e git://github.com/mikexstudios/python-crocodoc.git#egg=python-crocodoc
        
    or with easy_install:

        easy_install http://github.com/mikexstudios/python-crocodoc/tarball/master

    Note that python-crocodoc depends on bolacha, a REST/http client for
    python. If you used pip or easy_install, the dependency should automatically
    be installed. The bolacha dependency is my own forked version (since there
    is a bug in the original bolacha for GET/HEAD requests):

        https://github.com/mikexstudios/bolacha

2.  Then simply import crocodoc at the top of your python script:

        import crocodoc

    and then instantiate Crocodoc, passing in your API key like:

        c = crocodoc.Crocodoc('[API KEY GOES HERE]')

    Now call the different methods of the Crocodoc class (see the source
    of `crocodoc/__init__.py` for what methods are available and how to 
    call them). For example, to upload a url:

        r = c.upload('http://www.dcaa.mil/chap6.pdf')

    The response `r` is a dictionary, for example:

        {"shortId": "yQZpPm", "uuid": "8e5b0721-26c4-11df-b354-002170de47d3"}


Testing
-------

To test the script, set `CROCODOC_API_KEY` in your environment variables to 
our API key. For example with bash:

    export CROCODOC_API_KEY=[API KEY GOES HERE]

Then run:

    python test.py

NOTE: Tests may fail because crocodoc limits free users to two simultaneous
      conversions at once.


TODO
----

1.  Implement `download` method.
2.  See TODOs attached to `share` and `get_session`.
3.  Delete uploaded documents after each test (in `test.py`).
