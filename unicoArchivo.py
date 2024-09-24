#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random

habitaciones = { #Vamos a tener 12 habitaciones ()
    
    'normal_2': [{'capacidad': 2, 
                  'reservas': []} for _ in range(3)], #Creamos 3 habitaciones normales, que tienen una capacidad de 2 personas
                                                      #y dentro habra una lista de reservas.
    'normal_4': [{'capacidad': 4, 
                  'reservas': []} for _ in range(3)], #Creamos 3 habitaciones normales, que tienen una capacidad de 4 personas
                                                      #y dentro habra una lista de reservas.
    'premium_2': [{'capacidad': 2, 
                   'reservas': []} for _ in range(3)],#Creamos 3 habitaciones premium, que tienen una capacidad de 2 personas
                                                      #y dentro habra una lista de reservas.
    'premium_4': [{'capacidad': 4, 
                   'reservas': []} for _ in range(3)],#Creamos 3 habitaciones premium, que tienen una capacidad de 4 personas
                                                      #y dentro habra una lista de reservas.
}

def menu(): #Funcion del menu princial.

    bandera = True #Con esta bandera cuando lo pongamos en Falso terminaremos el Programa principal.

    while bandera:

        print("====================================================== ")
        print("┇            🏨 BIENVENIDOS AL SISTEMA 🏨            ┇")
        print("====================================================== ")
        print("┇                                                    ┇")
        print("┇         1. Registrar Ingreso                       ┇")
        print("┇         2. Habitaciones Disponibles                ┇")
        print("┇         3. Check Out                               ┇")
        print("┇         4. Buscar reserva x Nombre y Apellido      ┇")
        print("┇         5. Buscar reserva x Numero de Reserva      ┇")
        print("┇                                                    ┇")
        print("┇                    0. SALIR                        ┇")
        print("┇                                                    ┇")
        print("====================================================== ")

        bandera2 = True #Con esta bandera cuando lo pongamos en Falso volveremos al menu ingresando 0.

        respuesta = int(input("Seleccione una opción del menú ➡  "))

        if respuesta == 1: #Registrar el Ingreso.
            funcionIngreso()
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 2:  #Ver habitacion.
            verHabitaciones(habitaciones)
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 3:
            #Funcion Check Out.
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 4:
            #Funcion Buscar Reserva x N y A.
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 5:
            #Funcion Buscar Reserva x Nro de Reserva.
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:  
                    bandera2 = False      
        elif respuesta == 0: #Si se ingresa 0 salimos del programa.
            bandera = False  
        else:

            print("✕ El numero que ingresaste no esta en el rango de opciones. ✕")
            print("✕✕ Por favor, Ingrese un numero del (0 - 5) ✕✕")

