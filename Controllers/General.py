from flask import  *
import HttpContext
import  DataLayer.DocumentDb.Queries as queries
from SwaggerConfig import requests, responses
from flask_restplus import Namespace, Resource, fields
import jsonpickle

api = Namespace('General', description='General related operations')

responses = responses.responsetypes(api)
sad = requests.requesttypes._myreq
a = requests.requesttypes()
requests.requesttypes.loadmodels(api)
a =requests.requesttypes()

@api.route('/my-resource/<id>')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    # @app.before_request
    def get(self, id):
        return id

    @api.doc(responses={403: 'Not Authorized'})
    # @app.before_request
    def post(self, id):
        api.abort(403)

@api.route('/api/Test',methods=['GET'])
class GetConfig(Resource):
    @api.doc(responses={401: 'Not Authorized'})
    @api.doc(responses={200: 'Okay'})
    def get(self,**kwargs):
        mydocument = queries.GetConfigDocument()
        return jsonpickle.encode(list(mydocument))

@api.route('/api/config',methods=['GET'])
class GetConfig2(Resource):
    @api.doc(responses={401: 'Not Authorized'})
    @api.doc(responses={200: 'Okay'})
    def get(self):
        mydocument = queries.GetConfigDocument()
        return jsonpickle.encode(list(mydocument))



@api.route('/api/Myconfig',methods=['POST'])
class GetConfig(Resource):
    @api.doc(responses={401: 'Not Authorized'})
    @api.response(200, 'Success', responses.res)
    @api.doc(responses={200: 'Okay'})
    @api.expect(requests.requesttypes.getrequestmodel())
    def post(self):
        if (request.data):
              a = request.get_json(force=True)


        HttpContext.ActiveRequest.GetCurrentContext().etag="etag"
        #request.etag = "xcxfxcvcc"

        mydocument = queries.GetConfigDocument()
        mydocument2 = queries.GetConfigDocument()
        return jsonpickle.encode(list(mydocument))


@api.route('/health')
@api.response(200, 'server is healthy')
class HealthCheck(Resource):
    @api.doc('check general server health')
    def post(self):
        '''Checks general server health state'''
        return "im 0kay :). i mean it"
        '''Fetch an alert given its identifier'''


