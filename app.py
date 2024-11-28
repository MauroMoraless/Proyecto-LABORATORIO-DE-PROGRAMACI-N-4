import mysql.connector # pip install mysql-connector-python
import re  # Para verificar el formato de fecha
import sys
from datetime import datetime
from prettytable import PrettyTable # python -m pip install -U prettytable

# Conexión a la base de datos
db = mysql.connector.connect(
    user='root', 
    password='root',
    host='localhost',
    port=3306,  # separamos el puerto
    database='tp_lab'
)

# Crear el cursor (es necesario llamarlo como un método)
cursor = db.cursor()  

# Función para agregar un alumno a la base de datos
def agregar_alumno():
    while True:
        nombre = input("Ingrese el nombre del Alumno: ")
        if not nombre:
            print("El nombre es obligatorio.")
        elif not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", nombre):   
            print("El nombre solo puede contener letras.")
        elif len(nombre) < 3:
            print("El nombre debe tener al menos 3 caracteres.")
        elif len(nombre) > 20:
            print("El nombre no debe exceder los 20 caracteres.")
        else:
            break

    while True:
        apellido = input("Ingrese el apellido del Alumno: ")
        if not apellido:
            print("El apellido es obligatorio.")
        elif not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]+$", apellido):   
            print("El apellido solo puede contener letras.")
        else:
            break

    while True:
        dni = input("Ingrese el DNI (sin espacios y sin puntos): ")
        if not dni.isdigit():
            print("El DNI debe contener solo números.")
        elif len(dni) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
        else:
            break

    while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento con los guiones - Ejemplo(2004-12-09):  ")
        if fecha_nacimiento and not re.match(r"\d{4}-\d{2}-\d{2}", fecha_nacimiento):
            print("La fecha de nacimiento no tiene el formato: AAAA-MM-DD.")
        else:
            try:
                # Convertir la fecha de nacimiento ingresada a objeto datetime
                fecha_nacimiento_obj = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
                # Calcular la edad
                edad = (datetime.now() - fecha_nacimiento_obj).days // 365
                if edad < 12 or edad > 21:
                    print("El alumno debe tener entre 12 y 21 años.")
                else:
                    break
            except ValueError:
                print("La fecha de nacimiento no tiene el formato: AAAA-MM-DD.")

    while True:
        telefono = input("Ingrese el celular (sin espacios y sin puntos): ")
        if not telefono.isdigit():
            print("El celular debe contener solo números.")
        elif len(telefono) != 10:
            print("El celular debe tener exactamente 10 dígitos.")
        else:
            break

    while True:
        domicilio = input("Ingrese el domicilio-Ejemplo(Av 9 de Julio 25096):  ")
        if not domicilio:
            print("El domicilio es obligatorio.")
        else:
            break

    query = """INSERT INTO alumno (nombre, apellido, dni, fecha_nacimiento, telefono, domicilio)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    data = (nombre, apellido, dni, fecha_nacimiento or None, telefono, domicilio)
    
    try:
        cursor.execute(query, data)
        db.commit()
        print("¡Alumno agregado exitosamente!")
        menu_alumnos()
        
    except mysql.connector.Error as err:
        print(f"Error al agregar alumno: {err}")
        menu_alumnos()
    
def mostrar_alumnos():
    query = "SELECT * FROM alumno;"
    cursor.execute(query)
    alumnos = cursor.fetchall()
    
    # Crear una tabla con PrettyTable
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Apellido", "DNI", "Fecha Nacimiento", "Teléfono", "Domicilio"]

    # Agregar filas a la tabla
    for alumno in alumnos:
        id_alumno, nombre, apellido, dni, fecha_nac, telefono, domicilio = alumno
        tabla.add_row([id_alumno, nombre, apellido, dni, fecha_nac.strftime("%Y-%m-%d"), telefono, domicilio])
    
    # Mostrar la tabla
    print(tabla)
    menu_alumnos()    

def eliminar_alumno():
    try:
        id_alumno = input("Ingrese el ID del alumno que desea eliminar: ")
        
        # Validar que el ID sea un número
        if not id_alumno.isdigit():
            print("El ID debe ser un número.")
            return(eliminar_alumno())

        # Consulta SQL para verificar si el alumno existe
        query_verificar = "SELECT * FROM alumno WHERE id_alumno = %s"
        cursor.execute(query_verificar, (id_alumno,))
        resultado = cursor.fetchone()

        if not resultado:
            print("No se encontró ningún alumno con el ID ingresado.")
            return(mostrar_menu())

        # Confirmación de eliminación
        confirmacion = input(f"¿Está seguro que desea eliminar al alumno con ID {id_alumno}? (si/no): ").lower()
        if confirmacion != 'si':
            print("Operación cancelada.")
            return(menu_alumnos())

        query_eliminar = "DELETE FROM alumno WHERE id_alumno = %s"
        cursor.execute(query_eliminar, (id_alumno,))
        db.commit()
        print(f"¡Alumno con ID {id_alumno} eliminado exitosamente!")
        menu_alumnos()
    
    except mysql.connector.Error as err:
        print(f"Error al eliminar el alumno: {err}")
        menu_alumnos()

def orden_alfabetico_alumno():
    query = "SELECT * FROM alumno ORDER BY nombre, apellido"
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Apellido", "DNI", "Fecha Nacimiento", "Teléfono", "Domicilio"]
    try:
        cursor.execute(query)
        alumnos = cursor.fetchall()
        for alumno in alumnos:
            id_alumno, nombre, apellido, dni, fecha_nac, telefono, domicilio = alumno
            tabla.add_row([id_alumno, nombre, apellido, dni, fecha_nac.strftime("%Y-%m-%d"), telefono, domicilio])
        print(f"\nAlumnos por orden alfabetico:")
        print(tabla)
        menu_orden_alumnos()
    except mysql.connector.Error as err:
        print(f"Error al ordenar alumnos: {err}")
        menu_alumnos()

def orden_id_alumno():
    query = "SELECT * FROM alumno ORDER BY id_alumno"
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Apellido", "DNI", "Fecha Nacimiento", "Teléfono", "Domicilio"]
    try:
        cursor.execute(query)
        alumnos = cursor.fetchall()
        for alumno in alumnos:
            id_alumno, nombre, apellido, dni, fecha_nac, telefono, domicilio = alumno
            tabla.add_row([id_alumno, nombre, apellido, dni, fecha_nac.strftime("%Y-%m-%d"), telefono, domicilio])
        # Mostrar tabla
        print(f"\nAlumnos ordenados por ID:")
        print(tabla)
        menu_orden_alumnos()
    except mysql.connector.Error as err:
        print(f"Error al ordenar alumnos: {err}")
        menu_alumnos()

def orden_edad_alumno():
    query = "SELECT *, YEAR(CURDATE()) - YEAR(fecha_nacimiento) AS edad FROM alumno ORDER BY edad"
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Apellido", "DNI", "Fecha Nacimiento", "Teléfono", "Domicilio", "Edad"]
    try:
        cursor.execute(query)
        alumnos = cursor.fetchall()
        for alumno in alumnos:
            id_alumno, nombre, apellido, dni, fecha_nac, telefono, domicilio, edad = alumno
            tabla.add_row([id_alumno, nombre, apellido, dni, fecha_nac.strftime("%Y-%m-%d"), telefono, domicilio, edad])
        print(f"\nAlumnos por orden de edad:")
        print(tabla)
        menu_orden_alumnos()
    except mysql.connector.Error as err:
        print(f"Error al ordenar alumnos: {err}")
        menu_alumnos()

def agregar_cursada():
    cursada = input("Ingrese el nombre de la cursada: ")

    if not cursada:
        print("El campo nombre es obligatorio.")
        return(agregar_cursada())

    query = "INSERT INTO cursadas (curso) VALUES (%s)"
    data = (cursada, )

    try:
        cursor.execute(query, data)
        db.commit()
        print("¡Cursada agregada exitosamente!")
        menu_cursada()
    except mysql.connector.Error as err:
        print(f"Error al agregar cursada: {err}")
        menu_cursada()

def mostrar_cursada():
    query = "SELECT * FROM cursadas;"
    tabla = PrettyTable()
    tabla.field_names = ["ID Cursada", "Nombre Cursada"]
    try:
        cursor.execute(query)
        cursadas = cursor.fetchall()
        for cursada in cursadas:
            id_cursada, nombre_cursada = cursada
            tabla.add_row([id_cursada, nombre_cursada])
        print("\nCursadas:")
        print(tabla)
        menu_cursada()
    
    except mysql.connector.Error as err:
        print(f"Error al mostrar cursadas: {err}")
        menu_cursada()  

def eliminar_cursada():
    id_cursada = input("Ingrese el ID de la cursada que desea eliminar: ")

    if not id_cursada.isdigit():
        print("El ID debe ser un número.")
        return(eliminar_cursada())

    query_verificar = "SELECT * FROM cursadas WHERE id_cursada = %s"
    cursor.execute(query_verificar, (id_cursada,))
    resultado = cursor.fetchone()

    if not resultado:
        print("No se encontró ninguna cursada con el ID ingresado.")
        return(eliminar_cursada())

    confirmacion = input(f"¿Está seguro que desea eliminar la cursada con ID {id_cursada}? (si/no): ").lower()
    if confirmacion != 'si':
        print("Operación cancelada.")
        return(menu_cursada())

    query_eliminar = "DELETE FROM cursadas WHERE id_cursada = %s"
    try:
        cursor.execute(query_eliminar, (id_cursada,))
        db.commit()
        print(f"¡Cursada con ID {id_cursada} eliminada exitosamente!")
        menu_cursada()
    except mysql.connector.Error as err:
        print(f"Error al eliminar cursada: {err}")
        eliminar_cursada()

def agregar_inscripcion(): 
    id_alumno = input("Ingrese el ID del alumno: ")
    id_cursada = input("Ingrese el ID de la cursada: ")
    fecha_inscripcion = input("Ingrese la fecha de inscripción (AAAA-MM-DD): ")

    if not re.match(r"\d{4}-\d{2}-\d{2}", fecha_inscripcion):
        print("La fecha no tiene un formato válido (AAAA-MM-DD).")
        return(agregar_inscripcion())
   
    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    if fecha_inscripcion > fecha_actual:
        print("La fecha de inscripción no puede ser posterior al día de hoy. \n Ingresa los datos nuevamente.")
        return agregar_inscripcion()

    query = "INSERT INTO inscripciones (id_alumno, id_cursada, fecha_inscripcion) VALUES (%s, %s, %s)"
    data = (id_alumno, id_cursada, fecha_inscripcion)

    try:
        cursor.execute(query, data)
        db.commit()
        print("¡Inscripción agregada exitosamente!")
        menu_inscripcion()
    except mysql.connector.Error as err:
        print(f"Error al agregar inscripción: {err}")
        menu_inscripcion()

def mostrar_inscripcion():
    query = """
    SELECT inscripciones.id_inscripciones, alumno.nombre, alumno.apellido, cursadas.curso AS cursada, inscripciones.fecha_inscripcion
    FROM inscripciones
    JOIN alumno ON inscripciones.id_alumno = alumno.id_alumno
    JOIN cursadas ON inscripciones.id_cursada = cursadas.id_cursada
    order by id_inscripciones asc;
    """
    tabla = PrettyTable()
    tabla.field_names = ["ID Inscripción", "Nombre Alumno", "Apellido Alumno", "Cursada", "Fecha Inscripción"]

    try:
        cursor.execute(query)
        inscripciones = cursor.fetchall()
        for inscripcion in inscripciones:
            id_inscripcion, nombre, apellido, nombre_cursada, fecha_inscripcion = inscripcion
            tabla.add_row([id_inscripcion, nombre, apellido, nombre_cursada, fecha_inscripcion.strftime("%Y-%m-%d")])
        print("\nInscripciones:")
        print(tabla)
        menu_inscripcion()
    except mysql.connector.Error as err:
        print(f"Error al mostrar inscripciones: {err}")
        menu_inscripcion()

def eliminar_inscripcion():
    id_inscripcion = input("Ingrese el ID de la inscripción que desea eliminar: ")
    if not id_inscripcion.isdigit():
        print("El ID debe ser un número.")
        return(eliminar_inscripcion())

    query_verificar = "SELECT * FROM inscripciones WHERE id_inscripciones = %s"
    cursor.execute(query_verificar, (id_inscripcion,))
    resultado = cursor.fetchone()

    if not resultado:
        print("No se encontró ninguna inscripción con el ID ingresado.")
        return(menu_inscripcion())

    confirmacion = input(f"¿Está seguro que desea eliminar la inscripción con ID {id_inscripcion}? (si/no): ").lower()
    if confirmacion != 'si':
        print("Operación cancelada.")
        return(menu_inscripcion())

    query_eliminar = "DELETE FROM inscripciones WHERE id_inscripciones = %s"
    try:
        cursor.execute(query_eliminar, (id_inscripcion,))
        db.commit()
        print(f"¡Inscripción con ID {id_inscripcion} eliminada exitosamente!")
        menu_inscripcion()
    except mysql.connector.Error as err:
        print(f"Error al eliminar inscripción: {err}")
        menu_inscripcion()

def menu_cursada():
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "MENÚ DE CURSADA:")
        print("=" * 50)
        print("1. Agregar cursada")
        print("2. Mostrar cursadas")
        print("3. Eliminar cursada")
        print("4. Volver a menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cursada()
        elif opcion == "2":
            mostrar_cursada()
            break
        elif opcion == "3":
            eliminar_cursada()
            break
        elif opcion == "4":
            print("Volviendo al menú principal...")
            mostrar_menu()
            break
        
        else:
            print("Opción no válida, intente nuevamente.")
    return

def menu_alumnos():
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "MENÚ DE ALUMNOS:")
        print("=" * 50)
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Eliminar alumnos")
        print("4. Menú para ordenar alumnos")
        print("5. Volver a menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
            break
        elif opcion == "3":
            eliminar_alumno()
            break
        elif opcion == "4":
            menu_orden_alumnos()
            break
        elif opcion == "5":
            print("Volviendo a Menú principal...")
            mostrar_menu()
            break
        
        else:
            print("Opción no válida, intente intente nuevamente.")
    return

def menu_orden_alumnos():
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "VER ALUMNOS POR:")
        print("=" * 50)
        print("1. Orden alfabetico")
        print("2. Orden por ID")
        print("3. Orden por edad")
        print("4. Volver al menú de alumnos")
        print("5. Volver al menú principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            orden_alfabetico_alumno()
        elif opcion == "2":
            orden_id_alumno()
            break
        elif opcion == "3":
            orden_edad_alumno()
            break
        elif opcion == "4":
            menu_alumnos()
            break
        elif opcion == "5":
            print("Volviendo a Menú principal...")
            mostrar_menu()
            break
        
        else:
            print("Opción no válida, intente nuevamente.")
    return

def menu_inscripcion():
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "MENÚ DE INSCRIPCIONES:")
        print("=" * 50)
        print("1. Agregar inscripción")
        print("2. Mostrar inscripción")
        print("3. Eliminar inscripción")
        print("4. Volver al menu principal")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_inscripcion()
        elif opcion == "2":
            mostrar_inscripcion()
            break
        elif opcion == "3":
            eliminar_inscripcion()
            break
        elif opcion == "4":
            print("Volviendo a Menú principal...")
            mostrar_menu()
            break
        
        else:
            print("Opción no válida, intente nuevamente.")
    return

def mostrar_menu():
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Administrar alumnos")
        print("2. Administrar cursadas")
        print("3. Administrar inscripciones")
        print("4. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_alumnos()
        elif opcion == "2":
            menu_cursada()
        elif opcion == "3":
            menu_inscripcion()
        elif opcion == "4":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            print("\n" + "=" * 50)
            sys.exit()
        else:
            print("\n" + "=" * 50)
            print("Opción no válida, intente nuevamente.")
            print("=" * 50)
        return

mostrar_menu()

db.close()