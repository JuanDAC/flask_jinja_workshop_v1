""" Blueprint API"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='')

""" views import """
from app.views.sign_in import *
from app.views.task import *