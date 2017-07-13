from api import session
from flask_restful import Resource, reqparse
from api.model import Market

class Markets(Resource):

    def get(self):
        statuscode = 200
        statusmsg = "OK"
        data=None
        parser = reqparse.RequestParser()
        parser.add_argument('DeviceToken', location='headers')
        try:
            args = parser.parse_args()
            try:
                if (args['DeviceToken'] == None):
                    return {"StatusCode": 401, "StatusMessage": "Unauthorized: DeviceToken is missing or invalid.",
                            "Data": data}
            except:
                return {"StatusCode": 401, "StatusMessage": "Unauthorized: DeviceToken is missing or invalid.",
                        "Data": data}
            # data = [dict(marketid=i.MarketID, name_en=i.MarketNameEn, name_ar=i.MarketNameAr) for i in session.query(Market.MarketID,Market.MarketNameEn,Market.MarketNameAr).all()]
            data = [dict(marketid=i.MarketID,name_en=i.MarketNameEn,name_ar=i.MarketNameAr, country=i.Country.CountryNameEn) for i in session.query(Market).all()]
        except Exception as e:
            statuscode =500
            statusmsg = str(e)
        return {"StatusCode": statuscode,"StatusMessage": statusmsg,"Data": data}
