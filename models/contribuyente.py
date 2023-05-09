class ContribuyenteModel():
    id = 0
    categoria = ""
    dv = ""
    estado = ""
    mescierre = ""
    razonsocial = ""
    ruc = ""
    operacion = ""

    def __str__(self):
        return self.id

    def __init__(self, operacion, id, ruc, categoria, dv, estado, mescierre, razonsocial):
        self.categoria = categoria
        self.dv = dv
        self.estado = estado
        self.mescierre = mescierre
        self.razonsocial = razonsocial
        self.ruc = ruc
        self.id = id
        self.operacion = operacion