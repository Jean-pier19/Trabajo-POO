# main.py
from DAL.crud_empleado import crear_empleado, leer_empleados, actualizar_empleado, eliminar_empleado

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar empleado")
        print("2. Leer empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            
            id_empleado = int(input("Ingrese ID del empleado: "))
            id_tipo_emp = int(input("Ingrese ID del tipo de empleado: "))
            identificacion = input("Ingrese la identificación: ")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            email = input("Ingrese el email: ")
            fecha_contrato = input("Ingrese la fecha de contrato (YYYY-MM-DD): ")
            salario = float(input("Ingrese el salario: "))
            crear_empleado(id_empleado, id_tipo_emp, identificacion, nombre, direccion, telefono, email, fecha_contrato, salario)

        elif opcion == '2':
            
            leer_empleados()

        elif opcion == '3':
            
            id_empleado = int(input("Ingrese el ID del empleado que desea actualizar: "))
            nombre = input("Ingrese el nuevo nombre (o deje en blanco para no cambiar): ")
            direccion = input("Ingrese la nueva dirección (o deje en blanco para no cambiar): ")
            telefono = input("Ingrese el nuevo teléfono (o deje en blanco para no cambiar): ")
            email = input("Ingrese el nuevo email (o deje en blanco para no cambiar): ")
            salario_input = input("Ingrese el nuevo salario (o deje en blanco para no cambiar): ")
            salario = float(salario_input) if salario_input else None
            actualizar_empleado(id_empleado, nombre, direccion, telefono, email, salario)

        elif opcion == '4':
           
            id_empleado = int(input("Ingrese el ID del empleado que desea eliminar: "))
            eliminar_empleado(id_empleado)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
