import logging
from flask import Flask
from flask_restful import Api
from config import postgresqlConfig
from db import db
from resources.contribuyente import Contribuyente, ContribuyenteList
from resources.errors import errors #manejo de exepciones

app = Flask(__name__)
api = Api(app)
#api = Api(app, errors = errors)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig #importar la configuracion de la bd del archi config

# Setup the Flask-JWT-Extended extension
#app.config["JWT_SECRET_KEY"] = "asdf4asd964as5c4s85d4sa6c51sd9c84sa65c1sa9d8c46as5c1a6sdc4a6sx5c21sd56c4sa5c"  # Change this!

db.init_app(app)

api.add_resource(Contribuyente, '/api/contribuyente/')
#api.add_resource(ContribuyenteList, '/api/contribuyente/')

try:
    if __name__ == '__main__':
        logging.debug('This message should go to the log file')
        app.run(debug=False)
except Exception as e:
    print(str(e)) 