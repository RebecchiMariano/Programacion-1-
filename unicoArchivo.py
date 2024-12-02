#--------------------------------------------------------------------------------------------------------------

#Librerias
from datetime import datetime #IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
import os #Biblioteca para usar la terminar
import json #Biblioteca para usar Json
import hashlib #Biblioteca para usar un numero unico generado.

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE HABITACION (Diccionario)

#Carga la habitacion lo que hace es leerla
def cargar_habitaciones():
    with open('habitaciones.json', 'r') as file:
        habitaciones = json.load(file)
    return habitaciones

#Sobre escribir el diccionario post reserva 
def guardar_habitaciones(habitaciones):
    with open('habitaciones.json', 'w') as file:
        json.dump(habitaciones, file, indent=4)

#Agrega la habitacion       
def agregar_habitacion(nueva_habitacion):
    global habitaciones 
    habitaciones = cargar_habitaciones()  
    habitaciones.append(nueva_habitacion)  
    guardar_habitaciones(habitaciones)

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE RESERVA (Diccionario)

#Lee la reserva
def leer_reservas():
    try:
        with open("reservas.json", "r") as archivo:
            reservas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []  # Si el archivo no existe o está vacío, usar una lista vacía
    return reservas

#Guarda la reserva
def guardar_reservas(reservas):
    with open("reservas.json", "w") as archivo:
        json.dump(reservas, archivo, indent=4, default=str) 

#Agrega la reserva
def agregar_reserva(nueva_reserva):
    global reservas  
    reservas = leer_reservas()  
    reservas.append(nueva_reserva)  
    guardar_reservas(reservas)  


#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE MENU (Usuario y Admin)

