#--------------------------------------------------------------------------------------------------------------
#Librerias
from datetime import datetime #IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
import random 
import os #Biblioteca para usar la terminar
import json #Biblioteca para usar Json
import hashlib #Biblioteca para usar un numero unico generado.
#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------
"""
Habitaciones Informacion General

Tipo de habitacion:

Cada tipo de habitacion tiene 3 unidades cada una 
habitaciones normales de 2 persons == 1
habitaciones normales de 4 persons == 2
habitaciones premium de 2 persons == 3
habitaciones premium de 4 persons == 4

Estado de Habitaciones:
0 libre 1 ocupado
"""
#---------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
"""
FUNCIONES DE HABITACIONES

Se Trae el conjunto de habitaciones del documento json habitaciones .json, el mismo se utilizara para mostrar el nombre de habitaciones
Y su posterior re escritura a la hora de reservar una habitacion

"""""

def cargar_habitaciones():
    with open('habitaciones.json', 'r') as file:
        habitaciones = json.load(file)
    return habitaciones

#Sobre escribir el diccionario post reserva 
def guardar_habitaciones(habitaciones):
    with open('habitaciones.json', 'w') as file:
        json.dump(habitaciones, file, indent=4)

#Funcion Mostar habitaciones, Muestra todo el Array textual se presente en ese momento la utilizamos para la opcion mostrar habitaciones del menu

def verificar_disponibilidad(fecha_ingreso, fecha_salida, n_reserva):
    
    for reserva in reservas:
        if reserva['NumeroHabitacion'] == n_reserva:
            fecha_ingreso_existente = datetime.strptime(reserva['Fecha_ingreso'], "%Y-%m-%d").date()
            fecha_salida_existente = datetime.strptime(reserva['Fecha_salida'], "%Y-%m-%d").date()

            # Verificar solapamiento o contigüidad de fechas
            if fecha_ingreso <= fecha_salida_existente and fecha_salida >= fecha_ingreso_existente:
                print("No se puede reservar. Las fechas de la nueva reserva se solapan o tocan una reserva existente.")
                return False
    
    print("La habitación está disponible para las fechas solicitadas ✔.")
    return True
""""
Funcion Mostrar habitaciones, la utilizamos para mostrar el numero de cuartos a la hora de hacer una reserva, los cuartos mostrados dependeran
de si ya se encuentran reservadas, estado 1 (Solo mostramos estados 0s) y Segun la cantidad de acompa;antes declarados dentro de ella
se encuentra la funcion cambiar_estado
"""

def asignar_habitacion(habitaciones, num_acompanantes,fecha_ingreso,fecha_salida):
    # Si hay menos de 2 acompañantes, mostrar todas las habitaciones
    print("==================================")
    print("|          Habitaciones          |")
    print("| Numero  -   Nombre   -    Tipo |")
    print("----------------------------------")

    if num_acompanantes < 2:
        for habitacion in habitaciones:
            if habitacion['cantidadPersonas'] == 2:
                print(f"-",habitacion['numeroHabitacion']," ✦",habitacion['nombreHabitacion']," ～",habitacion['tipoHabitacion'],f"-")
    # Si hay 2 o más acompañantes, mostrar solo habitaciones con capacidad para 4 personas
    else:
        for habitacion in habitaciones:
            if habitacion['cantidadPersonas'] == 4:
                print(f"-",habitacion['numeroHabitacion']," ✦",habitacion['nombreHabitacion']," ～",habitacion['tipoHabitacion'],f"-")

    fecha_ingreso_formateada = fecha_ingreso.strftime("%d-%m-%Y")
    fecha_salida_formateada = fecha_salida.strftime("%d-%m-%Y")
    
    print("==================================")
    print("| Fecha de estadia de la reserva |")
    print("| Dia   -     Mes     -    Anio  |")
    print("----------------------------------")
    print("|",fecha_ingreso_formateada,"   Al   ",fecha_salida_formateada,"|")
    print("==================================")

    habitacion_valida = False  # Variable de control

    while not habitacion_valida:
        asignar_n_habitacion = input("Ingrese el número de la habitación: ")  # Convertir a string

        # Si hay menos de 2 acompañantes, buscamos habitaciones de capacidad 2
        if num_acompanantes < 2:
            for habitacion in habitaciones:
                if habitacion['cantidadPersonas'] == 2 and asignar_n_habitacion == habitacion['numeroHabitacion']:
                    if verificar_disponibilidad(fecha_ingreso,fecha_salida,asignar_n_habitacion):
                        print("Se ingresó la habitación ✔.")
                        habitacion_valida = True
        
        # Si hay 2 o más acompañantes, buscamos habitaciones de capacidad 4
        else:
            for habitacion in habitaciones:
                if habitacion['cantidadPersonas'] == 4 and asignar_n_habitacion == habitacion['numeroHabitacion']:
                    if verificar_disponibilidad(fecha_ingreso,fecha_salida,asignar_n_habitacion):
                        print("Se ingresó la habitación ✔.")
                        habitacion_valida = True
        
        # Revisar si no se encontró una habitación válida
        if not habitacion_valida :
            print("- Ingrese un numero de habitacion valido -")
    
    return asignar_n_habitacion

