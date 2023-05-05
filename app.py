from flask import Flask
from flask_restful import Api
from config import postgresqlConfig
from db import db
from resources.contribuyente import Contribuyente

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig #importar la configuracion de la bd del archivo config.py

db.init_app(app)

#se instancia la url de la api
api.add_resource(Contribuyente, '/api/contribuyente/')

if __name__ == '__main__':
    app.run(debug=False)