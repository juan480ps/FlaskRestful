import psycopg2, logging
from flask_restful import Resource
from models.contribuyente import ContribuyenteModel
from flask import request
from db.config import postgresqlConfig
from util.logz import create_logger

class Contribuyente(Resource):    
    def post(self):#se siempre al metodo post y se pregunta el tipo de operacion para cada caso     
        try:
            
            logging.debug("Entro GET")
            logging.debug(request.headers)
            logging.debug(request.data)
            logging.info('@REQUEST GET '+request.full_path)
            
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
                try:                    
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
                        create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results})
                        return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                    else:
                        create_logger(contribuyente.operacion, {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results})
                        return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results})
                    return {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500            
            
            elif contribuyente.operacion == "getbyid" and contribuyente.id != None: #se se llama desde el cliente al metodo getbyid entonces devuelve el id del contribuyente buscado
                try:  
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
                        create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results})
                        return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                    else:
                        create_logger(contribuyente.operacion, {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results})
                        return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results})
                    return {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500 

            elif contribuyente.operacion == "getbyruc" and contribuyente.ruc != "":#se se llama desde el cliente al metodo getbyruc entonces devuelve el contribuyenteque coincide con el ruc filtrado
                try:
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
                        create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results})
                        return {'Codigo':'200', 'Descripcion': 'Contribuyente encontrado', 'Contribuyente': results}, 200
                    else:
                        create_logger(contribuyente.operacion, {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results})
                        return {'Codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results})
                    return {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500 
                
            elif contribuyente.operacion == "postinsert":#se se llama desde el cliente al metodo postinsert para insertar o agregar un nuevo contribuyente
                try:
                    query = "SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where ruc = '{}';".format(contribuyente.ruc)
                    cur.execute(query)
                    result = cur.fetchone()
                    if result:
                        create_logger(contribuyente.operacion, {'Codigo':'409', 'Descripcion': "El contribuyente con RUC '{}' ya existe.".format(contribuyente.ruc), 'Contribuyente': "'{}'".format(result)})
                        return {'Codigo':'409', 'Descripcion': "El contribuyente con RUC '{}' ya existe.".format(contribuyente.ruc), 'Contribuyente': "'{}'".format(result)}, 400  
                    else:
                        query = """insert into contribuyente (categoria, dv, estado, mescierre, razonsocial, ruc)
                        select '{}', '{}', '{}', '{}', '{}', '{}';
                        """.format(contribuyente.categoria, contribuyente.dv, contribuyente.estado, contribuyente.mescierre, contribuyente.razonsocial, contribuyente.ruc )
                        cur.execute(query)
                        conn.commit()
                        item = {
                            "categoria": contribuyente.categoria,
                            "dv": contribuyente.dv,
                            "estado": contribuyente.estado,
                            "mescierre": contribuyente.mescierre,
                            "razonsocial": contribuyente.razonsocial,
                            "ruc": contribuyente.ruc
                        }
                        create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': "Contribuyente insertado con éxito.", 'Contribuyente': item})
                        return {'Codigo':'200', "Descripcion": "Contribuyente insertado con éxito.", 'Contribuyente': item}, 200                        
                except Exception as e:
                    conn.rollback()
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': results})
                    return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': contribuyente}, 500
            
            elif contribuyente.operacion == "postupdate":#se se llama desde el cliente al metodo postupdate para modificar el contribuyente eleccionado
                try:
                    if contribuyente.id == None:
                        create_logger(contribuyente.operacion, {'Codigo':'409', 'Descripcion': "El id no puede quedar vacío", 'Contribuyente': ""})
                        return {'Codigo':'409', 'Descripcion': 'El id no puede quedar vacío', 'Contribuyente': ''}, 400       
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
                    item = {
                        "categoria": contribuyente.categoria,
                        "dv": contribuyente.dv,
                        "estado": contribuyente.estado,
                        "mescierre": contribuyente.mescierre,
                        "razonsocial": contribuyente.razonsocial,
                        "ruc": contribuyente.ruc
                    }
                    create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': "Contribuyente actualizado con éxito.", 'Contribuyente': item})
                    return {'Codigo':'200', "Descripcion": "Contribuyente actualizado con éxito.", 'Contribuyente': item}, 200
                except Exception as e:
                    conn.rollback()
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': item})
                    return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': item}, 500
                
                
            elif contribuyente.operacion == "postdelete":#se se llama desde el cliente al metodo postdelete para eliminar el contribuyente eleccionado
                try:
                    if contribuyente.id == None:
                        create_logger(contribuyente.operacion, {'Codigo':'409', 'Descripcion': "El id no puede quedar vacío", 'Contribuyente': ""})
                        return {'Codigo':'409', 'Descripcion': 'El id no puede quedar vacío', 'Contribuyente': ''}, 400       
                    query = """delete from contribuyente where id = {};""".format(contribuyente.id)
                    cur.execute(query)
                    conn.commit()
                    item = {
                        "categoria": contribuyente.categoria,
                        "dv": contribuyente.dv,
                        "estado": contribuyente.estado,
                        "mescierre": contribuyente.mescierre,
                        "razonsocial": contribuyente.razonsocial,
                        "ruc": contribuyente.ruc
                    }
                    create_logger(contribuyente.operacion, {'Codigo':'200', 'Descripcion': "Contribuyente eliminado con éxito.", 'Contribuyente': item})
                    return {'Codigo':'200', "Descripcion": "Contribuyente eliminado con éxito.", 'Contribuyente': item}, 200
                except Exception as e:
                    conn.rollback()
                    create_logger(contribuyente.operacion, {'Codigo':'400', 'Descripcion': str(e), 'Contribuyente': item})
                    return {'Codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': item}, 500
            
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