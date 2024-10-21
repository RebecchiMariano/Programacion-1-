#--------------------------------------------------------------------------------------------------------------
#Librerias
from datetime import datetime #IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
import random 
import os #Biblioteca para usar la terminar
import json #Biblioteca para usar Json
import hashlib #Biblioteca para usar un numero unico generado.
#---------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------
#Habitaciones Informacion General

#Tipo de habitacion:

#Cada tipo de habitacion tiene 3 unidades cada una 
#habitaciones normales de 2 persons == 1
#habitaciones normales de 4 persons == 2
#habitaciones premium de 2 persons == 3
#habitaciones premium de 4 persons == 4

#Estado de Habitaciones:
#0 libre 1 ocupado
#---------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE HABITACIONES

#Se Trae el conjunto de habitaciones del documento json habitaciones .json, el mismo se utilizara para mostrar el nombre de habitaciones
#Y su posterior re escritura a la hora de reservar una habitacion
def cargar_habitaciones():
    with open('habitaciones.json', 'r') as file:
        habitaciones = json.load(file)
    return habitaciones

#Sobre escribir el diccionario post reserva 
def guardar_habitaciones(habitaciones):
    with open('habitaciones.json', 'w') as file:
        json.dump(habitaciones, file, indent=4)

#Funcion Mostar habitaciones, Muestra todo el Array textual se presente en ese momento la utilizamos para la opcion mostrar habitaciones del menu
def mostrar_habitaciones(habitaciones):
    for habitacion in habitaciones:
        print(f"- {habitacion['numeroHabitacion']} (tipo: {habitacion['tipoHabitacion']}, valor: {habitacion['valor']}, personas: {habitacion['cantidadPersonas']}, estado: {habitacion['estado']}), reservas: {habitacion['reservas']}")

#Funcion Mostrar habitaciones, la utilizamos para mostrar el numero de cuartos a la hora de hacer una reserva, los cuartos mostrados dependeran
#de si ya se encuentran reservadas, estado 1 (Solo mostramos estados 0s) y Segun la cantidad de acompa;antes declarados dentro de ella
#se encuentra la funcion cambiar_estado
def nombre_habitaciones(habitaciones, num_acompanantes):

    for habitacion in habitaciones:
        
        if num_acompanantes == 1 and habitacion['tipoHabitacion'] in [2, 4]:
            continue  

        
        if num_acompanantes >= 2 and habitacion['tipoHabitacion'] in [1, 3]:
            continue  

        
        if habitacion['estado'] == 1:
            continue  

        
        print(f"- {habitacion['numeroHabitacion']}")
        
        
        cambiar_estado()

#La funcion cambiar estado hace que cuando se seleccione un cuarto de los mostrados por nombre habitacion cambia su estado a 1 1== ocupado de esta
#forma cuando ejecutemos la busqueda de cuartos disponibles solo se mostraran los que tengan 0 es decir sin reservas 
def cambiar_estado():
    elegirHabitacion = int(input("Ingrese la habitacion que desea:"))
    for habitacion in habitaciones:
        if habitacion["numeroHabitacion"] == elegirHabitacion:
            habitacion["estado"] = 1
            return f"Estado de la habitación {elegirHabitacion} cambiado a 1"   

#----------------------------------------------------------------------------------------------------------------------------------------------


#ME PUEDEN DECIR PARA QUE ES ESTO ES UN COMMENT?
reservas = []


#-----------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE RESERVA 

#Funcion guardar reserva en archivo VALIDAR SI LA SEGUIMOS USANDO O NO
def guardar_reserva_archivo(reserva):
    try:
        # Cargar las reservas existentes
        reservas = cargar_reservas_archivos()

        # Convertir objetos datetime a cadena
        if isinstance(reserva.get('Fecha_ingreso'), datetime):
            reserva['Fecha_ingreso'] = reserva['Fecha_ingreso'].strftime('%Y-%m-%d')
        if isinstance(reserva.get('Fecha_salida'), datetime):
            reserva['Fecha_salida'] = reserva['Fecha_salida'].strftime('%Y-%m-%d')

        # Añadir la nueva reserva
        reservas.append(reserva)

        # Guardar todas las reservas en formato JSON
        with open("reservas.json", "w") as archivo:
            json.dump(reservas, archivo, indent=4)

        print("Reserva guardada correctamente!")
    except IOError:
        print("No se puede abrir el archivo")

