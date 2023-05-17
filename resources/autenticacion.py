import psycopg2, logging
from flask_restful import Resource
from models.autenticacion import AutenticacionModel
from flask import request
from db.config import postgresqlConfig

class Autenticacion(Resource):    
    
    def post(self):
        conn = psycopg2.connect(postgresqlConfig)
        cur = conn.cursor()
        autenticacion = AutenticacionModel(
            operacion = request.json['operacion'],
            username = request.json['username'],
            pswd = request.json['pswd'],
            )
        logging.debug(request.json)
        if autenticacion.operacion == "getlogin": #se se llama desde el cliente al metodo getall entonces traer todos los contribuyentes
            try:
                logging.debug("Entro getlogin")
                logging.debug(request.headers)
                logging.debug(request.data)
                logging.info('@REQUEST getlogin ' + request.full_path)            
                query = f"SELECT username, contraseña, puedelogin FROM public.usuario where username  = '" + autenticacion.username + "' and contraseña = '" + autenticacion.contraseña + "' and puedelogin"
                logging.debug(query)
                cur.execute(query)
                result = cur.fetchall()
                results = []
                for row in result:
                    results.append({
                        'username': row[0],
                        'contraseña': row[1],
                    })
                if results:
                    respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': results}, 200
                else:
                    respuesta = {'codigo':'404', 'Descripcion': 'Usuario no autenticado', 'Usuario': results}, 404
            except Exception as e:
                respuesta = {'codigo':'400', 'Descripcion': str(e), 'Usuario': results}, 500 
                
        return respuesta