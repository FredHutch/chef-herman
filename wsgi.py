#!/usr/bin/env python

import sys
import os

from herman import create_app


APPROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'herman'))
if not APPROOT in sys.path:
    sys.path.insert(0, APPROOT)

env = os.environ.get('HERMAN_ENV', 'dev')
application = create_app('herman.settings.%sConfig' % env.capitalize())