#Funcion cargar reservas archivos VALIDAR SI LA SEGUIMOS USANDO O NO
def cargar_reservas_archivos():

    try:
        # Intentar abrir el archivo JSON de reservas
        with open("reservas.json", "r") as archivo:
            reservas = json.load(archivo)

        # Convertir fechas de cadena a objetos datetime
        for reserva in reservas:
            if 'Fecha_ingreso' in reserva:
                reserva['Fecha_ingreso'] = datetime.strptime(reserva['Fecha_ingreso'], '%Y-%m-%d')
            if 'Fecha_salida' in reserva:
                reserva['Fecha_salida'] = datetime.strptime(reserva['Fecha_salida'], '%Y-%m-%d')

        print("Se cargaron las reservas.")
        return reservas
    except (IOError, json.JSONDecodeError):
        print("No se puede abrir el archivo o el archivo está vacío.")
        return []

#----------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE MENU

#Menu para buscar Habitaciones 
def buscarMenu():

#Funcion Menu Ejecutadora del proyecto
    bandera = True

    
    while bandera:

        print("============================================== ")
        print("┇                🏨 BUSCAR 🏨               ┇ ")
        print("============================================== ")
        print("┇                                            ┇ ")
        print("┇         1. Buscar x Numero de Reserva      ┇ ")
        print("┇         2. Buscar x Nombre y Apellido      ┇ ")
        print("┇         3. Buscar x Habitacion             ┇ ")
        print("┇         4. Buscar x Fecha de Reserva       ┇ ")
        print("┇         5. Buscar x Fecha de Estancia      ┇ ")
        print("┇         6. Buscar x Rango de Fechas        ┇ ")
        print("┇         7. Buscar x Estado de Reserva      ┇ ")
        print("┇         8. Buscar x Tipo de Habitación     ┇ ")
        print("┇         9. Buscar x Número de Huéspedes    ┇ ")
        print("┇         10. Buscar x Método de Pago        ┇ ")
        print("┇                                            ┇ ")
        print("┇                 0. SALIR                   ┇ ")
        print("┇                                            ┇ ")
        print("============================================== ")

        opcion = int(input("Seleccione una opción del menú ➡  "))

        if opcion >= 10 or opcion <= 0:
            print("✕ El numero que ingresaste no esta en el rango de opciones. ✕")  
def menu(reservas):
    


    bandera = True  # Con esta bandera controlamos el ciclo principal del menú.

    while bandera:
        # Mostrar el menú
        print("============================================ ")
        print("┇       🏨 BIENVENIDOS AL SISTEMA 🏨      ┇ ")
        print("============================================ ")
        print("┇                                          ┇ ")
        print("┇         1. Registrar Ingreso             ┇ ")
        print("┇         2. Ver Habitaciones              ┇ ")
        print("┇         3. Buscar                        ┇ ")
        print("┇         4. Checkout                      ┇ ")
        print("┇                                          ┇ ")
        print("┇                 0. SALIR                 ┇ ")
        print("┇                                          ┇ ")
        print("============================================ ")

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
            reserva = funcionIngreso()
            if reserva != None:
                reservas.append(reserva)
                guardar_reserva_archivo(reserva)
        elif respuesta == 2:  # Ver habitaciones.
            print("Habitaciones actuales:")
            mostrar_habitaciones(habitaciones)
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

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
#FUNCIONES DE INGRESO 1.0