"""
La funcion cambiar estado hace que cuando se seleccione un cuarto de los mostrados por nombre habitacion cambia su estado a 1 1== ocupado de esta
forma cuando ejecutemos la busqueda de cuartos disponibles solo se mostraran los que tengan 0 es decir sin reservas 
def cambiar_estado():
    
    elegirHabitacion = int(input("Ingrese la habitacion que desea:"))
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == elegirHabitacion:
            habitacion["estado"] = 1
            return f"Estado de la habitación {elegirHabitacion} cambiado a 1"
        else:
            print("valor invalido asigne una habitacion valida")
            cambiar_estado();   
"""
#----------------------------------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE RESERVA 

#Funcion guardar reserva en archivo VALIDAR SI LA SEGUIMOS USANDO O NO

def leer_reservas():
    try:
        with open("reservas.json", "r") as archivo:
            reservas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []  # Si el archivo no existe o está vacío, usar una lista vacía
    return reservas

def guardar_reservas(reservas):
    with open("reservas.json", "w") as archivo:
        json.dump(reservas, archivo, indent=4, default=str) 

def agregar_reserva(nueva_reserva):
    reservas = leer_reservas()
    reservas.append(nueva_reserva)
    guardar_reservas(reservas)

def agregar_habitacion(nueva_habitacion):
    n_habitacion = cargar_habitaciones()
    n_habitacion.append(nueva_habitacion)
    guardar_habitaciones(n_habitacion)

#----------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE MENU

