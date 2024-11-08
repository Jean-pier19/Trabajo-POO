from .empleado import Empleado
from .departamento import Departamento

class Asignacion():
    def __init__(self,id,id_empleado,id_depto):
        super().__init__(id_empleado)
        super().__init__(id_depto)
        self.id = id
        