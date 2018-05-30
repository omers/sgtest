from .Alerts import api as alertNamespace
from .Audit import api as auditNamespace
from flask_restplus import Api
from .General import api as generalNamespace


api = Api(
    title='Example for a flask based application (python 3.6.5) based upon cherrypy WSGI server',
    version='1.0.0.0',
    description='Sample code.',
    # All API metadatas
)

#bootstrapping all namespaces.
api.add_namespace(alertNamespace)
api.add_namespace(auditNamespace)
api.add_namespace(generalNamespace)