def menu():

    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("============================= ")
        print("┇     🏨 BIENVENIDOS 🏨     ┇ ")
        print("============================= ")
        print("┇                           ┇ ")
        print("┇       \033[4mAdministrador\033[0m       ┇ ")
        print("┇                           ┇ ")
        print("┇       1. Ingreso          ┇ ")
        print("┇       2. Habitaciones     ┇ ")
        print("┇       3. Reservas         ┇ ")
        print("┇       4. CheckOut-In      ┇ ")
        print("┇                           ┇ ")
        print("┇          0. SALIR         ┇ ")
        print("┇                           ┇ ")
        print("============================= ")

        # Inicializamos la variable de respuesta en None
        respuesta = None

        # Validamos la entrada del usuario
        try:
            respuesta = int(input("Seleccione una opción del menú ➡  "))
        except ValueError:
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        if respuesta == 1:  # Registrar el Ingreso.

            os.system('cls' if os.name == 'nt' else 'clear')

            reserva = funcionIngreso()
            if reserva != None:
                agregar_reserva(reserva)
        elif respuesta == 2:  # Ver habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')

            menu_habitaciones_admin()
        elif respuesta == 3:  # Buscar.
            buscarMenu()
        elif respuesta == 4:  # Checkout.
            realizarCheckout()
        elif respuesta == 0:  # Salir del programa.
            bandera = False
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 4). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_habitaciones_admin():

    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("===================================== ")
        print("┇         🏨 Habitaciones 🏨       ┇ ")
        print("===================================== ")
        print("┇                                   ┇ ")
        print("┇       1. Ingresar Habitaciones    ┇ ")
        print("┇       2. Ver Habitacion/es        ┇ ")
        print("┇       3. Modificar Habitacion     ┇ ")
        print("┇       4. Eliminar Habitacion      ┇ ")
        print("┇                                   ┇ ")
        print("┇             0. ATRAS              ┇ ")
        print("┇                                   ┇ ")
        print("===================================== ")

        # Inicializamos la variable de respuesta en None
        respuesta = None

        # Validamos la entrada del usuario
        try:
         respuesta = int(input("Seleccione una opción del menú ➡  "))
        except ValueError:
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        if respuesta == 1:  

            os.system('cls' if os.name == 'nt' else 'clear')

            nueva_habitacion = ingresar_habitacion()
            if nueva_habitacion != None:
                agregar_habitacion(nueva_habitacion)
            else:
                print("No se ingreso ninguna habitacion X")
        elif respuesta == 2:

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_ver_habitaciones()

        elif respuesta == 3:

            os.system('cls' if os.name == 'nt' else 'clear')
            modificar_atributo_habitacion()

        elif respuesta == 4: 
            eliminar_habitacion()
        elif respuesta == 0: 
            bandera = False
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 4). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_ver_habitaciones():

    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("========================================== ")
        print("┇        🏨 Ver Habitacion/es 🏨        ┇ ")
        print("========================================== ")
        print("┇                                        ┇ ")
        print("┇      1. Ver todas las habitaciones     ┇ ")
        print("┇      2. Ver x numero de habitacion     ┇ ")
        print("┇                                        ┇ ")
        print("┇               0. ATRAS                 ┇ ")
        print("┇                                        ┇ ")
        print("========================================== ")

        # Inicializamos la variable de respuesta en None
        respuesta = None

        # Validamos la entrada del usuario
        try:
            respuesta = int(input("Seleccione una opción del menú ➡  "))
        except ValueError:
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

        if respuesta == 1:  # Registrar el Ingreso.

            os.system('cls' if os.name == 'nt' else 'clear')

            ver_todas_las_habitaciones()

        elif respuesta == 2:  # Ver habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')

            ver_habitacion_x_numero()

        elif respuesta == 0:  # Salir del programa.
            bandera = False
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 4). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
    
#--------------------------------------------------------------------------------------------------------------------

def ingresar_habitacion():

    tipo_habitacion = verificar_tipo()
    descripcion = verificar_descripcion()
    valor = verificar_valor()
    capacidad = verificar_capacidad()
    estado = verificar_estado()
    nombre_habitacion = verificar_nombre()
    numero_habitacion = verificar_numero()

    if guardar_datos():
        return None
    else:
        nueva_habitacion = {
        "tipoHabitacion": tipo_habitacion,
        "descripcion": descripcion,
        "valor": valor,
        "cantidadPersonas": capacidad,
        "estado": estado,
        "nombreHabitacion": nombre_habitacion,
        "numeroHabitacion": numero_habitacion
        }
        
        return nueva_habitacion

def ver_todas_las_habitaciones():

    if not habitaciones: #Si no hay habitacion. En este casi simpre hay habitaciones
        print("No hay habitaciones disponibles.")
        return
    
    for habitacion in habitaciones:
        print(f"Nombre de la habitación: {habitacion['nombreHabitacion']}")
        print(f"Número de habitación: {habitacion['numeroHabitacion']}")
        print(f"Tipo de habitación: {habitacion['tipoHabitacion']}")
        print(f"Descripción: {habitacion['descripcion']}")
        print(f"Valor: ${habitacion['valor']}")
        print(f"Capacidad: {habitacion['cantidadPersonas']} personas")
        print(f"Estado: {'Disponible' if habitacion['estado'] == 0 else 'Ocupada'}")
        print("==================================================") 
    
    while True:

        respuesta = None
        
        try:
         respuesta = int(input("Ingrese (0) para volver para atras ➡  "))
        except ValueError:
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        if respuesta == 0:
            return

