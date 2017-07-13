from api import session
from flask_restful import Resource, reqparse


class MarketNews(Resource):

    def get(self):
        statuscode = 200
        statusmsg = "OK"
        data = None

        parser = reqparse.RequestParser()
        parser.add_argument('pageno')
        parser.add_argument('pagesize')
        parser.add_argument('DeviceToken', location='headers')

        try:
           args = parser.parse_args()
           try:
               if (args['DeviceToken']==None):
                  return  {"StatusCode":401,"StatusMessage":"Unauthorized: DeviceToken is missing or invalid.","Data":data}
           except:
                  return {"StatusCode": 401, "StatusMessage": "Unauthorized: DeviceToken is missing or invalid.","Data":data}

           data = [dict(rank=i.Rank, articale_id=i.ArticleId, Title=i.Title) for i in session.execute('Mobile_Article_GetArticlesForMultipleMarketSection :pageNo, :pageSize',{'pageNo': args['pageno'], 'pageSize': args['pagesize'] }).fetchall()]

        except Exception as e:
            statuscode = 500
            statusmsg = str(e)

        return {"StatusCode": statuscode, "StatusMessage": statusmsg, "Data": data}