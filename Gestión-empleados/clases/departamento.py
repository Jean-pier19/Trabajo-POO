from .empleado import Empleado

class Departamento(Empleado):
    def __init__(self,id_depto,nombre,id_empleado=None):
        super().__init__(id_empleado)
        self.id_depto = id_depto
        self.nombre = nombre
        