def ver_habitacion_x_numero():


    numero = input("Ingrese el número de habitación ➡  ")
    habitacion_encontrada = False  # Variable de control para saber si se encontró la habitación

    # Bucle para recorrer todas las habitaciones
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == numero:
            print("==================================================")
            print(f"Nombre de la habitación: {habitacion['nombreHabitacion']}")
            print(f"Número de habitación: {habitacion['numeroHabitacion']}")
            print(f"Tipo de habitación: {habitacion['tipoHabitacion']}")
            print(f"Descripción: {habitacion['descripcion']}")
            print(f"Valor: ${habitacion['valor']}")
            print(f"Capacidad: {habitacion['cantidadPersonas']} personas")
            print(f"Estado: {'Disponible' if habitacion['estado'] == 0 else 'Ocupada'}")
            print("==================================================")
            habitacion_encontrada = True  # Actualiza la variable de control

    # Si no se encontró ninguna habitación, muestra el mensaje una vez
    if not habitacion_encontrada:
        print("Habitación no encontrada.")

    # Bucle para opción de regresar
    while True:
        respuesta = None
        
        try:
            respuesta = int(input("Ingrese (0) para volver para atrás ➡  "))
        except ValueError:
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
            input("Presione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        
        if respuesta == 0:
            return

def modificar_atributo_habitacion():

    numero_habitacion = input("Ingrese el numero de habitacion que desea modificar ➡  ")
    
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == numero_habitacion:
            # Mostrar opciones de atributos para modificar
            print("===================================== ")
            print("Seleccione el atributo que desea modificar:")
            print("1. Número de Habitación")
            print("2. Tipo de Habitación")
            print("3. Descripción")
            print("4. Valor")
            print("5. Cantidad de Personas")
            print("6. Estado")
            print("7. Nombre de Habitación")
            print("===================================== ")

            opcion = input("Ingrese el numero de la opcion que desea modificar ➡  ")

            # Pedir nuevo valor basado en la opción seleccionada
            if opcion == "1":
                habitacion["numeroHabitacion"] = verificar_numero()
            elif opcion == "2":
                habitacion["tipoHabitacion"] = verificar_tipo()
            elif opcion == "3":
                habitacion["descripcion"] = verificar_descripcion()
            elif opcion == "4":
                habitacion["valor"] = verificar_valor()
            elif opcion == "5":
                habitacion["cantidadPersonas"] = verificar_capacidad()
            elif opcion == "6":
                habitacion["estado"] = verificar_estado()
            elif opcion == "7":
                habitacion["nombreHabitacion"] = verificar_nombre()
            else:
                print("Opción no válida X")
                return
            
            guardar_habitaciones(habitaciones)

            print("Atributo actualizado exitosamente ✔ ")
            return

    # Si la habitación no se encuentra
    print("Habitación no encontrada.")
#--------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE INGRESO 1.0

#Ingreso y validacion de datos basicos para el diccionario de huespedes
def funcionIngreso(): 
    
    #----------------------------------------------------------------------------------
    #Parte 1 Ingreso de los valores basicos del titular por medio de funciones

    print("========================== ")
    print("┇   🏨   Ingreso   🏨   ┇ ")
    print("========================== ")
    
    nombre = verificar_nombre()
    apellido = verificar_apellido()
    nacionalidad = verificar_nacionalidad()
    dni_pasaporte = verificar_dni(nacionalidad)
    correo = verificar_correo()
    numero = verificar_telefono()
    fecha_ingreso = verificar_fecha_ingreso()
    fecha_salida = verificar_fecha_salida(fecha_ingreso)
    edad = "Mayor"
    
    #--------------------------------------------------------------------------------------------------------
    
    #Parte 2 Acompanientes, se valida si huesped viene con acompanientes 

    os.system('cls' if os.name == 'nt' else 'clear')

    huespedes = acompaniantes() 
    numeros_de_huespedes = len(huespedes)

    #--------------------------------------------------------------------------------------------------------
    #Nombre Habitaciones printea el nombre de todos los cuartos
    #Se guardan todos los input en un diccionario.
    #

    if guardar_datos():
        return None
    else:
    
        ingresar_habitacion = asignar_habitacion(habitaciones,numeros_de_huespedes,fecha_ingreso,fecha_salida)

        codigoReserva = generar_codigo_reserva(nombre,fecha_ingreso,ingresar_habitacion)

        print("==========================================")
        print("El numero de reserva es : ", codigoReserva)
        print("==========================================")

        reserva = { 
            'Nombre': nombre,
            'Apellido': apellido,
            'Documento': dni_pasaporte,
            'Nacionalidad': nacionalidad,
            'Correo': correo,
            'Numero tel': numero,
            'Fecha_ingreso': fecha_ingreso,
            'Fecha_salida': fecha_salida,
            'Edad': edad,
            'NumeroHabitacion': ingresar_habitacion,
            'CodigoReserva' : codigoReserva,
            #Se almacena acompaniantes en caso de existir
            'Acompanantes' : huespedes
        }
        
        #---------------------------------------------------------------------------------------------------------
        #Parte 3 Seleccion de Habitaciones, la funcion labura con el diccionario previamente llamado del .json 

        return reserva

#Ingreso y validacion de acompanientes en caso de que exista
def acompaniantes(): 
    
    while True:
        try:
            print("======================================")
            print("┇   ¿Vas a ir con algún acompañante? ┇") 
            print("======================================")
            print("┇      1. Si       ┇      2.No       ┇")
            option = int(input("====================================== ➞  ").capitalize())

        
            if option == 1:
                acompaniantes = ingresar_acompanantes() #Llamamos a la funcion. Si tiene acompaniantes.
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Se ingreso correctamente los acompañantes ✔ ")

                return acompaniantes
            elif option == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No se ingresaron acompaniantes X ")

                return "-"  #Devuelve el huesped con los acompaniantes o sin.
            else:
                print("No se ingresó un dato valido.")
        except ValueError:
            print("No se ingresó un número válido. Por favor ingresa 1 o 2.")

#Si existen acompanientes se valida el numero
def ingresar_acompanantes(): 
    bandera = True
    acompanantes = [] #Se hace una lista con los diccionarios de los acompaniantes.
    max_acompanantes = 3 #El maximo de los acompaniantes es 3, ya que nuestras habitaciones maximo de 4 personas (Ingresante + Acompaniantes).

    while bandera:

        

        try:

            print("============================ ")
            print("┇ 🏨    Acompanantes   🏨  ┇")
            print("============================ ")
            print("┇          (1 - 3)         ┇")

            num_acompanantes = int(input("============================ ➞  "))
            

            if num_acompanantes >= 1 and num_acompanantes <= max_acompanantes: #Si ingresamos el numero (1 - 3).

                os.system('cls' if os.name == 'nt' else 'clear')
                
                for i in range(num_acompanantes): 
                    print(f" Ingresando datos del acompañante 【 {i + 1} 】") 
                    nombre = verificar_nombre()
                    apellido = verificar_apellido()
                    acompanante = nombre + " " + apellido

                    acompanantes.append(acompanante) #Se va agregando a la lista.

                    bandera = False #Sale de la bandera.
            else:
                print("x Por favor, ingrese un número válido de acompañantes (1 a 3) x") 
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" ---------------------------------------  ")
            print(" Error - No se ingresó un número válido. ")
            print(" ---------------------------------------  ")
        
        

        
    
    
    

    return acompanantes

