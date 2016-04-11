#!/usr/bin/env python

import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from herman import create_app
from herman.models import db, User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('HERMAN_ENV', 'dev')
app = create_app('herman.settings.%sConfig' % env.capitalize())

if __name__ == "__main__":
    app.run()