def menu_administrador():

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
        elif respuesta == 2:  #Habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_habitaciones_admin()

        elif respuesta == 3:  # Reserva.

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_reservas()
            
        elif respuesta == 4:  # Checkout.

            os.system('cls' if os.name == 'nt' else 'clear')
            menu_check_in_out()

        elif respuesta == 0:  # Salir del programa.
            bandera = False
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 4). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_cliente(reserva):

    
    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        
        # Mostrar el menú
        print("===================================== ")
        print("┇         🏨 BIENVENIDOS 🏨        ┇ ")
        print("===================================== ")
        print("┇                                   ┇ ")
        print("┇              \033[4mCliente\033[0m              ┇ ")
        print("┇                                   ┇ ")
        print(f"      🌟 Bienvenido, {reserva['Nombre']} ")
        print("┇                                   ┇ ")
        print("┇         1. Ver Reserva            ┇ ")
        print("┇         2. Información del Hotel  ┇ ")
        print("┇         3. Servicios              ┇ ")
        print("┇         4. Contactar Recepción    ┇ ")
        print("┇                                   ┇ ")
        print("┇              0. SALIR             ┇ ")
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

        if respuesta == 1:  # Ver detalles de la reserva
            os.system('cls' if os.name == 'nt' else 'clear')

            # Convertir fechas al formato dd/mm/yyyy
            fecha_ingreso = datetime.strptime(reserva['Fecha_ingreso'], "%Y-%m-%d").strftime("%d/%m/%Y")
            fecha_salida = datetime.strptime(reserva['Fecha_salida'], "%Y-%m-%d").strftime("%d/%m/%Y")

            # Calcular la cantidad de días de estadía
            fecha_ingreso_obj = datetime.strptime(reserva['Fecha_ingreso'], "%Y-%m-%d")
            fecha_salida_obj = datetime.strptime(reserva['Fecha_salida'], "%Y-%m-%d")
            cantidad_dias = (fecha_salida_obj - fecha_ingreso_obj).days

            # Buscar la descripción de la habitación
            numero_habitacion = reserva['NumeroHabitacion']
            descripcion_habitacion = ""
            tipo_habitacion = ""
            for habitacion in habitaciones:
                if habitacion['numeroHabitacion'] == numero_habitacion:
                    descripcion_habitacion = habitacion['descripcion']
                    tipo_habitacion = habitacion['tipoHabitacion']
                    break

            # Imprimir los detalles
            print("\n🔍 Detalles de tu reserva:")
            print(f"🏠 Nombre de la habitación: {reserva['NumeroHabitacion']}")
            print(f"🏷️ Tipo de habitación: {tipo_habitacion}")
            print(f"📅 Fechas: {fecha_ingreso} a {fecha_salida}")
            print(f"📝 Descripción: {descripcion_habitacion}")
            print(f"📊 Cantidad de días: {cantidad_dias} días")
            print(f"💵 Total a pagar: ${reserva['TotalPagar']}")
            print("\n¡Esperamos que disfrutes tu estadía! 🌟")
            input("\nPresione Enter para regresar al menú...")

        elif respuesta == 2:  # Información del hotel
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n🏨 Información del Hotel:")
            print("- Dirección: 11 de Septiembre de 1888 1990")
            print("- Teléfono: +123 456 789")
            print("- Servicios: Wi-Fi, Piscina, Spa, Restaurante")
            input("\nPresione Enter para regresar al menú...")

        elif respuesta == 3:  # Servicios adicionales
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n🛎️ Servicios adicionales:")
            print("- Spa: $50")
            print("- Gimnasio: $10")
            print("- Desayuno buffet: $15")
            print("- Traslado aeropuerto: $30")
            print("\n¡Consulta recepción para agregar servicios a tu reserva! 😊")
            input("\nPresione Enter para regresar al menú...")

        elif respuesta == 4:  # Contactar recepción
            os.system('cls' if os.name == 'nt' else 'clear')
            mensaje = input("📩 Escriba su mensaje para la recepción: ")

            if mensaje.strip():  # Verificar que el mensaje no esté vacío
                reservas = leer_reservas()
                codigo_reserva = reserva["CodigoReserva"]
                reserva_encontrada = False

                for r in reservas:
                    if r["CodigoReserva"] == codigo_reserva:
                        r["Mensaje"] = mensaje  # Actualizar el mensaje
                        reserva_encontrada = True
                        break

                if reserva_encontrada:
                    guardar_reservas(reservas)  # Guardar los cambios en el archivo JSON
                    print("\nGracias. Su mensaje ha sido enviado. Nos pondremos en contacto pronto.")
                else:
                    print("\n❌ Error: No se encontró la reserva.")

            else:
                print("\n❌ No se ha enviado ningún mensaje.")
            
            input("\nPresione Enter para regresar al menú...")

        elif respuesta == 0:  # Salir del menú cliente
            bandera = False
            print("\n👋 ¡Gracias por elegirnos! Esperamos verte pronto. 🌟")

        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 6). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#FUNCIONES DE MENUs Administrador

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

            os.system('cls' if os.name == 'nt' else 'clear')

            habitaciones_actualizadas, reservas_actualizadas = eliminar_habitacion_y_reservas()

            # Guardar los datos actualizados si se hizo la eliminación
            if habitaciones_actualizadas is not None and reservas_actualizadas is not None:

                guardar_habitaciones(habitaciones_actualizadas)
                guardar_reservas(reservas_actualizadas)

            
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
                print("✕ Por favor, ingrese un número válido del (0 - 2). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_reservas():

    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("===================================== ")
        print("┇          🏨 Reservas 🏨          ┇ ")
        print("===================================== ")
        print("┇                                   ┇ ")
        print("┇        1. Ver Reserva/as          ┇ ")
        print("┇        2. Modificar Reserva       ┇ ")
        print("┇        3. Eliminar Reserva        ┇ ")
        print("┇                                   ┇ ")
        print("┇              0. ATRAS             ┇ ")
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
            menu_ver_reservas()

        elif respuesta == 2:

            os.system('cls' if os.name == 'nt' else 'clear')
            modificar_atributo_reserva()

        elif respuesta == 3:

            os.system('cls' if os.name == 'nt' else 'clear')

            reservas_actualizadas = eliminar_reserva()

            # Guardar los datos actualizados si se hizo la eliminación
            if reservas_actualizadas is not None:

                guardar_reservas(reservas_actualizadas)
            
        elif respuesta == 0: 
            bandera = False
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 4). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_ver_reservas():

    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("===================================================== ")
        print("┇                 🏨 Ver Reservas 🏨               ┇ ")
        print("===================================================== ")
        print("┇                                                   ┇ ")
        print("┇          1. Ver todas las reservas                ┇ ")
        print("┇          2. Ver x codigo de reserva               ┇ ")
        print("┇          3. Ver próximas reservas x habitacion    ┇ ")
        print("┇                                                   ┇ ")
        print("┇                      0. ATRAS                     ┇ ")
        print("┇                                                   ┇ ")
        print("===================================================== ")

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

            ver_todas_las_reservas()

        elif respuesta == 2:  # Ver habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')

            ver_reserva_x_codigo()
        
        elif respuesta == 3:  # Ver habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')

            ver_proximas_reservas()

        elif respuesta == 0:  # Salir del programa.
            bandera = False
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 3). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

