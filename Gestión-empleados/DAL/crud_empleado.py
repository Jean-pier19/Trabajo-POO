from DAL.generar_conexion import crear_conexion
from clases.empleado import Empleado

def crear_empleado(id_empleado, id_tipo_emp, identificacion, nombre, direccion, telefono, email, fecha_contrato, salario):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            sql_crear_empleado = """INSERT INTO empleado (id_empleado, id_tipo_emp, identificacion, nombre, direccion, telefono, email, fecha_contrato, salario)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
            cursor.execute(sql_crear_empleado, (id_empleado, id_tipo_emp, identificacion, nombre, direccion, telefono, email, fecha_contrato, salario))
            conexion.commit()
            print("Empleado agregado exitosamente.")
        except Exception as e:
            print(f"Error al crear el empleado: {e}")
        finally:
            cursor.close()
            conexion.close()

def leer_empleados():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            sql_leer_empleados = "SELECT * FROM empleado"
            cursor.execute(sql_leer_empleados)
            empleados = cursor.fetchall()
            for empleado in empleados:
                print(empleado)
        except Exception as e:
            print(f"Error al leer los empleados: {e}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_empleado(id_empleado, nombre=None, direccion=None, telefono=None, email=None, salario=None):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            campos = []
            valores = []
            if nombre:
                campos.append("nombre = %s")
                valores.append(nombre)
            if direccion:
                campos.append("direccion = %s")
                valores.append(direccion)
            if telefono:
                campos.append("telefono = %s")
                valores.append(telefono)
            if email:
                campos.append("email = %s")
                valores.append(email)
            if salario:
               campos.append("salario = %s")
               valores.append(salario)
            
            valores.append(id_empleado)
            sql_actualizar_empleado = f"UPDATE empleado SET {', '.join(campos)} WHERE  id_empleado = %s"     
            cursor.execute(sql_actualizar_empleado, valores)
            conexion.commit()
            print("Empleado actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_empleado(id_empleado):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            sql_eliminar_empleado = "DELETE FROM empleado WHERE id_empleado = %s"
            cursor.execute(sql_eliminar_empleado, (id_empleado,))
            conexion.commit()
            print("Empleado eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")
        finally:
            cursor.close()
            conexion.close()    