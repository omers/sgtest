from flask_restplus import fields





class responsetypes(object):
    def __init__(self, api):
        self.res = api.model('ResponseModel', {
            'name': fields.String,
            'age': fields.Integer(min=0)
        })