#Codigo aleatorio

generar_codigo_reserva = lambda nombre, fecha_ingreso, numeroHabitacion: hashlib.md5(f"{nombre}{fecha_ingreso}{numeroHabitacion}".encode()).hexdigest()[:8]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE INGRESO 1.1 (validamos que los valores asignados por el cliente sea valido)

def verificar_nombre():
    
    while True:
        nombre = input(" • Nombre ➞  ").capitalize()
        if nombre.isalpha(): #Retorna tru si todos los caracteres utilizados son letras
            return nombre
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

def verificar_apellido():
    
    while True:
        apellido = input(" • Apellido ➞  ").capitalize()
        if apellido.isalpha(): #Retorna true si todos los caracteres utilizados son letras
            return apellido
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

def verificar_nacionalidad():

    while True:
        pais = input(" • Nacionalidad 🌍 ➞  ").capitalize() #La primera letra la pone en mayuscula.
        if pais.isalpha(): #Retorna tru si todos los caracteres utilizados son letras
            return pais
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

def verificar_dni(nacionalidad):
    if nacionalidad == "Argentina":
        while True:
        
            dni = input(" • DNI ➞  ")
            if dni.isdigit() and len(dni) == 8:#Retorna true si todos los caracteres utilizados son numero y tiene un largo de 8 numeros
    
            
                return dni
            else:
                print(" ----------------------------------------- ")
                print(" Error - No es ni un Pasaporte, ni un DNI. ")
                print(" ----------------------------------------- ")
    return None

