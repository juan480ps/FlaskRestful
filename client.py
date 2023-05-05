# import requests
# import json

# url = "http://127.0.0.1:5000/api/contribuyente/"
# data = {
#     "operacion":"getall",
#     "id": None,
#     "ruc": "864521655",
#     "categoria": "teas",
#     "dv": "teas",
#     "estado": "teas",
#     "mescierre": "teas",
#     "razonsocial": "teas"
# }
# headers = {"Content-Type": "application/json"}

# response = requests.post(url, data=json.dumps(data), headers=headers)

# print(response.json())



import requests, json
from prettytable import PrettyTable

base_url = "http://127.0.0.1:5000/api/contribuyente"

loop = True

print("""

    Bienvenid@. Por favor seleccione una opción a continuación:
    """)

while(loop == True):

    print("""

    1 - Listar todos los contribuyentes.
    2 - Listar contribuyente por ID.
    3 - Listar contribuyente por RUC.
    4 - Agregar un nuevo contribuyente.
    5 - Actualizar un contribuyente.
    6 - Borrar un contribuyente.
    0 - Salir del sistema.

    """)

    accion = input()

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    if accion == '1':
        url = base_url 
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
            json_data = json.dumps(data)
            data = json.loads(json_data)
            table = PrettyTable()
            table.field_names = data['Contribuyentes'][0].keys()
            for contribuyente in data['Contribuyentes']:
                table.add_row(contribuyente.values())
            print(table)
        else:
            print(f"Ocurrió un error al enviar la solicitud: {response.text}")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    elif accion == '2':
        print("""

        Elegiste la opción 2. 

        Por favor a continuacón, ingrese el ID del contribuyente que sea consultar:

        """)
        opcion = input()
        if opcion is not None or opcion != "":
            url = base_url + "/" + opcion
            response = requests.request("POST", url)
            if response.status_code == 200:
                data = response.json()
                print("""
Id | Razón social
__________________

            """)
                print(str(data["id"]) + " | " + data["razonsocial"])
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    elif accion == '3':
        print("""

        Elegiste la opción 3. 

        Por favor a continuacón, ingrese el RUC del contribuyente que sea consultar:

        """)
        opcion = input()
        if opcion is not None or opcion != "":
            url = base_url + "/byruc/" + opcion
            response = requests.request("GET", url)
            if response.status_code == 200:
                data = response.json()
                print("""
RUC | Razón social
__________________

            """)
                if data:
                    for dato in data:
                        print(dato["ruc"] + " | " + dato["razonsocial"])                    
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    elif accion == '4':
        print("""

        Elegiste la opción 3. 

        Por favor a continuacón, ingrese los siguientes datos del contribuyente a agregar:

        categoria, dv, estado, mescierre, razonsocial, ruc

        **Favor respete el orden de los compos citados.

        """)
        print("""

        Ingrese la categoría:

        """)
        categoria = input()

        print("""

        Ingrese el dígito verificador:

        """)
        dv = input()

        print("""

        Ingrese el estado:

        """)
        estado = input()    

        print("""

        Ingrese el mes de cierre:

        """)
        mescierre = input()

        print("""

        Ingrese la razón social:

        """)
        razonsocial = input()

        print("""

        Ingrese el RUC:

        """)
        ruc = input()

        if (categoria != "" or dv != "" or estado != "" or mescierre != "" or 
            razonsocial != "" or ruc != "" ):

            url = base_url
            headers = {"Content-Type": "application/json"}
            data = {
            "categoria": categoria,
            "dv": dv,
            "estado": estado,
            "mescierre": mescierre,
            "razonsocial": razonsocial,
            "ruc": ruc
            }

            response = requests.request("POST", url, headers = headers, data = json.dumps(data))
            if response.status_code == 201:
                print(f"La operación se realizó correctamente: ")
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    elif accion == '5':
        print("""

        Elegiste la opción 4. 

        Por favor a continuacón, ingrese el ID del contribuyente que sea modificar: 
        
        """)
        id = input()
        if id != "":

            url = base_url + "/" + id
            response = requests.request("GET", url)
            if response.status_code == 200:
                data = response.json()
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")

            print("""Por favor a continuacón, ingrese los siguientes datos del contribuyente a modificar:

            categoria, dv, estado, mescierre, razonsocial, ruc

            **Favor respete el orden de los compos citados.

            """)

            print("""

            Ingrese la categoría:

            """)
            categoria = input()

            print("""

            Ingrese el dígito verificador:

            """)
            dv = input()

            print("""

            Ingrese el estado:

            """)
            estado = input()    

            print("""

            Ingrese el mes de cierre:

            """)
            mescierre = input()

            print("""

            Ingrese la razón social:

            """)
            razonsocial = input()

            print("""

            Ingrese el RUC:

            """)
            ruc = input()

        if (categoria != "" or dv != "" or estado != "" or mescierre != "" or 
            razonsocial != "" or ruc != "" ):

            url = base_url + "/" + id 
            headers = {"Content-Type": "application/json"}
            data = {
            "categoria": categoria,
            "dv": dv,
            "estado": estado,
            "mescierre": mescierre,
            "razonsocial": razonsocial,
            "ruc": ruc,
            "id": id
            }

            response = requests.request("PUT", url, headers = headers, data = json.dumps(data))
            if response.status_code == 200:
                print(f"La operación se realizó correctamente: ")
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    elif accion == '6':
        print("""

        Elegiste la opción 5. 

        Por favor a continuacón, ingrese el ID del contribuyente que sea eliminar: 
        
        """)
        id = input()
        print("""

        ¿Estás segur@ de eliminar el contribuyente ingresado?

        S = Si / N = No
        
        """)
        respuesta = input()
        if respuesta.lower() == "s":
            url = base_url + "/" + id 
            response = requests.request("DELETE", url)
            if response.status_code == 200:
                print(f"La operación se realizó correctamente: ")
            else:
                print(f"Ocurrió un error al enviar la solicitud: {response.text}")
        else:
            print(f"Operación cancelada")

#########################################################################################################
#-------------------------------------------------------------------------------------------------------#
#########################################################################################################

    else:
        loop = False 