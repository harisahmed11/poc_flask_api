from . import api
from api.common import  MarketNews
from .viewfunctions import Markets



api.add_resource(Markets, '/markets')
api.add_resource(MarketNews, '/marketnews')