#Ingreso y validacion de datos basicos para el diccionario de huespedes
def funcionIngreso(): 
    
    #----------------------------------------------------------------------------------
    #Parte 1 Ingreso de los valores basicos del titular por medio de funciones

    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print("======= INGRESE LOS DATOS DEL TITULAR DE LA RESERVA =======")
    print("=========================================================== ")
    
    nombre = verificar_nombre()
    apellido = verificar_apellido()
    nacionalidad = verificar_nacionalidad()
    dni_pasaporte = verificar_dni(nacionalidad)
    correo = verificar_correo()
    numero = verificar_numero()
    fecha_ingreso = verificar_fecha_ingreso()
    fecha_salida = verificar_fecha_salida(fecha_ingreso)
    edad = "Mayor"
    
    

    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print("=== Estas seguro que quieres guardar los datos del titular? ===")
    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        
    regresar = input("=== Ingrese No/n . Si quieres seguir ingrese cualquier caracter. === ➞  ")
    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    
    #Reset a la consola  
    if regresar.lower() == 'n' or regresar.lower() == 'no':
        print("Sin guardar datos...")
        return None

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Se ingreso correctamente el Titular ✔ ")
    
    #--------------------------------------------------------------------------------------------------------
    
    #Parte 2 Acompanientes, se valida si huesped viene con acompanientes 
    
    huespedes = acompaniantes() 
    #--------------------------------------------------------------------------------------------------------
    #Nombre Habitaciones printea el nombre de todos los cuartos
    #Se guardan todos los input en un diccionario.
    # 
    huesped = { 
        'Nombre': nombre,
        'Apellido': apellido,
        'Documento': dni_pasaporte,
        'Nacionalidad': nacionalidad,
        'Correo': correo,
        'Numero tel': numero,
        'Fecha_ingreso': fecha_ingreso,
        'Fecha_salida': fecha_salida,
        'Edad': edad,
        #'Numero de cliente' :numeroCliente, Esto se elimina ya no usamos randint
        'NumeroHabitacion': numeroHabitacion,
        'CodigoReserva' : codigoReserva,
        #Se almacena acompaniantes en caso de existir
        'Acompanantes' : huespedes
    }
    
    #---------------------------------------------------------------------------------------------------------
    #Parte 3 Seleccion de Habitaciones, la funcion labura con el diccionario previamente llamado del .json 
    
    
    codigoReserva = generar_codigo_reserva(nombre,fecha_ingreso,numeroHabitacion)

    reservas = cargar_reservas_archivos()

#Ingreso y validacion de acompanientes en caso de que exista
def acompaniantes(): 

    option = input("¿Vas a ir con algún acompañante? (Si/No) ➞  ").lower() #Preguntamos si va a ir solo o con alguien mas.

    if option == "si" or option == "s":
                                        
        acompaniantes = ingresar_acompanantes() #Llamamos a la funcion. Si tiene acompaniantes.

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Se ingreso correctamente los acompañantes ✔ ")
        return acompaniantes
    else: #Si no se ingresa ningun acompaniante, quedara la lisa sin acompaniantes.
        os.system('cls' if os.name == 'nt' else 'clear')
        print("No se ingresaron acompaniantes")
        return None  #Devuelve el huesped con los acompaniantes o sin.

#Si existen acompanientes se valida el numero
def ingresar_acompanantes(): 
    bandera = True
    acompanantes = [] #Se hace una lista con los diccionarios de los acompaniantes.
    max_acompanantes = 3 #El maximo de los acompaniantes es 3, ya que nuestras habitaciones maximo de 4 personas (Ingresante + Acompaniantes).

    while bandera:

        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("===== INGRESE LOS DATOS DE LOS ACOMPANIANTES DE LA RESERVA =====") 
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

        num_acompanantes = int(input("¿Cuántas personas más harán la reserva junto a usted? (1 - 3 Personas): "))
        
        

        if 1 <= num_acompanantes or num_acompanantes <= max_acompanantes: #Si ingresamos el numero (1 - 3).
            for i in range(num_acompanantes): 
                print(f" Ingresando datos del acompañante 【 {i + 1} 】") 
                nombre = verificar_nombre()
                apellido = verificar_apellido()
                acompanante = nombre + " " + apellido

                acompanantes.append(acompanante) #Se va agregando a la lista.

            bandera = False #Sale de la bandera.
        else:
            print("x Por favor, ingrese un número válido de acompañantes (1 a 3) x") 
    
    nombre_habitaciones(habitaciones, num_acompanantes)
    

    return acompanantes #Retorna la lista.
    