def menu_check_in_out():
    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("========================================== ")
        print("┇           🏨 CheckOut-In 🏨           ┇ ")
        print("========================================== ")
        print("┇                                        ┇ ")
        print("┇             1. Check-In                ┇ ")
        print("┇             2. Check-Out               ┇ ")
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
            check_in()

        elif respuesta == 2:  # Ver habitaciones.

            os.system('cls' if os.name == 'nt' else 'clear')
            check_out()

        elif respuesta == 0:  # Salir del programa.
            bandera = False
        else:
            if respuesta is not None:  # Solo mostrar si la respuesta no fue None
                print("✕ Por favor, ingrese un número válido del (0 - 2). ✕")
                input("Presione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#Funciones de reservas

def ver_todas_las_reservas():

    global reservas
    reservas = leer_reservas()
     
    if not reservas: #Si no hay reservas.
        print("No hay reservas disponibles.")
        return
    
    for reserva in reservas:
        print("==================================================")
        print(f"Nombre: {reserva['Nombre']}")
        print(f"Apellido: {reserva['Apellido']}")
        print(f"Nacionalidad: {reserva['Nacionalidad']}")
        print(f"Documento: {'Sin Dni' if reserva['Documento'] is None else reserva['Documento']}")
        print(f"Correo: {reserva['Correo']}")
        print(f"Numero telefono: {reserva['Numero tel']}")
        print(f"Dia de ingreso: {datetime.strptime(reserva['Fecha_ingreso'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
        print(f"Dia de salida: {datetime.strptime(reserva['Fecha_salida'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
        print(f"Numero de habitacion: {reserva['NumeroHabitacion']}")
        print(f"Codigo de reserva: {reserva['CodigoReserva']}")
        print(f"Total a pagar: {reserva['TotalPagar']} $")
        print(f"Acompañantes: {'Sin acompañantes' if reserva['Acompanantes'] == '-' else ', '.join(reserva['Acompanantes'])}")

        # Mostrar el mensaje de la reserva
        mensaje = reserva.get('Mensaje', '')
        print(f"Mensaje: {mensaje if mensaje else 'No hay mensajes de la reserva'}")
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

def ver_reserva_x_codigo():

    global reservas
    reservas = leer_reservas()

    print("==========  Numero de Reservas  ==========")
    for reserva in reservas:
        print(f"Num. reserva ➡  {reserva['CodigoReserva']}")

    codigo = input("Ingrese el codigo de la reserva ➡  ")
    codigo_encontrado = False  # Variable de control para saber si se encontró la habitación

    # Bucle para recorrer todas las habitaciones
    for reserva in reservas:
        if reserva["CodigoReserva"] == codigo:
            print("==================================================")
            print(f"Nombre: {reserva['Nombre']}")
            print(f"Apellido: {reserva['Apellido']}")
            print(f"Nacionalidad: {reserva['Nacionalidad']}")
            print(f"Documento: {'Sin Dni' if reserva['Documento'] is None else reserva['Documento']}")
            print(f"Correo: {reserva['Correo']}")
            print(f"Numero telefono: {reserva['Numero tel']}")
            print(f"Dia de ingreso: {datetime.strptime(reserva['Fecha_ingreso'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
            print(f"Dia de salida: {datetime.strptime(reserva['Fecha_salida'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
            print(f"Numero de habitacion: {reserva['NumeroHabitacion']}")
            print(f"Codigo de reserva: {reserva['CodigoReserva']}")
            print(f"Total a pagar: {reserva['TotalPagar']} $")
            print(f"Acompañantes: {'Sin acompañantes' if reserva['Acompanantes'] == '-' else ', '.join(reserva['Acompanantes'])}")

            # Mostrar el mensaje de la reserva
            mensaje = reserva.get('Mensaje', '')
            print(f"Mensaje: {mensaje if mensaje else 'No hay mensajes de la reserva'}")
            print("==================================================")

            codigo_encontrado = True  

    # Si no se encontró ninguna habitación, muestra el mensaje una vez
    if not codigo_encontrado:
        print("Reserva no encontrada.")

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

def modificar_atributo_reserva():

    print("==========  Numero de Reservas  ==========")
    for reserva in reservas:
        print(f"Num. reserva ➡  {reserva['CodigoReserva']}")

    codigo = input("Ingrese el codigo de reserva que desea modificar ➡  ")
    
    for reserva in reservas:
        if reserva["CodigoReserva"] == codigo:

            print("==================================================")
            print(f"Nombre: {reserva['Nombre']}")
            print(f"Apellido: {reserva['Apellido']}")
            print(f"Nacionalidad: {reserva['Nacionalidad']}")
            print(f"Documento: {'Sin Dni' if reserva['Documento'] == None else reserva['Documento']}")
            print(f"Correo: {reserva['Correo']}")
            print(f"Numero telefono: {reserva['Numero tel']}")
            print(f"Dia de ingreso: {datetime.strptime(reserva['Fecha_ingreso'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
            print(f"Dia de salida: {datetime.strptime(reserva['Fecha_salida'], '%Y-%m-%d').strftime('%d-%m-%Y')}")
            print(f"Numero de habitacion: {reserva['NumeroHabitacion']}")
            print(f"Codigo de reserva: {reserva['CodigoReserva']}")
            print(f"Total a pagar: {reserva['TotalPagar']}","$")
            print(f"Acompañantes: {'Sin acompañantes' if reserva['Acompanantes'] == '-' else ', '.join(reserva['Acompanantes'])}")
            print("==================================================")
            print("")
            # Mostrar opciones de atributos para modificar
            print("================================================")
            print("┇  Seleccione el atributo que desea modificar: ┇")
            print("┇                                              ┇")
            print("┇                1. Nombre                     ┇")
            print("┇                2. Apellido                   ┇")
            print("┇                3. Nacionalidad               ┇")
            print("┇                4. Documento                  ┇")
            print("┇                5. Correo                     ┇")
            print("┇                6. Numero de telefono         ┇")
            print("┇                7. Dia de ingreso             ┇")
            print("┇                8. Dia de salida              ┇")
            print("┇                9. Numero de habitacion       ┇")
            print("┇               10. Codigo de reserva          ┇")
            print("┇               11. Total a pagar              ┇")
            print("┇               12. Nombre de Acompañantes     ┇")
            print("================================================")

            opcion = input("Ingrese el numero de la opcion que desea modificar ➡  ")

            # Pedir nuevo valor basado en la opción seleccionada
            if opcion == "1":
                reserva["Nombre"] = verificar_nombre()
            elif opcion == "2":
                reserva["Apellido"] = verificar_apellido()
            elif opcion == "3":
                reserva["Nacionalidad"] = verificar_nacionalidad()
            elif opcion == "4":
                reserva["Documento"] = verificar_dni(reserva["Nacionalidad"])
            elif opcion == "5":
                reserva["Correo"] = verificar_correo()
            elif opcion == "6":
                reserva["Numero tel"] = verificar_telefono()
            elif opcion == "7":
                reserva["Fecha_ingreso"] = verificar_fecha_ingreso()
                cantidad_dias = calcularDiasEstadia(reserva["Fecha_ingreso"], reserva["Fecha_salida"])
                reserva["Cantidad_de_dias"] = cantidad_dias
            elif opcion == "8":
                reserva["Fecha_salida"] = verificar_fecha_salida(reserva["Fecha_ingreso"])
                cantidad_dias = calcularDiasEstadia(reserva["Fecha_ingreso"], reserva["Fecha_salida"])
                reserva["Cantidad_de_dias"] = cantidad_dias
            elif opcion == "9":
                reserva["NumeroHabitacion"] = verificar_numero()
            elif opcion == "10":
                reserva["CodigoReserva"] = verificar_codigo_reserva()
            elif opcion == "11":
                reserva["TotalPagar"] = verificar_total_a_pagar()
            elif opcion == "12":
                reserva["Acompanantes"] = acompaniantes()
            else:
                print("Opción no válida X")
                return
            
            guardar_reservas(reservas)

            print("Atributo actualizado exitosamente ✔ ")
            return

    # Si la habitación no se encuentra
    print("Habitación no encontrada.")

def eliminar_reserva():
    """
    Eliminar una reserva
    """

    # Mostrar las reservas disponibles
    print("==========  Numero de Reservas  ==========")
    for reserva in reservas:
        print(f"Num. reserva ➡  {reserva['CodigoReserva']}")

    # Solicitar el código de la reserva a eliminar
    codigo = input("Ingrese el codigo de reserva que desea eliminar ➡  ").strip()

    # Verificar si la reserva existe
    reserva_encontrada = False
    for reserva in reservas:
        if reserva['CodigoReserva'] == codigo:
            reserva_encontrada = True
            break  # Salimos del bucle al encontrar la reserva

    if not reserva_encontrada:
        print(f"La reserva {codigo} no se encuentra en el sistema.")
        input("Presione Enter para salir.")  # Espera a que el usuario presione Enter
        return  # Salimos de la función si no se encuentra la reserva

    # Confirmar la eliminación con el usuario
    confirmacion = input(f"¿Estás seguro de que quieres eliminar la reserva {codigo} (sí/no)? ➡  ").strip().lower()
    if confirmacion != 'si':
        print("Operación cancelada.")
        return  # Salimos si el usuario no confirma la eliminación
    
    # Filtrar las reservas para eliminar la seleccionada
    reservas_actualizadas = [reserva for reserva in reservas if reserva['CodigoReserva'] != codigo]

    print(f"La reserva {codigo} ha sido eliminada.")
    return reservas_actualizadas

def ver_proximas_reservas():
    print("\n========== Lista de Habitaciones ==========")
    # Muestra las habitaciones disponibles
    for habitacion in habitaciones:
        print(f" ➡ Habitacion {habitacion['numeroHabitacion']}")

    # Preguntar por el número de habitación
    numero_habitacion = input("\nIngrese el número de habitación que desea ver las próximas reservas ➡  ")

    # Verificar si la habitación existe
    habitacion_encontrada = False
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == numero_habitacion:
            habitacion_encontrada = True

    if not habitacion_encontrada:
        print("\n🚨 Esa habitación no existe.")
        return

    print(f"\n========== Próximas Reservas para la habitación {numero_habitacion} ==========")
    
    # Filtrar las reservas para la habitación específica
    reservas_habitacion = []
    for reserva in reservas:
        # Convertir las fechas de ingreso y salida a tipo date
        fecha_ingreso_reserva = datetime.strptime(reserva["Fecha_ingreso"], "%Y-%m-%d").date()
        fecha_salida_reserva = datetime.strptime(reserva["Fecha_salida"], "%Y-%m-%d").date()

        # Solo agregamos las reservas de la habitación seleccionada
        if reserva["NumeroHabitacion"] == numero_habitacion:
            reservas_habitacion.append(reserva)
    
    # Ordenar las reservas por fecha de ingreso
    reservas_habitacion.sort(key=lambda r: datetime.strptime(r["Fecha_ingreso"], "%Y-%m-%d").date())

    if reservas_habitacion:
        # Mostrar las reservas encontradas
        for reserva in reservas_habitacion:
            # Formatear las fechas en el formato 'DD-MM-YYYY'
            fecha_ingreso_formateada = datetime.strptime(reserva["Fecha_ingreso"], "%Y-%m-%d").strftime("%d-%m-%Y")
            fecha_salida_formateada = datetime.strptime(reserva["Fecha_salida"], "%Y-%m-%d").strftime("%d-%m-%Y")
            
            print("\n==================================================")
            print(f"👤 **Nombre:** {reserva['Nombre']} {reserva['Apellido']}")
            print(f"📅 **Fechas de Reserva:** {fecha_ingreso_formateada} a {fecha_salida_formateada}")
            print(f"🔑 **Código de Reserva:** {reserva['CodigoReserva']}")
            print("==================================================")
    else:
        print("\n🚫 No hay reservas próximas para esta habitación.")
    
    # Opción para regresar
    while True:
        print("\n==================================================")
        respuesta = input("Ingrese (0) para volver atrás ➡  ")
        if respuesta == "0":
            return

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#Funciones de habitaciones

def ingresar_habitacion():

    tipo_habitacion = verificar_tipo()
    descripcion = verificar_descripcion()
    valor = verificar_valor()
    capacidad = verificar_capacidad()
    estado = verificar_estado()
    nombre_habitacion = verificar_nombre_habitacion()
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
        print("==================================================")
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

    print("========== Lista de Habitaciones ==========")
    for habitacion in habitaciones:
        print(f"Habitacion ➡  {habitacion['numeroHabitacion']}")


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

    print("========== Lista de Habitaciones ==========")
    for habitacion in habitaciones:
        print(f"Habitacion ➡  {habitacion['numeroHabitacion']}")
        
    numero_habitacion = input("Ingrese el numero de habitacion que desea modificar ➡  ")
    
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == numero_habitacion:

            print(f"========= Habitacion : {numero_habitacion} =========")
            print(f"Número de habitación: {habitacion['numeroHabitacion']}")
            print(f"Tipo de habitación: {habitacion['tipoHabitacion']}")
            print(f"Descripción: {habitacion['descripcion']}")
            print(f"Valor: ${habitacion['valor']}")
            print(f"Capacidad: {habitacion['cantidadPersonas']} personas")
            print(f"Estado: {'Disponible' if habitacion['estado'] == 0 else 'Ocupada'}")
            print(f"Nombre de habitacion: {habitacion['nombreHabitacion']}")
            print("========================================== ") 
            print("")
            # Mostrar opciones de atributos para modificar
            print("========================================== ")
            print("Seleccione el atributo que desea modificar:")
            print("                                           ")
            print("          1. Número de Habitación          ")
            print("          2. Tipo de Habitación            ")
            print("          3. Descripción                   ")
            print("          4. Valor                         ")
            print("          5. Cantidad de Personas          ")
            print("          6. Estado                        ")
            print("          7. Nombre de Habitación          ")
            print("========================================== ")

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
                habitacion["nombreHabitacion"] = verificar_nombre_habitacion()
            else:
                print("Opción no válida X")
                return
            
            guardar_habitaciones(habitaciones)

            print("Atributo actualizado exitosamente ✔ ")
            return

    # Si la habitación no se encuentra
    print("Habitación no encontrada.")

def eliminar_habitacion_y_reservas():  
    """
    Elimina la habitación especificada por su número y las reservas asociadas a ella,
    previa confirmación del usuario.
    """

    print("========== Lista de Habitaciones ==========")
    for habitacion in habitaciones:
        print(f"Habitacion ➡  {habitacion['numeroHabitacion']}")

    numero_habitacion = input("Ingrese el numero de habitacion que desea eliminar ➡  ")

    # Verificar si la habitación existe
    habitacion_encontrada = False
    for habitacion in habitaciones:
        if habitacion['numeroHabitacion'] == numero_habitacion:
            habitacion_encontrada = True
            break
    
    if not habitacion_encontrada:
        print(f"La habitación {numero_habitacion} no se encuentra en el sistema.")
        return None, None

    # Contar cuántas reservas están asociadas a la habitación
    contador_reservas = 0
    for reserva in reservas:
        if reserva['NumeroHabitacion'] == numero_habitacion:
            contador_reservas += 1
    
    if contador_reservas == 0:
        print("No hay reservas asociadas a esta habitación.")
    else:
        print(f"⚠️ Advertencia ⚠️: Se eliminarán {contador_reservas} reservas asociadas a la habitación {numero_habitacion}.")

    # Confirmar con el usuario
    confirmacion = input(f"¿Estás seguro de que quieres eliminar la habitación {numero_habitacion} y sus reservas asociadas? (sí/no) ➡  ").strip().lower()
    if confirmacion != 'si':
        print("Operación cancelada.")
        return None, None
    
    # Lista para almacenar las habitaciones actualizadas
    habitaciones_actualizadas = []
    for habitacion in habitaciones:
        if habitacion['numeroHabitacion'] != numero_habitacion:
            habitaciones_actualizadas.append(habitacion)

    # Lista para almacenar las reservas actualizadas
    reservas_actualizadas = []
    for reserva in reservas:
        if reserva['NumeroHabitacion'] != numero_habitacion:
            reservas_actualizadas.append(reserva)

    print(f"Habitacion {numero_habitacion} y sus reservas asociadas han sido eliminadas.")
    return habitaciones_actualizadas, reservas_actualizadas

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

def asignar_habitacion(num_acompanantes,fecha_ingreso,fecha_salida,estadia):
    # Si hay menos de 2 acompañantes, mostrar todas las habitaciones
    print("==================================")
    print("|          Habitaciones          |")
    print("| Numero  -   Nombre   -    Tipo |")
    print("----------------------------------")

    if num_acompanantes < 2:
        for habitacion in habitaciones:
            if habitacion['cantidadPersonas'] == 2:
                print(f"-",habitacion['numeroHabitacion']," ✦",habitacion['nombreHabitacion']," ～",habitacion['tipoHabitacion']," ⟡",habitacion['valor'],"$ x Noche ",f"-")
    # Si hay 2 o más acompañantes, mostrar solo habitaciones con capacidad para 4 personas
    else:
        for habitacion in habitaciones:
            if habitacion['cantidadPersonas'] == 4:
               print(f"-",habitacion['numeroHabitacion']," ✦",habitacion['nombreHabitacion']," ～",habitacion['tipoHabitacion']," ⟡",habitacion['valor'],"$ x Noche ",f"-")
    
    fecha_ingreso_formateada = fecha_ingreso.strftime("%d-%m-%Y")
    fecha_salida_formateada = fecha_salida.strftime("%d-%m-%Y")
    
    print("==================================")
    print("| Fecha de estadia de la reserva |")
    print("| Dia   -     Mes     -    Anio  |")
    print("----------------------------------")
    print("|",fecha_ingreso_formateada,"   Al   ",fecha_salida_formateada,"|")
    print("----------------------------------")
    print("| Estadia  :    ", estadia ,"    Dias       |")
    print("==================================")

    habitacion_valida = False  # Variable de control

    while not habitacion_valida:
        asignar_n_habitacion = input("Ingrese el número de la habitación: ")  # Convertir a string
        habitacion_encontrada = False  # Variable para saber si se encontró la habitación

        # Si hay menos de 2 acompañantes, buscamos habitaciones de capacidad 2
        if num_acompanantes < 2:
            for habitacion in habitaciones:
                if habitacion['cantidadPersonas'] == 2 and asignar_n_habitacion == habitacion['numeroHabitacion']:
                    habitacion_encontrada = True
                    if verificar_disponibilidad(fecha_ingreso, fecha_salida, asignar_n_habitacion):
                        print("Se ingresó la habitación ✔.")
                        habitacion_valida = True
                    else:
                        print("- La habitación no está disponible en las fechas ingresadas -")

        # Si hay 2 o más acompañantes, buscamos habitaciones de capacidad 4
        else:
            for habitacion in habitaciones:
                if habitacion['cantidadPersonas'] == 4 and asignar_n_habitacion == habitacion['numeroHabitacion']:
                    habitacion_encontrada = True
                    if verificar_disponibilidad(fecha_ingreso, fecha_salida, asignar_n_habitacion):
                        print("Se ingresó la habitación ✔.")
                        habitacion_valida = True
                    else:
                        print("- La habitación no está disponible en las fechas ingresadas -")

        # Revisar si no se encontró una habitación válida
        if not habitacion_valida and not habitacion_encontrada:
            print("- Ingrese un número de habitación válido -")
    
    return asignar_n_habitacion

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#Funciones Check-in y Check-out

def check_in():

    codigo_reserva = input("Ingrese el código de la reserva para realizar el check-in ➡  ")
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    reserva_encontrada = False

    # Verificar cada reserva
    for reserva in reservas:
        if reserva['CodigoReserva'] == codigo_reserva:
            reserva_encontrada = True
            # Verificar si la fecha de ingreso coincide con la fecha actual
            if reserva['Fecha_ingreso'] == fecha_hoy:
                numero_habitacion = reserva['NumeroHabitacion']
                
                # Buscar la habitación correspondiente
                for habitacion in habitaciones:
                    if habitacion['numeroHabitacion'] == numero_habitacion:
                        # Verificar si la habitación está disponible (estado 0)
                        if habitacion['estado'] == 0:
                            # Actualizar estado a 1 (ocupada)
                            habitacion['estado'] = 1

                            # Guardar los cambios
                            guardar_habitaciones(habitaciones)
                            guardar_reservas(reservas)

                            print("Check-in realizado con éxito para la habitación:", numero_habitacion)
                            return  # Salir de la función después de un check-in exitoso
                        else:
                            print("La habitación no está disponible para el check-in. X")
                            return

            else:
                print("La fecha de ingreso no coincide con la fecha actual. X")
                return

    if not reserva_encontrada:
        print("No se encontró una reserva con el código ingresado. X")

def check_out():
    
    codigo_reserva = input("Ingrese el código de la reserva para realizar el Check-out ➡  ")
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    reserva_encontrada = False

    # Verificar cada reserva
    for reserva in reservas:
        if reserva['CodigoReserva'] == codigo_reserva:
            reserva_encontrada = True
            # Verificar si la fecha de ingreso coincide con la fecha actual
            if reserva['Fecha_salida'] == fecha_hoy:
                numero_habitacion = reserva['NumeroHabitacion']
                
                # Buscar la habitación correspondiente
                for habitacion in habitaciones:
                    if habitacion['numeroHabitacion'] == numero_habitacion:
                        # Verificar si la habitación está disponible (estado 0)
                        if habitacion['estado'] == 1:
                            # Actualizar estado a 1 (ocupada)
                            habitacion['estado'] = 0

                            # Guardar los cambios
                            guardar_habitaciones(habitaciones)
                            guardar_reservas(reservas)

                            print("Check-in realizado con éxito para la habitación:", numero_habitacion)
                            return  # Salir de la función después de un check-in exitoso
                        else:
                            print("La habitación no está disponible para el Check-out. X")
                            return

            else:
                print("La fecha que ingreso no coincide con la fecha actual. X")
                return

    if not reserva_encontrada:
        print("No se encontró una reserva con el código ingresado. X")

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#Funciones total de pago

def calcularDiasEstadia(fecha_ingreso, fecha_egreso):
    # Convertir a datetime.date solo si es necesario
    if isinstance(fecha_ingreso, str):
        fecha_ingreso = datetime.strptime(fecha_ingreso, '%Y-%m-%d').date()
    if isinstance(fecha_egreso, str):
        fecha_egreso = datetime.strptime(fecha_egreso, '%Y-%m-%d').date()
    
    diasEstadia = (fecha_egreso - fecha_ingreso).days

    if diasEstadia == 0:
        diasEstadia = 1
    
    return diasEstadia

def monto_base_x_dia(total_estadia, num_habitacion,diaEstadia):
    
    for hab in habitaciones:
        if hab["numeroHabitacion"] == num_habitacion:
            if diaEstadia == 1:
                monto_base = (hab["valor"] * total_estadia)
            else:
                monto_base = (hab["valor"] * total_estadia) - hab["valor"]
            
            return monto_base
        
#--------------------------------------------------------------------------------------------------------------------

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

        os.system('cls' if os.name == 'nt' else 'clear')

        diasEstadia = calcularDiasEstadia(fecha_ingreso, fecha_salida)
        ingresar_habitacion = asignar_habitacion(numeros_de_huespedes,fecha_ingreso,fecha_salida,diasEstadia)
        pago_base = monto_base_x_dia(diasEstadia,ingresar_habitacion,diasEstadia)
        codigoReserva = generar_codigo_reserva(nombre,fecha_ingreso,ingresar_habitacion)

        os.system('cls' if os.name == 'nt' else 'clear')

        print("==========================================")
        print("El numero de reserva es : ", codigoReserva)
        print("El total de dias de su estadia es: ",diasEstadia)
        print("El pago base total es : ",pago_base,"$")
        print("==========================================")

        if guardar_datos():
            return None
        else:
            reserva = { 
                'Nombre': nombre,
                'Apellido': apellido,
                'Documento': dni_pasaporte,
                'Nacionalidad': nacionalidad,
                'Correo': correo,
                'Numero tel': numero,
                'Fecha_ingreso': fecha_ingreso,
                'Fecha_salida': fecha_salida,
                'Cantidad_de_dias': diasEstadia,
                'NumeroHabitacion': ingresar_habitacion,
                'CodigoReserva' : codigoReserva,
                'TotalPagar' : pago_base,
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
    # Convertir `fecha_ingreso` a un objeto `datetime.date` si es una cadena
    if isinstance(fecha_ingreso, str):
        fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date() 
    
    while True:
        try:
            salida = input(" • Fecha de Salida en formato (DD-MM-YYYY) ➞  ").strip()
            

            salida = salida.replace(" ", "-")
            
            # Convertir el input a una fecha `datetime.date`
            fecha_salida = datetime.strptime(salida, "%d-%m-%Y").date()
            
            # Comprobar si `fecha_salida` es mayor o igual que `fecha_ingreso`
            if fecha_ingreso <= fecha_salida:
                return fecha_salida
            else:
                print("x La fecha de salida es menor a la fecha de ingreso. x")
        
        except ValueError:
            print(" ----------------------------------------- ")
            print("  Error - No se ingresó una fecha válida.  ")
            print(" ----------------------------------------- ")

def verificar_total_a_pagar():
    while True:
        pago = input(" • Pago $ ➞  ")
        if pago.isdigit():  # Verifica si el valor contiene solo dígitos y no es negativo
            if int(pago) > 0:  # Asegura que sea positivo
                return int(pago)
            else:
                print("Se ingreso un valor menor X")
        else:
            print(" ----------------------------------------- ")
            print("    Error - No se ingreso un numero.    ")
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

def verificar_nombre_habitacion():
    nombre = input(" • Nombre Habitacion ➞  ").capitalize()
    return nombre

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

def verificar_codigo_reserva():
    codigo = input(" • Codigo ➞  ")
    return codigo

#------------------------------------------------------------------------------------------------------------------------------------------------

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
    pass

#------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------

#Variables globales

habitaciones = cargar_habitaciones()
reservas = leer_reservas()

#------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------

#Menu inicio de seccion

def menu_inicio_sesion():
    print("=" * 40)
    print(" " * 10 + "🌟 Hotel Reservas 🌟")
    print("=" * 40)

def menu_principal():

    global reservas
    reservas = leer_reservas()
    global habitaciones
    habitaciones = cargar_habitaciones()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_inicio_sesion()
        usuario = input("👤 Usuario (o escriba 'salir' para finalizar): ")
        if usuario.lower() == "salir":
            print("\nGracias por usar Hotel Reservas. ¡Hasta pronto! 🌟")
            return
        contraseña = input("🔒 Contraseña: ")

        if usuario == "admin" and contraseña == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n✅ Acceso al menú de administrador.")
            menu_administrador()
        else:
            reserva = buscar_reserva(usuario, contraseña)
            if reserva:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n✅ Bienvenido, {reserva['Nombre']} {reserva['Apellido']}.")
                menu_cliente(reserva)
            else:
                print("\n❌ Credenciales incorrectas. Intente nuevamente.")
                input("\nPresione Enter para continuar...") 

def buscar_reserva(correo, codigo):
    for reserva in reservas:
        if reserva["Correo"] == correo and reserva["CodigoReserva"] == codigo:
            return reserva
    return None


#------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------

#Ejecucion del Programa 

menu_principal()

#menu_administrador() Si queremos solo ejecutar el administrador poner este y comentar el de arriba.

#-------------------------------------------------------------------------------------------------------------------------------
