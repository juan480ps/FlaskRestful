from flask_restful import Resource
from models.contribuyente import ContribuyenteModel
from flask import request
from config import postgresqlConfig
import psycopg2
from util.logz import create_logger

class Contribuyente(Resource):       
    
    def post(self):#se siempre al metodo post y se pregunta el tipo de operacion para cada caso     
        try:
            conn = psycopg2.connect(postgresqlConfig)
            cur = conn.cursor()
            contribuyente = ContribuyenteModel(
                operacion = request.json['operacion'],
                id = request.json['id'],
                categoria=request.json['categoria'], 
                dv=request.json['dv'], 
                estado=request.json['estado'], 
                mescierre=request.json['mescierre'], 
                razonsocial=request.json['razonsocial'], 
                ruc=request.json['ruc'],                 
            )
            
            if contribuyente.operacion == "getall" and contribuyente.id == None: #se se llama desde el cliente al metodo getall entonces traer todos los contribuyentes
                query = f"SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente;"
                cur.execute(query)
                result = cur.fetchall()
                results = []
                for row in result:
                    results.append({
                        'categoria': row[0],
                        'dv': row[1],
                        'estado': row[2],
                        'mescierre': row[3],
                        'razonsocial': row[4],
                        'ruc': row[5],
                    })
                if results:
                    self.logger = create_logger(contribuyente.operacion)
                    return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                else:
                    return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
            
            elif contribuyente.operacion == "getbyid" and contribuyente.id != None: #se se llama desde el cliente al metodo getbyid entonces devuelve el id del contribuyente buscado
                query = "SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where id = {};".format(contribuyente.id)
                cur.execute(query)
                result = cur.fetchall()
                results = []
                for row in result:
                    results.append({
                        'categoria': row[0],
                        'dv': row[1],
                        'estado': row[2],
                        'mescierre': row[3],
                        'razonsocial': row[4],
                        'ruc': row[5],
                    })
                if results:
                    return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                else:
                    return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
            
            elif contribuyente.operacion == "getbyruc" and contribuyente.ruc != "":#se se llama desde el cliente al metodo getbyruc entonces devuelve el contribuyenteque coincide con el ruc filtrado
                query = "SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where ruc ilike '%{}%';".format(contribuyente.ruc)
                cur.execute(query)
                result = cur.fetchall()
                results = []
                for row in result:
                    results.append({
                        'categoria': row[0],
                        'dv': row[1],
                        'estado': row[2],
                        'mescierre': row[3],
                        'razonsocial': row[4],
                        'ruc': row[5],
                    })
                if results:
                    return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                else:
                    return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
            
            elif contribuyente.operacion == "postinsert":#se se llama desde el cliente al metodo postinsert para insertar o agregar un nuevo contribuyente
                try:
                    query = "SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where ruc = '{}';".format(contribuyente.ruc)
                    cur.execute(query)
                    result = cur.fetchone()
                    if result:
                        return {'Codigo':'400', 'Descripcion': "El contribuyente '{}' ya existe.".format(result[4]), 'Contribuyente': result}, 400  
                    else:
                        query = """insert into contribuyente (categoria, dv, estado, mescierre, razonsocial, ruc)
                        select '{}', '{}', '{}', '{}', '{}', '{}';
                        """.format(contribuyente.categoria, contribuyente.dv, contribuyente.estado, contribuyente.mescierre, contribuyente.razonsocial, contribuyente.ruc )
                        cur.execute(query)
                        conn.commit()
                        contribuyente = {
                            "categoria": contribuyente.categoria,
                            "dv": contribuyente.dv,
                            "estado": contribuyente.estado,
                            "mescierre": contribuyente.mescierre,
                            "razonsocial": contribuyente.razonsocial,
                            "ruc": contribuyente.ruc
                        }
                        return {'Codigo':'200', "Descripcion": "Contribuyente insertado con exito.", 'Contribuyente': contribuyente}, 200                        
                except Exception as e:
                    conn.rollback()
                    return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': contribuyente}, 500
            
            elif contribuyente.operacion == "postupdate":#se se llama desde el cliente al metodo postupdate para modificar el contribuyente eleccionado
                if contribuyente.id == None:
                    return {'Codigo':'400', 'Descripcion': 'El id no puede quedar vacío', 'Contribuyente': ''}, 400       
                query = """
                update contribuyente set categoria = '{}', 
                                        dv = '{}', 
                                        estado = '{}', 
                                        mescierre = '{}', 
                                        razonsocial = '{}', 
                                        ruc = '{}'
                where id = {}
                """.format(contribuyente.categoria, contribuyente.dv, contribuyente.estado, 
                contribuyente.mescierre, contribuyente.razonsocial, contribuyente.ruc, contribuyente.id 
                )
                cur.execute(query)
                conn.commit()
                contribuyente = {
                    "categoria": contribuyente.categoria,
                    "dv": contribuyente.dv,
                    "estado": contribuyente.estado,
                    "mescierre": contribuyente.mescierre,
                    "razonsocial": contribuyente.razonsocial,
                    "ruc": contribuyente.ruc
                }
                return {'Codigo':'200', "Descripcion": "Contribuyente actualizado con exito.", 'Contribuyente': contribuyente}, 200                        
            
            
        except Exception as e:
            print(str(e))
            return {'Codigo':'400', 'Descripcion': 'Error al procesar la solicitud', 'Contribuyente': ''}, 400       
        finally:
            cur.close()
            conn.close()

class ContribuyenteList(Resource):
    def __init__(self):
        self.logger = create_logger()
        
    def get(self):        
        return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': [contribuyente.json() for contribuyente in ContribuyenteModel.query.all()]}