def funcionIngreso(): # 1) Registrar el Ingreso.

    bandera = True #Cuando la bandera se ponga en False salimos de la funcion Ingreso.

    while bandera:


        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("======= INGRESE LOS DATOS DEL TITULAR DE LA RESERVA =======")
        print("====== ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ =====")
        print("=========================================================== ")
        print("=== SI EN ALGUN MOMENTO QUERES SALIR INGRESE \" Salir \" ===")
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        
        nombre = str(input(" • Nombre ➞  "))
        if nombre.lower() == "salir": #Si nosotros ponemos Salir en algun input saldremos del programa y no se guardaran datos. ya que sino se ingresa salir pasa al siguiente Else y asi sigue.
            print("Salir sin guardar datos.")
            bandera = False
        else:
            apellido = str(input(" • Apellido ➞  "))
            if apellido.lower() == "salir":
                print("Salir sin guardar datos.")
                bandera = False
            else:
                dni = input(" • DNI ➞  ")
                if dni.lower() == "salir":
                    print("Salir sin guardar datos.")
                    bandera = False
                else:
                    mail = str(input(" • Mail 📧 ➞  "))
                    if mail.lower() == "salir":
                        print("Salir sin guardar datos.")
                        bandera = False
                    else:
                        numero = input(" • Telefono 📞 ➞  ")
                        if numero.lower() == "salir":
                            print("Salir sin guardar datos.")
                            bandera = False
                        else:
                            ingreso = input(" • Ingreso separados por un espacio (DD-MM) ➞  ")
                            if ingreso.lower() == "salir":
                                print("Salir sin guardar datos.")
                                bandera = False
                            else:
                                dia, mes = map(int, ingreso.split()) #Map, int deja a toda la variable en numeros enteros y split los separa en listas. 01 12 , [01 , 12].
                                fecha_ingreso = convertir_fecha(dia, mes) #Llamamos a la funcion de la bilioteca para convertir nuestra fecha.
                                bandera2 = True #Se inicializa siempre.
                                while bandera2 :
                                    salida = input(" • Salida separados por un espacio (DD-MM) ➞  ")
                                    if salida.lower() == "salir":
                                        print("Salir sin guardar datos.")
                                        bandera = False 
                                        bandera2 = False # La bandera1 y bandera2, se vuelven el falso si ponemos salir.
                                    else:                       
                                        diaSalida, mesSalida = map(int, salida.split()) #Map, int deja a toda la variable en numeros enteros y split los separa en listas. 01 12 , [01 , 12].
                                        fecha_salida = convertir_fecha(diaSalida, mesSalida)#Llamamos a la funcion de la bilioteca para convertir nuestra fecha.

                                        if fecha_salida <= fecha_ingreso: #Nunca la fecha de ingreso puede ser menor o igual a la fecha de salida.
                                            print("✕ La fecha de salida no puede ser menor o igual a la fecha de ingreso. Inténtelo de nuevo. ✕")
                                        else:
                                            bandera2 = False
                                            
                                bandera2 = True
                                if bandera and bandera2: # Se tienen que cumplir los 2 requisitos para que se ingrese un huesdep.
                                    
                                    numeroCliente = funcionNumerocliente() #Asignacion de numero de cliente.

                                    print("Se ingreso correctamente el Titular ✔ ")

                                    huesped = { #Se guardan todos los input en un diccionario.
                                        'Nombre': nombre,
                                        'Apellido': apellido,
                                        'DNI': dni,
                                        'Mail': mail,
                                        'Número de teléfono': numero,
                                        'Dia de ingreso': dia,
                                        'Mes de ingreso': mes,
                                        'Dia de Salida': diaSalida,
                                        'Mes de Salida': mesSalida,
                                        'Numero de cliente' :numeroCliente,
                                        'Acompanantes' : [] #Se le va a ingresar una lista de los acompanantes del ingresado.
                                        }
                                    
                                    huespedes = acompaniantes(huesped) #Llamamos a la funcion acompaniantes con la biblioteca del ingresado.

                                    tipo_habitacion = asignar_habitacion(len(huespedes['Acompanantes']), fecha_ingreso, fecha_salida,huespedes) #Se le asignara una habitacion.
                                    if tipo_habitacion:
                                        print(f"Habitación asignada correctamente: {tipo_habitacion} ✔")
                                    else:
                                        print("No se pudo asignar una habitación.")

                                    return huesped
                                else:
                                    return #Volver al menu.
                                
def convertir_fecha(dia, mes): #Convertimos la fecha con esta funcion con la libreria DateTime.
    return datetime(2024, mes, dia)

def funcionNumerocliente():
    numeroCliente = random.randint(1000, 9999) #Se le asignara una id al cliente para que sea mas facil identificarlo.
    return numeroCliente

def acompaniantes(huesped):

    option = input("¿Vas a ir con algún acompañante? (Si/No) ➞  ").lower() #Preguntamos si va a ir solo o con alguien mas.

    if option == "si" or option == "s":
                                        
        acompaniantes = ingresar_acompanantes() #Llamamos a la funcion. Si tiene acompaniantes.

        huesped['Acompanantes'] = acompaniantes #Se le asigna el acompaniante al diccionario 'Acompanantes'.

        print("Se ingreso correctamente los acompañantes ✔ ")
    else: #Si no se ingresa ningun acompaniante, quedara la lisa sin acompaniantes.
        print("No se ingresaron acompaniantes")

    return huesped #Devuelve el huesped con los acompaniantes o sin.

def ingresar_acompanantes(): #Si se ingresa acompaniantes.
    bandera = True
    acompanantes = [] #Se hace una lista con los diccionarios de los acompaniantes.
    max_acompanantes = 3 #El maximo de los acompaniantes es 3, ya que nuestras habitaciones maximo de 4 personas (Ingresante + Acompaniantes).

    while bandera:

        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("===== INGRESE LOS DATOS DE LOS ACOMPANIANTES DE LA RESERVA =====") 
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

        num_acompanantes = int(input("¿Cuántas personas más harán la reserva junto a usted? (1 - 3 Personas): "))

        if 1 <= num_acompanantes <= max_acompanantes: #Si ingresamos el numero (1 - 3).
            for i in range(num_acompanantes): 
                print(f" Ingresando datos del acompañante 【 {i + 1} 】") 
                nombre = str(input(" • Nombre ➞  "))
                apellido = str(input(" • Apellido ➞  "))
                dni = input(" • DNI ➞  ")

                acompanante = { #Diccionario del acompaniante.
                    'nombre': nombre,
                    'apellido': apellido,
                    'documento': dni,
                }

                acompanantes.append(acompanante) #Se va agregando a la lista.

            bandera = False #Sale de la bandera.
        else:
            print(" ╳  Por favor, ingrese un número válido de acompañantes (1 a 3) ╳ ") 

    return acompanantes #Retorna la lista.

