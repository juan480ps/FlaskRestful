from flask_restful import Resource, abort, reqparse
from models.contribuyente import ContribuyenteModel
from resources.errors import InternalServerError, ContribuyenteNotExistsError
from psycopg2 import DatabaseError
from flask import request as req
#token
#from flask_jwt_extended import jwt_required
    

class Contribuyente(Resource):

    # def get(self, name):
    #     item = ContribuyenteModel.find_by_name(name)
    #     if item:
    #         return item.json()
    #     return {'message': 'Item not found'}, 404
    
    parser = reqparse.RequestParser()
    parser.add_argument('ruc', type = str, required = True,
                            help = 'El RUC no puede quedar en blanco', location='json')
    parser.add_argument('razonsocial', type = str, required = True,
                        help = 'La razón social no puede quedar en blanco', location='json')

    #@jwt_required()  # Requires dat token
    def get(self, name):
        try:
            contribuyente = ContribuyenteModel.find_by_name(name)
            if contribuyente:
                return contribuyente.json()
            else:
                return {'message': 'Contribuyente no encontrado'}, 404
        except DatabaseError:
            raise ContribuyenteNotExistsError
        except Exception:
            raise InternalServerError

    #@jwt_required()
    def post(self, name):
        if ContribuyenteModel.find_by_name(name):
            return {'message': "El contribuyente '{}' ya existe.".format(
                name)}, 400  
        try:
            item = ContribuyenteModel(
            categoria = req.json['categoria'], 
            dv=req.json['dv'], 
            estado=req.json['estado'], 
            mescierre=req.json['mescierre'], 
            razonsocial=req.json['razonsocial'], 
            ruc=req.json['ruc'], 
        )
            item.save_to_db()
        except Exception as e:
            return {"message": "Ha ocurrido un error al insertar." + str(e)}, 500
        
    
class ContribuyenteList(Resource):
    def get(self):        
        return {'Contribuyentes': [contribuyente.json() for contribuyente in ContribuyenteModel.query.all()]}