#!!!!!!!!!!!!!!!!!!!!!hay que re escribir esto porque ahora toda la seleccion de cuarto (la que modifica el estado en el json) se hace con la funcion nombre_habitacion!!!!!!!!!!!!!!!!!
def generar_codigo_reserva(nombre,fecha_ingreso,numeroHabitacion):
    # Concatenamos el nombre, fecha de ingreso y número de habitación
    info_reserva = f"{nombre}{fecha_ingreso}{numeroHabitacion}"
    
    codigo_reserva = hashlib.md5(info_reserva.encode()).hexdigest()[:8]  # Usamos solo los primeros 8 caracteres del hash

    return codigo_reserva

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

def verificar_numero():
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
            
            ingreso = input(" • Fecha de Ingreso separados por un espacio (DD-MM-YYYY) ➞  ")
            dia, mes, anio = map(int, ingreso.split()) #Map, int deja a toda la variable en numeros enteros y split los separa en listas. 01 12 , [01 , 12].
            fecha_ingreso = convertir_fecha(dia, mes, anio)
            fecha_actual = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) #Esto nos dira la fechecha de ahora.
            
            
            if fecha_actual <= fecha_ingreso:
                return fecha_ingreso
            else:
                print("x La fecha ingresada es menor a la fecha actual. x")

        except ValueError:
            print(" ----------------------------------------- ")
            print("  Error - No se ingreso una fecha valida.  ")
            print(" ----------------------------------------- ")

def verificar_fecha_salida(fecha_ingreso):
    while True:
        

        try:
            
            salida = input(" • Fecha de Salida separados por un espacio (DD-MM-YYYY) ➞  ")                    
            diaSalida, mesSalida, anioSalida = map(int, salida.split()) #Map, int deja a toda la variable en numeros enteros y split los separa en listas. 01 12 , [01 , 12].
            fecha_salida = convertir_fecha(diaSalida, mesSalida, anioSalida)#Llamamos a la funcion de la bilioteca para convertir nuestra fecha.
            
            if fecha_ingreso <= fecha_salida:
                return fecha_salida
            else:
                print("x La fecha ingresada es menor a la fecha de ingreso. x")

        except ValueError:
            print(" ----------------------------------------- ")
            print("  Error - No se ingreso una fecha valida.  ")
            print(" ----------------------------------------- ")

#Convertimos la fecha con esta funcion con la libreria DateTime. La utilizamos para la funcion ingreso                                
def convertir_fecha(dia, mes,anio): 
    return datetime(anio , mes, dia) 

#------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------
#Funciones de validacion de Disponibilidad (A CHEQUEAR ESTO)

#La funcion valida si esta disponible
def esta_disponible(fecha_ingreso, fecha_salida, reservas):
    for reserva in reservas: #Va buscar una reserva (i) en las reservas
        if (fecha_salida > reserva['ingreso'] or fecha_ingreso < reserva['salida']): #Si en las fechas de en.
        #15/2 y 31/2 o 17/2 y 31/2 
            return False #Retorna Falso cuando se encuentra una fecha ingresada en la reserva. (No se cumple el if).
    return True #Retora True cuando se encuentra una fecha que no esta en la reserva.  