def asignar_habitacion(num_acompanantes, fecha_ingreso, fecha_salida, huespedes): #asignar_habitacion(len(huespedes['Acompanantes']), fecha_ingreso, fecha_salida,huespedes).

    #Que beneficios tiene las habitaciones normal y premium. (Proximanente.)

    seleccion_tipo = input("Seleccione qué tipo de habitación quiere, normal o premium: ").lower() #Que tipo de habitacion es premium o normal.
    
    # Determinar el tipo de habitación basado en el número de acompañantes.
    if num_acompanantes <= 1: # (1-2)
        if seleccion_tipo == "normal":
            tipos = ['normal_2']
        elif seleccion_tipo == "premium":
            tipos = ['premium_2']
        else:
            print("Selección inválida.")
            return None
    else: #(3-4)
        if seleccion_tipo == "normal":
            tipos = ['normal_4']
        elif seleccion_tipo == "premium":
            tipos = ['premium_4']
        else:
            print("Selección inválida.")
            return None

# habitaciones = { #Vamos a tener 12 habitaciones ()   
#     'normal_2': [{'capacidad': 2, 
#                   'reservas': []} for _ in range(3)],
#     'normal_4': [{'capacidad': 4, 
#                   'reservas': []} for _ in range(3)], 
#     'premium_2': [{'capacidad': 2, 
#                    'reservas': []} for _ in range(3)],
#     'premium_4': [{'capacidad': 4, 
#                    'reservas': []} for _ in range(3)],
# }

    # Intentar asignar la habitación.
    for tipo in tipos: #Tipo( i ) en tipos.
        for habitacion in habitaciones.get(tipo, []): #Habitacion (i) en habitaciones.
            if esta_disponible(fecha_ingreso, fecha_salida, habitacion['reservas']): #Funcion abajo.
                habitacion['reservas'].append({ #Se agrega las fechas de ingreso y la de los huespedes.
                    'ingreso': fecha_ingreso,
                    'salida': fecha_salida,
                    'huesped': huespedes,  # El diccionario contiene al titular y los acompañantes.
                    #Agregar el numero de la reserva.
                })
                print(f"Habitación asignada: {tipo}")
                return tipo 

    print("No hay habitaciones disponibles en este rango de fechas.") #Else. Si no encuentra una reserva en la lista de reserva devuelve.
    return None

def esta_disponible(fecha_ingreso, fecha_salida, reservas): #Si esta disponible.
    for reserva in reservas: #Va buscar una reserva (i) en las reservas
        if (fecha_salida > reserva['ingreso'] or fecha_ingreso < reserva['salida']): #Si en las fechas de en.
           #15/2 y 31/2 o 17/2 y 31/2 
            return False #Retorna Falso cuando se encuentra una fecha ingresada en la reserva. (No se cumple el if).
    return True #Retora True cuando se encuentra una fecha que no esta en la reserva.  

def verHabitaciones(habitaciones): # 2) Registrar el Ingreso.
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
                    nombre_huesped = huesped.get('Nombre', 'Nombre no disponible') #Nombra del huesped titular.
                    apellido_huesped = huesped.get('Apellido', 'Apellido no disponible')#Apellido del huesped titular.
                    
                    print(f"   Titular: {nombre_huesped} {apellido_huesped}") #Nombre y apellido.
                    
                    # Imprimir los datos de los acompañantes
                    if acompanantes:  # Aquí se comprueba si hay acompañantes
                        print("   Acompañantes:")
                        for acompanante in acompanantes: #Recorro los acompaniantes.
                            nombre_acompanante = acompanante.get('nombre', 'Nombre no disponible') #Nombre de los acompaniantes.
                            apellido_acompanante = acompanante.get('apellido', 'Apellido no disponible') #Apellido de los acompaniantes.
                            print(f"      - {nombre_acompanante} {apellido_acompanante}") #Nombre y apellido.
            print("------------------------------------------------------")
    
    print("======================================================")


# def funcionTotalpagar():
#     pass

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

menu() #Menu del programa.
