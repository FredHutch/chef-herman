from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask.ext.hookserver import Hooks
from flask.ext.redis import FlaskRedis

from flask_assets import Environment

from herman.models import User

# Setup flask cache
cache = Cache()

# Setup hookserver

hook = Hooks(url='/hooks')

# Setup Redis Queue

redis_store = FlaskRedis()

# init flask assets
assets_env = Environment()

debug_toolbar = DebugToolbarExtension()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
