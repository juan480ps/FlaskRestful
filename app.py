import logging
from flask import Flask
from flask_restful import Api
from config import postgresqlConfig
from db import db
from resources.contribuyente import Contribuyente, ContribuyenteList
from resources.errors import errors #manejo de exepciones

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig #importar la configuracion de la bd del archi config

db.init_app(app)

api.add_resource(Contribuyente, '/api/contribuyente/')
#api.add_resource(ContribuyenteList, '/api/contribuyente/')

try:
    if __name__ == '__main__':
        logging.basicConfig(filename='app.log', level=logging.DEBUG)
        app.run(debug=False)
except Exception as e:
    print(str(e)) 