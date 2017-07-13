from flask_restful import Api
from flask import Blueprint


api_v2_blueprint = Blueprint('v2_api', __name__, template_folder='templates')

api = Api(api_v2_blueprint)

from .routes import *