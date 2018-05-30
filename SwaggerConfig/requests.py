from flask_restplus import fields

class requesttypes(object):

    _myreq = None

    def __init__(self):
        self.__dx=2

    @staticmethod
    def getrequestmodel():
        if (requesttypes.__myreq is None):
            raise Exception("you must first load the api obj")
        return  requesttypes.__myreq

    @staticmethod
    def loadmodels(api):
        requesttypes.__myreq = api.model('RequestModel', {
        'name': fields.String(description='Name of the thing', required=True),
        'filter:': fields.String,
        'Take:': fields.Integer
    })

#     def __init__(self, api):
#         self.avireq = api.model('RequestModel', {
#         'name': fields.String(description='Name of the thing', required=True),
#         'filter:': fields.String,
#         'Take:': fields.Integer
#     }
# )
#
#         self.req = api.model('RequestModel', {
#         'name': fields.String(description='Name of the thing', required=True),
#         'filter:': fields.String,
#         'Take:': fields.Integer
#     }
# )
