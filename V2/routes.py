from . import api
from .viewfunctions import Markets
from api.common import MarketNews


api.add_resource(Markets, '/markets')
api.add_resource(MarketNews, '/marketnews')