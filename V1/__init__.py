from flask_restful import Api
from flask import Blueprint


api_v1_blueprint = Blueprint('v1_api', __name__, template_folder='templates')

api = Api(api_v1_blueprint)

from .routes import *