def verificar_correo():
    while True:
        correo = input(" • Correo 📧 ➞  ")
        if correo.count("@") == 1 and correo.count(".") == 1:
            return correo
        else:
            print(" ----------------------------------------- ")
            print("     Error - No se ingreso un correo.      ")
            print(" ----------------------------------------- ")

def verificar_telefono():
    while True:
        numero = input(" • Telefono 📞 ➞  ")
        if numero.isdigit(): #Retorna true si todos los caracteres utilizados son numero
            return numero
        else:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero 📞.    ")
            print(" ----------------------------------------- ")

def verificar_fecha_ingreso():
    while True:
        try:
            ingreso = input(" • Fecha de Ingreso en formato (DD-MM-YYYY) ➞  ").strip()

            # Convertir el input a un objeto datetime solo con fecha
            fecha_ingreso = datetime.strptime(ingreso, "%d %m %Y").date()
            
            # Obtener la fecha actual solo con fecha
            fecha_actual = datetime.now().date()
            
            if fecha_actual <= fecha_ingreso:
                return fecha_ingreso
            else:
                print("x La fecha ingresada es menor a la fecha actual. x")
        
        except ValueError:
            print(" ----------------------------------------- ")
            print("  Error - No se ingresó una fecha válida.  ")
            print(" ----------------------------------------- ")

def verificar_fecha_salida(fecha_ingreso):

    while True:
        try:
            salida = input(" • Fecha de Salida en formato (DD-MM-YYYY) ➞  ").strip()
            
            # Convertir el input a una fecha datetime solo con fecha
            fecha_salida = datetime.strptime(salida, "%d %m %Y").date()
            
            if fecha_ingreso <= fecha_salida:
                return fecha_salida
            else:
                print("x La fecha de salida es menor a la fecha de ingreso. x")
        
        except ValueError:
            print(" ----------------------------------------- ")
            print("  Error - No se ingresó una fecha válida.  ")
            print(" ----------------------------------------- ")

#FUNCION DE INGRESO HABITACIONES

def verificar_tipo():
        
    while True:
        tipo = input(" • Tipo ➞  ").capitalize()
        if tipo.isalpha(): #Retorna tru si todos los caracteres utilizados son letras
            return tipo
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

def verificar_descripcion():
    descripcion = input(" • Descripcion ➞  ").capitalize()
    return descripcion
    
def verificar_valor():
    while True:
        valor = input(" • Valor ➞  ")
        if valor.isdigit(): #Retorna true si todos los caracteres utilizados son numero
            return valor
        else:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero.    ")
            print(" ----------------------------------------- ")

def verificar_capacidad():
    while True:
        try:

            capacidad = int(input(" • Capacidad ➞  "))

            if capacidad == 2 or capacidad == 4:
                return capacidad
            else:
                print("La habitacion no tiene esas capacidad de huespedes X")
        except ValueError:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero.    ")
            print(" ----------------------------------------- ")
    
def verificar_estado():

    while True:
        try:
            
            estado = int(input(" • Estado (0.Disponible o 1.Ocupado) ➞  "))

            if estado == 1 or estado == 0:
                return estado
            else:
                print("No es un Estado valido X")
                
        except ValueError:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero.    ")
            print(" ----------------------------------------- ")
    
def verificar_numero():
    while True:
        numero = input(" • Numero ➞  ")
        if numero.isdigit(): #Retorna true si todos los caracteres utilizados son numero
            return numero
        else:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero.    ")
            print(" ----------------------------------------- ")

def guardar_datos():
    
    print("================================= ")
    print("┇  ¿Quieres guardar los datos?  ┇ ")
    print("================================= ")
        
    while True:
        try:
            print("┇     1. Si     ┇     2.No      ┇     ")
            regresar = int(input("================================= ➞  ").capitalize())

        
            if regresar == 2 or regresar == "No":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sin guardar datos...")
                return True
            elif regresar == 1 or regresar == "Si" :
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Se ingreso correctamente ✔ ")
                return False
                
            else:
                print("No se ingresó un dato valido.")
        except ValueError:
            print("No se ingresó un número válido. Por favor ingresa 1 o 2.")

