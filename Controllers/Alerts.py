from flask_restplus import Namespace, Resource, fields
from flask import *
import  DataLayer.DocumentDb.Queries as queries

api = Namespace('Alerts', description='Alerts related operations')



alert_advanced_data = api.model('advanced_alerts_data', {
    'refkeynumber': fields.String(required=True),
    'name': fields.String(required=True),
})


create_alert_response_model = api.model('create_alert_response_model', {
    'alert_id': fields.String(required=True, description='The alert identifier'),
    'InternalData': fields.List(fields.Nested(alert_advanced_data)),
    'alert_name': fields.String(required=True, description='The alert name')

})



get_all_alerts_response_model = api.model('get_all_alerts_response', {
    'id': fields.String(required=True, description='The alert name'),
    'alert_name': fields.String(required=True, description='The alert name'),
    'alert_category': fields.String(required=True, description='The alert name')
})


class xx(object):
    def __init__(self):
        self.refkeynumber="sdfsdf"
        self.name ="dsafsdf"


class alertres(object):
    def __init__(self,alertid,alertname,internaldata):
        self.alert_id = alertid
        self.alert_name = alertname
        self.InternalData = internaldata
        self.test_avi = "sdfsdf"
        self.data="dataaa!"


create_alert_request_model = api.model('create_alert_request_model', {
         'Alert_Name': fields.String(description='Name of the Alert', required=True),
         'Alert_Id': fields.String(description='Id of the alert', required=True),
         'InternalData': fields.List(fields.Nested(alert_advanced_data), required=True),
         'Data': fields.String(description='Id of the alert', required=False),
    })


Alerts = [
    {'id': 'this_is_alert_id', 'name': 'xsg33ghd3w2667e233'},
]



# @api.route('/aaa')
# class Cat(Resource):
#     @api.doc('list_alerts')
#     #@api.marshal_list_with(create_alert_response_model)
#     def get(self):
#         '''List all alerts'''
#         mydocument = queries.get_alert()
#         return mydocument

@api.route('/<id>')
@api.param('id', 'The alert identifier')
@api.response(404, 'alert not found')
class Cat(Resource):
    @api.doc('Get_Alert_By_Id')
    @api.marshal_with(create_alert_response_model)
    def get(self, id):
        '''Fetch an alert given its identifier'''
        for cat in Alerts:
            if cat['id'] == id:
                return cat
        api.abort(404)


@api.route('/')
@api.response(201, 'alert created')
class Cat(Resource):
    @api.doc('create_new_alert')
    @api.marshal_with(create_alert_response_model)
    @api.expect(create_alert_request_model)
    def post(self):
        '''Creates new alert'''
        x = xx()
        xxxx =list()
        xxxx.append(x)
        adf= alertres("id","name",xxxx)
        json =  request.get_json(force=True)
        return adf
        #return jsonpickle.encode(adf)
        '''Fetch an alert given its identifier'''


    @api.doc('list_alerts')
    @api.marshal_with(get_all_alerts_response_model)
    #@api.marshal_list_with(create_alert_response_model)
    def get(self):
        '''List all alerts'''
        mydocument = queries.get_alert()
        return mydocument



@api.route('/health')
@api.response(200, 'server is healthy')
class HealthCheck(Resource):
    @api.doc('check alert server health')
    def post(self):
        '''Checks alert server health state'''
        return "im 0kay :). i mean it"
        '''Fetch an alert given its identifier'''




