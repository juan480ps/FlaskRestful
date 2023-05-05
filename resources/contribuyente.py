from flask_restful import Resource
from models.contribuyente import ContribuyenteModel
from flask import request
from config import postgresqlConfig
import psycopg2

class Contribuyente(Resource):   

    def post(self):        
        try:
            contribuyente = ContribuyenteModel(
                    operacion = request.json['operacion'], 
                    categoria = request.json['categoria'], 
                    dv=request.json['dv'], 
                    estado=request.json['estado'], 
                    mescierre=request.json['mescierre'], 
                    razonsocial=request.json['razonsocial'], 
                    ruc=request.json['ruc'], 
                )            
            if contribuyente.operacion == "get":
                contribuyente = ContribuyenteModel.find_by_name(contribuyente.razonsocial)
                if contribuyente:
                    return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': contribuyente.json()}, 200
                else:
                    return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': contribuyente.json()}, 404
            elif contribuyente.operacion == "post":
                try:
                    if ContribuyenteModel.find_by_name(contribuyente.razonsocial):
                        contribuyente = ContribuyenteModel.find_by_name(contribuyente.razonsocial)                
                        return {'Codigo':'400', 'Descripcion': "El contribuyente '{}' ya existe.".format(contribuyente.razonsocial), 'Contribuyente': contribuyente.json()}, 400  
                    else:
                        contribuyente.save_to_db()
                        print("insertado")
                        return {'Codigo':'200', "Descripcion": "Contribuyente insertado con exito.", 'Contribuyente': contribuyente.json()}, 200
                except Exception as e:
                    print(str(e))
                    return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': contribuyente.json()}, 500
            
        except Exception as e:
            print(str(e))
            return {'Codigo':'400', 'Descripcion': 'Error al procesar la solicitud', 'Contribuyente': ''}, 400       
    
class ContribuyenteList(Resource):
    def get(self):        
        return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': [contribuyente.json() for contribuyente in ContribuyenteModel.query.all()]}