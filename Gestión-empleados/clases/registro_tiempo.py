from .proyecto_empleado import Proyectoempleado
class Registrotime():
    def __init__(self, id, id_proyec_emp, fecha, horas, descipcion):
        super().__init__(id_proyec_emp)
        self.id = id
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion