from .proyecto import Proyecto
from .empleado import Empleado

class Proyectoempleado:
    def __init__(self, id_proyec_emp, id_proyec, id_empleado):
        super().__init__(id_proyec)
        super().__init__(id_empleado)
        self.id_proyec_emp = id_proyec_emp
        