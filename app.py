from flask import Flask
from flask_restful import Api
from db.config import postgresqlConfig
from db.db import db
from resources.contribuyente import Contribuyente
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        #'format': '[%(asctime)s] %(levelname)s in %(name)s %(module)s: %(message)s',
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
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig #importar la configuracion de la bd del archivo config.py

db.init_app(app)

#se instancia la url de la api
api.add_resource(Contribuyente, '/api/contribuyente/')

if __name__ == '__main__':
    app.run(debug=False)