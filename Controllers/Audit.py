from flask import Blueprint
from flask import  *
import HttpContext
import  DataLayer.DocumentDb.Queries as queries
import jsonpickle
from SwaggerConfig import requests, responses
from flask_restplus import Namespace, Resource, fields
import jsonpickle

api = Namespace('Audit', description='Audit related operations')



auditmodel = api.model('Audit', {
    'audit_entry_id': fields.String(required=True, description='The Audit entry identifier'),
    'audit_entry_name': fields.String(required=True, description='The Audit entry name'),
})

Audit = [
    {'id': 'This_is_Audit_Entry_Id', 'name': 'sdfgdf43t544563434'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_Audit_Entries')
    @api.marshal_list_with(auditmodel)
    def get(self):
        '''List all alerts'''
        return Audit

@api.route('/<id>')
@api.param('id', 'The audit entry identifier')
@api.response(404, 'audit entry not found')
class Cat(Resource):
    @api.doc('get_Audit_By_Id')
    @api.marshal_with(auditmodel)
    def get(self, id):
        '''Fetch an audit entry given its identifier'''
        for cat in Audit:
            if cat['id'] == id:
                return cat
        api.abort(404)

@api.route('/health')
@api.response(200, 'server is healthy')
class HealthCheck(Resource):
    @api.doc('check audit server health')
    def post(self):
        '''Checks audit server health state'''
        return "im 0kay :). i mean it"
        '''Fetch an alert given its identifier'''