#AL FINAL ESTO NO LO USAMOS
#def verHabitaciones(habitaciones): # 2) Registrar el Ingreso.
    print("======================================================")
    print("┇          LISTADO DE HABITACIONES DISPONIBLES        ┇")
    print("======================================================")
    
    for tipo, lista_habitaciones in habitaciones.items(): # Recorremos el diccionario 'habitaciones', donde 'tipo' es la clave (por ejemplo, 'premium' o 'normal') y 'lista_habitaciones' es el valor asociado a esa clave (una lista de habitaciones de ese tipo).
        for i, habitacion in enumerate(lista_habitaciones): # Ahora recorremos la lista de habitaciones para ese tipo. (i) indice de habitacion y habitacion el valor de cada habitacion
            if len(habitacion['reservas']) == 0:
                estado = "Disponible" #Si la lista de habitacion no tiene reserva es disponible.
            else:
                estado = "Ocupada" #Si la lista tiene.
            
            print(f"Habitación tipo: {tipo}, Número: {i + 1}")
            print(f"   Capacidad: {habitacion['capacidad']} personas") #Lo que nos mostrara nustro diccionario de habitacion
            print(f"   Estado: {estado}")
            
            if estado == "Ocupada": #Si esta ocupado.
                for reserva in habitacion['reservas']: #Recorremos esa reserva donde tenemos todos los datos de los huespedes.
                    # Obtener los datos del huésped
                    huesped = reserva.get('huesped', {}) #Traemos los huesped de la reserva.
                    acompanantes = huesped.get('Acompanantes', []) #Tramemos los acompaniantes de huespedes.
                    nombre_huesped = huesped.get('Nombre') #Nombra del huesped titular.
                    apellido_huesped = huesped.get('Apellido')#Apellido del huesped titular.
                    
                    print(f"   Titular: {nombre_huesped} {apellido_huesped}") #Nombre y apellido.
                    
                    # Imprimir los datos de los acompañantes
                    if acompanantes:  # Aquí se comprueba si hay acompañantes
                        print("   Acompañantes:")
                        for acompanante in acompanantes: #Recorro los acompaniantes.
                            nombre_acompanante = acompanante.get('nombre') #Nombre de los acompaniantes.
                            apellido_acompanante = acompanante.get('apellido') #Apellido de los acompaniantes.
                            print(f"      - {nombre_acompanante} {apellido_acompanante}") #Nombre y apellido.
            print("------------------------------------------------------")
    
    print("======================================================")

from datetime import datetime

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

#ESTO PARA QUE ES? 
habitaciones = cargar_habitaciones()



#------------------------------------------------------------------------------------------------------------------------------------
#VALIDAR SI LA USAMOS O HAY QUE RE ESCRIBIRLA

# def verificar_disponibilidad():
#     pass
                            
# def calcularDiasEstadia(diaIngreso, mesIngreso, diaSalida, mesSalida):
#     diasTotales = 0
#     # Contador de dias totales de estadia
#     if mesIngreso == mesSalida:
#         # Si el mes de ingreso y salida es el mismo, solo restamos los días
#         diasTotales = diaSalida - diaIngreso
#     else:
#         # Días restantes en el mes de ingreso
#         diasRestantesMesIngreso = diasPorMes[mesIngreso] - diaIngreso
        
#         # Días en el mes de salida
#         diasEnMesSalida = diaSalida
        
#         # Días completos en los meses intermedios
#         diasIntermedios = 0
#         for mes in range(mesIngreso + 1, mesSalida):
#             diasIntermedios += diasPorMes[mes]

#         # Calculo de la estadia total sumando el mes de ingreso, el intermedio y el de salida.
#         diasTotales = diasRestantesMesIngreso + diasIntermedios + diasEnMesSalida
#     return diasTotales

# def verificar_disponibilidad():
#     pass

# def funcionEgreso(): # +1 al cuarto ocupado
#     pass

# def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global
#     pass

# def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():
#     pass

#--------------------------------------------------------------------------------------------------------------------------------


#FUNCIONES QUE HAY QUE RE ESCRIBIR:

def verificar_disponibilidad(habitaciones, numero_habitacion, fecha_ingreso, fecha_salida):


#-------------------------------------------------------------------------------------------------------------------------------
#Ejecucion del Programa 

menu(reservas) 
#-------------------------------------------------------------------------------------------------------------------------------
    
    
    for habitacion in habitaciones:
        if habitacion['numeroHabitacion'] == numero_habitacion:
            for reserva in habitacion.get('reservas', []):
                fecha_entrada_reserva = datetime.strptime(reserva['fechaEntrada'], '%Y-%m-%d')
                fecha_salida_reserva = datetime.strptime(reserva['fechaSalida'], '%Y-%m-%d')

                # Verificar si las fechas se solapan
                if not (fecha_salida <= fecha_entrada_reserva or fecha_ingreso >= fecha_salida_reserva):
                    return False  # Hay una superposición, no está disponible
    return True 