import psycopg2, logging
from flask_restful import Resource
from models.contribuyente import ContribuyenteModel
from flask import request
from db.config import postgresqlConfig

class Contribuyente(Resource):    
    
    def post(self):#se siempre al metodo post y se pregunta el tipo de operacion para cada caso    
        respuesta = "" 
        item = {}
        try:
            conn = psycopg2.connect(postgresqlConfig)
            cur = conn.cursor()
            contribuyente = ContribuyenteModel(
                operacion = request.json['operacion'],
                id = request.json['id'],
                categoria = request.json['categoria'], 
                dv = request.json['dv'], 
                estado = request.json['estado'], 
                mescierre = request.json['mescierre'], 
                razonsocial = request.json['razonsocial'], 
                ruc = request.json['ruc'],                 
            )
            logging.debug(request.json)
            if contribuyente.operacion == "getall" and (contribuyente.id == None or contribuyente.id == ''): #se se llama desde el cliente al metodo getall entonces traer todos los contribuyentes
                try:
                    logging.debug("Entro getall")
                    logging.debug(request.headers)
                    logging.debug(request.data)
                    logging.info('@REQUEST getall ' + request.full_path)            
                    query = f"SELECT id, categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente;"
                    logging.debug(query)
                    cur.execute(query)
                    result = cur.fetchall()
                    results = []
                    for row in result:
                        results.append({
                            'id': row[0],
                            'categoria': row[1],
                            'dv': row[2],
                            'estado': row[3],
                            'mescierre': row[4],
                            'razonsocial': row[5],
                            'ruc': row[6],
                        })
                    if results:
                        respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': results}
                    else:
                        respuesta = {'codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    respuesta = {'codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500            
            
            elif contribuyente.operacion == "getbyid" and contribuyente.id != None: #se se llama desde el cliente al metodo getbyid entonces devuelve el id del contribuyente buscado
                try:  
                    query = "SELECT id, categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where id = {};".format(contribuyente.id)
                    cur.execute(query)
                    result = cur.fetchall()
                    results = []
                    for row in result:
                        results.append({
                            'id': row[0],
                            'categoria': row[1],
                            'dv': row[2],
                            'estado': row[3],
                            'mescierre': row[4],
                            'razonsocial': row[5],
                            'ruc': row[6],
                        })
                    if results:
                        respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': results}
                    else:
                        respuesta = {'codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    respuesta = {'codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500 

            elif contribuyente.operacion == "getbyruc" and contribuyente.ruc != "":#se se llama desde el cliente al metodo getbyruc entonces devuelve el contribuyenteque coincide con el ruc filtrado
                try:
                    query = "SELECT id, categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where ruc ilike '%{}%';".format(contribuyente.ruc)
                    cur.execute(query)
                    result = cur.fetchall()
                    results = []
                    for row in result:
                        results.append({
                            'id': row[0],
                            'categoria': row[1],
                            'dv': row[2],
                            'estado': row[3],
                            'mescierre': row[4],
                            'razonsocial': row[5],
                            'ruc': row[6],
                        })
                    if results:
                        respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': results}
                    else:
                        respuesta = {'codigo':'404', 'Descripcion': 'Contribuyente no encontrado', 'Contribuyente': results}, 404
                except Exception as e:
                    respuesta = {'codigo':'400', 'Descripcion': str(e), 'Contribuyente': results}, 500 
                
            elif contribuyente.operacion == "postinsert":#se se llama desde el cliente al metodo postinsert para insertar o agregar un nuevo contribuyente
                try:
                    query = "SELECT categoria, dv, estado, mescierre, razonsocial, ruc FROM contribuyente where ruc = '{}';".format(contribuyente.ruc)
                    cur.execute(query)
                    result = cur.fetchone()
                    if result:
                        respuesta = {'codigo':'409', 'Descripcion': "El contribuyente con RUC '{}' ya existe.".format(contribuyente.ruc), 'Contribuyente': "'{}'".format(result)}, 400  
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
                        respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': item}
                except Exception as e:
                    conn.rollback()
                    respuesta = {'codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': contribuyente}, 500
            
            elif contribuyente.operacion == "postupdate":#se se llama desde el cliente al metodo postupdate para modificar el contribuyente eleccionado
                try:
                    if contribuyente.id == None:
                        respuesta = {'codigo':'409', 'Descripcion': 'El id no puede quedar vacío', 'Contribuyente': ''}, 400       
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
                    respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': item}
                except Exception as e:
                    conn.rollback()
                    respuesta = {'codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': item}, 500
                
                
            elif contribuyente.operacion == "postdelete":#se se llama desde el cliente al metodo postdelete para eliminar el contribuyente eleccionado
                try:
                    if contribuyente.id == None or contribuyente.id == '':
                        respuesta = {'codigo':'409', 'Descripcion': 'El id no puede quedar vacío', 'Contribuyente': ''}, 400       
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
                    respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': item}
                except Exception as e:
                    conn.rollback()
                    respuesta = {'codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': item}, 500
            
        except Exception as e:
            print(str(e))
            respuesta = {'codigo':'400', 'Descripcion': 'Error al procesar la solicitud', 'Contribuyente': ''}, 400       
        finally:
            cur.close()
            conn.close()
            
        return respuesta

class ContribuyenteList(Resource):
    def __init__(self):
        respuesta = {'codigo':0, 'descripcion': 'OK',  "objetoJson": "", 'listJson': ''}
        
    def get(self):        
        return {'codigo':'400', 'Descripcion': "Ha ocurrido un error al insertar.", 'Contribuyente': [contribuyente.json() for contribuyente in ContribuyenteModel.query.all()]}