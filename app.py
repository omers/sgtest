from flask import *
import DocumentDbConfigurationExtractor
from paste.translogger import TransLogger
import cherrypy
from Controllers import api
from Middlewars import CorrelationId

# Bootstrapping code (db,web api,swagger, middleware)
DocumentDbConfigurationExtractor.LoadDbCoonectionDetails()
app = Flask(__name__)
api.init_app(app)
app.before_request(CorrelationId.ExtractCorrelationId)

app.debug = True


def run_server():

    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)

    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')

    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload_on': True,
        'log.screen': True,
        'server.socket_port': 5000,
        'server.socket_host': '0.0.0.0'
    })

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run_server()
    # app.run(debug=True)


