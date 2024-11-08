from .tipo_empleado import Tipoempleado

class Empleado(Tipoempleado):
    def __init__(self, id_empleado, id_tipo_emp,identificacion, nombre, direccion, telefono, email, fecha_contrato, salario):
        super().__init__(id_tipo_emp,identificacion)  
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_contrato = fecha_contrato
        self.salario = salario


