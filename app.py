from flask import Flask
from flask_restful import Api
from resources.contribuyente import Contribuyente
from resources.autenticacion import Autenticacion
from logging.config import dictConfig
from flask_cors import CORS, cross_origin

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': 'notificacionws02 %(levelname)s %(filename)s(%(lineno)d) %(funcName)s(): %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api/contribuyente/": {"origins": "*"}})
# cors = CORS(app, resources={r"/api/login/": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'


api = Api(app)

api.add_resource(Autenticacion, '/api/login/')
api.add_resource(Contribuyente, '/api/contribuyente/')

@app.route("/")
def hello():
    return "Welcome to Flask Application!"


@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def foo():
    return 'inputVar'

if __name__ == '__main__':
    app.run(debug=False)
    
    