#------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE PAGOS

#Funcion de subir valor dependiendo el mes de reserva
def ajustar_precio_por_temp(habitaciones, fecha_ingreso):
    """
    Ajusta los precios de las habitaciones según el mes de ingreso del cliente.

    """
    fecha = datetime.strptime(fecha_ingreso, '%Y-%m-%d')
    mes = fecha.month
#CHE ESTO TIENE QUE SER *1.10 1.12 y asi tipo si se alquila de un mes a otro se tiene que multiplicar el valor mas un porcentaje 
    if 1 <= mes <= 3:
        porcentaje = 10  
    elif 4 <= mes <= 7:
        porcentaje = 5   
    elif 8 <= mes <= 12:
        porcentaje = 20  

    print(f"Ajustando precios con un incremento del {porcentaje}% para el mes {mes}.")

    # Ajustar los precios de las habitaciones
    for habitacion in habitaciones:
        incremento = habitacion["valor"] * (porcentaje / 100)
        habitacion["valor"] += int(incremento)  #que quede en entero
        print(f'Habitación {habitacion["numeroHabitacion"]} - Nuevo precio: ${habitacion["valor"]}')

    
    actualizar_habitaciones(habitaciones)
    print("\nPrecios actualizados exitosamente.")
    return habitaciones

# Funcion pago total (queda pendiente)
#def pagoTotal():
habitaciones = cargar_habitaciones()
reservas = leer_reservas()
#------------------------------------------------------------------------------------------------------------------------------------
""""

VALIDAR SI LA USAMOS O HAY QUE RE ESCRIBIRLA

def verificar_disponibilidad():
    pass
                            
def calcularDiasEstadia(diaIngreso, mesIngreso, diaSalida, mesSalida):
    diasTotales = 0
    # Contador de dias totales de estadia
    if mesIngreso == mesSalida:
        # Si el mes de ingreso y salida es el mismo, solo restamos los días
        diasTotales = diaSalida - diaIngreso
    else:
        # Días restantes en el mes de ingreso
        diasRestantesMesIngreso = diasPorMes[mesIngreso] - diaIngreso
        
        # Días en el mes de salida
        diasEnMesSalida = diaSalida
        
        # Días completos en los meses intermedios
        diasIntermedios = 0
        for mes in range(mesIngreso + 1, mesSalida):
            diasIntermedios += diasPorMes[mes]

        # Calculo de la estadia total sumando el mes de ingreso, el intermedio y el de salida.
        diasTotales = diasRestantesMesIngreso + diasIntermedios + diasEnMesSalida
    return diasTotales

def verificar_disponibilidad():
    pass

def funcionEgreso(): # +1 al cuarto ocupado
    pass

def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global
    pass

def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():
    pass
"""
#--------------------------------------------------------------------------------------------------------------------------------


#FUNCIONES QUE HAY QUE RE ESCRIBIR:

#def verificar_disponibilidad(habitaciones, numero_habitacion, fecha_ingreso, fecha_salida):
#--------------------------------------------------------------------------------------------------------------------------------

#Variables globales

habitaciones = cargar_habitaciones()
reservas = leer_reservas()


#-------------------------------------------------------------------------------------------------------------------------------
#Ejecucion del Programa 

menu()
#-------------------------------------------------------------------------------------------------------------------------------
"""
    
    for habitacion in habitaciones:
       if habitacion['numeroHabitacion'] == numero_habitacion:
           for reserva in habitacion.get('reservas', []):
               fecha_entrada_reserva = datetime.strptime(reserva['fechaEntrada'], '%Y-%m-%d')
               fecha_salida_reserva = datetime.strptime(reserva['fechaSalida'], '%Y-%m-%d')

                Verificar si las fechas se solapan
               if not (fecha_salida <= fecha_entrada_reserva or fecha_ingreso >= fecha_salida_reserva):
                   return False  # Hay una superposición, no está disponible
    return True 
"""