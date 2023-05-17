class AutenticacionModel():
    username = ""
    contraseña = ""
    operacion = ""

    def __str__(self):
        return self.id

    def __init__(self, operacion, username, contraseña):
        self.username = username
        self.contraseña = contraseña
        self.operacion = operacion