#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Michael Gutteridge'
__email__ = 'mrg@fredhutch.org'
__version__ = '0.1'

from flask import Flask
from flask.ext.hookserver import Hooks
from webassets.loaders import PythonLoader as PythonAssetsLoader

from herman.controllers.main import main
from herman.controllers.hookhandler import hookhandler
from herman import assets
from herman.models import db

from herman.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager,
    hook,
    redis_store
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. herman.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config.from_object('herman.secrets.Config')

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # initialize webhooks
    hook.init_app(app)

    # Intialize redis
    redis_store.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)
    app.register_blueprint(hookhandler)

    return app
