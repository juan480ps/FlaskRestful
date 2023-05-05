# import psycopg2
# from flask_restful import Resource, reqparse

# class User(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, required=True)
#         args = parser.parse_args()
        
#         # Conectarse a la base de datos
#         conn = psycopg2.connect(
#             host='localhost',
#             port=5432,
#             dbname='nombre_de_la_base_de_datos',
#             user='nombre_de_usuario',
#             password='contraseña'
#         )
#         cur = conn.cursor()
        
#         # Ejecutar la consulta SELECT
#         query = f"SELECT * FROM usuarios WHERE username = '{args['username']}'"
#         cur.execute(query)
#         result = cur.fetchone()
        
#         # Cerrar la conexión a la base de datos
#         cur.close()
#         conn.close()
        
#         if result is None:
#             return {'message': 'Usuario no encontrado'}, 404
        
#         # Devolver el resultado en formato JSON
#         return {'user_id': result[0], 'username': result[1], 'email': result[2]}, 200


# from flask import jsonify
# from models import ContribuyenteModel

# class Contribuyente(Resource):
#     def get(self, ruc):
#         contribuyente = ContribuyenteModel.query.filter_by(ruc=ruc).all()
#         if not contribuyente:
#             return {'message': 'Contribuyente no encontrado'}, 404
#         return jsonify([c.json() for c in contribuyente])


# from flask_restful import Resource

# class MyResource(Resource):
#     def post(self):
#         result = MyTable.query.all()
#         json_result = [r.__dict__ for r in result]
#         return json_result
    

# tupla = ('valor1', 'valor2')
# claves = ['clave1', 'clave2']
# diccionario = dict(zip(claves, tupla))
# print(diccionario) # imprimirá {'clave1': 'valor1', 'clave2': 'valor2'}


# from flask_restful import Resource
# from flask import request
# import psycopg2

# class MyResource(Resource):
#     def post(self):
#         # Obtener los parámetros de la solicitud POST
#         data = request.get_json()
#         user_id = data.get('user_id')
        
#         # Conectarse a la base de datos y ejecutar la consulta
#         conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="localhost", port="5432")
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM mytable WHERE user_id = %s", (user_id,))
        
#         # Obtener todos los resultados de la consulta y procesarlos en una lista de diccionarios
#         results = []
#         rows = cur.fetchall()

#         results = []
#         for row in rows:
#             results.append({
#                 'id': row[0],
#                 'name': row[1],
#                 'age': row[2]
#             })
        
#         # Cerrar la conexión y devolver la respuesta JSON
#         cur.close()
#         conn.close()
#         return {'results': results}
