from db import db

class ContribuyenteModel():   
    __tablename__ = 'contribuyente'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(256), nullable=False)
    dv = db.Column(db.String(256), nullable=False)
    estado = db.Column(db.String(256), nullable=False)
    mescierre = db.Column(db.String(256), nullable=False)
    razonsocial = db.Column(db.String(256), nullable=False)
    ruc = db.Column(db.String(256), nullable=False)    
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

    # def json(self):
    #     return {
    #         'categoria' : self.categoria, 
    #         'dv' : self.dv, 
    #         'estado' : self.estado, 
    #         'mescierre' : self.mescierre, 
    #         'razonsocial' : self.razonsocial, 
    #         'ruc' : self.ruc
    #     }
    
    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(razonsocial=name).first()
    
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    

