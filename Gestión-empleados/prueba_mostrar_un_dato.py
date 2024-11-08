from DAL.generar_conexion import crear_conexion
from clases import Asignacion, Departamento, Empleado, Proyecto, Proyectoempleado, Registrotime, Tipoempleado

def main():
    
    conexion = crear_conexion()
    if conexion:
        print("Conexión a la base de datos exitosa.")
        
        
        empleado = Empleado(1, 1, 'ID001', 'Juan Perez', 'Calle Falsa 123, Santiago', '987654321', 'juan.perez@example.com', '2023-01-15', 1000.00)
        print(empleado.nombre)  

        conexion.close()

if __name__ == "__main__":
    main()
