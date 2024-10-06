#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random
import os


habitaciones = { #Vamos a tener 12 habitaciones ()
    
    'normal_2': [{'capacidad': 2,
                  'costo': 10000, 
                  'reservas': []} for _ in range(3)], #Creamos 3 habitaciones normales, que tienen una capacidad de 2 personas
                                                      #y dentro habra una lista de reservas.
    'normal_4': [{'capacidad': 4,
                  'costo': 20000, 
                  'reservas': []} for _ in range(3)], #Creamos 3 habitaciones normales, que tienen una capacidad de 4 personas
                                                      #y dentro habra una lista de reservas.
    'premium_2': [{'capacidad': 2,
                   'costo': 25000, 
                   'reservas': []} for _ in range(3)],#Creamos 3 habitaciones premium, que tienen una capacidad de 2 personas
                                                      #y dentro habra una lista de reservas.
    'premium_4': [{'capacidad': 4,
                   'costo': 35000, 
                   'reservas': []} for _ in range(3)],#Creamos 3 habitaciones premium, que tienen una capacidad de 4 personas
                                                      #y dentro habra una lista de reservas.
}

def buscarMenu():
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
            
        
# def pagoTotal():
#     while ingreso
#     sumaDias = ingreso, dias, mes + salida, dias, mes
#     if mes ingreso == mes salida:
#         mes dias == 0
#         #tendria que quedar algo asi mes ingreso = 2 y mes salida =2 
#         #mes 0 + 2
#         # ejemplo final ingreso dias 15 salida dias 30= 

def menu():  # Función del menú principal.
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
            funcionIngreso()
        elif respuesta == 2:  # Ver habitaciones.
            verHabitaciones(habitaciones)
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
       

def funcionIngreso(): # 1) Registrar el Ingreso.

    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print("======= INGRESE LOS DATOS DEL TITULAR DE LA RESERVA =======")
    print("=========================================================== ")
        
    nombre = verificar_nombre()
    apellido = verificar_apellido()
    pais = verificar_pais()
    dni_pasaporte = verificar_dni_pasaporte()
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
        
    if regresar.lower() == 'n' or regresar.lower() == 'no':
        print("Sin guardar datos...")
        return None
                           
    numeroCliente = funcionNumerocliente() #Asignacion de numero de cliente.

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Se ingreso correctamente el Titular ✔ ")

    huesped = { #Se guardan todos los input en un diccionario.
        'Nombre': nombre,
        'Apellido': apellido,
        'Documento': dni_pasaporte,
        'Pais': pais,
        'Correo': correo,
        'Número de teléfono': numero,
        'Fecha de Ingreso': fecha_ingreso,
        'Fecha de Salida': fecha_salida,
        'Edad': edad,
        'Numero de cliente' :numeroCliente,
        'Acompanantes' : [] #Se le va a ingresar una lista de los acompanantes del ingresado.
    }
                                    
    huespedes = acompaniantes(huesped) #Llamamos a la funcion acompaniantes con la biblioteca del ingresado.
    os.system('cls' if os.name == 'nt' else 'clear')

    tipo_habitacion = asignar_habitacion(len(huespedes['Acompanantes']), fecha_ingreso, fecha_salida,huespedes) #Se le asignara una habitacion.

    if tipo_habitacion:
        print(f"Habitación asignada correctamente: {tipo_habitacion} ✔")
    else:
        print("No se pudo asignar una habitación.")

    return huesped

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

def verificar_pais():

    while True:
        pais = input(" • Pais 🌍 ➞  ").capitalize() #La primera letra la pone en mayuscula.
        if pais.isalpha(): #Retorna tru si todos los caracteres utilizados son letras
            return pais
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

def verificar_dni_pasaporte():
    while True:
        dni_pasaporte = input(" • DNI o Pasaporte ➞  ")
        if dni_pasaporte.isdigit() and len(dni_pasaporte) == 8:#Retorna true si todos los caracteres utilizados son numero y tiene un largo de 8 numeros
          print("Se ingreso un DNI ✔")
          return dni_pasaporte
        elif len(dni_pasaporte) == 9:
            print("Se ingreso un Pasaporte ✔")
            dni_pasaporte = dni_pasaporte.upper() #Convierte todo las letras en mayuscular
            return dni_pasaporte
        else:
            print(" ----------------------------------------- ")
            print(" Error - No es ni un Pasaporte, ni un DNI. ")
            print(" ----------------------------------------- ")

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
                                
def convertir_fecha(dia, mes,anio): #Convertimos la fecha con esta funcion con la libreria DateTime. La utilizamos para la funcion ingreso
    return datetime(anio , mes, dia) 

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

        if 1 <= num_acompanantes or num_acompanantes <= max_acompanantes: #Si ingresamos el numero (1 - 3).
            for i in range(num_acompanantes): 
                print(f" Ingresando datos del acompañante 【 {i + 1} 】") 
                nombre = verificar_nombre()
                apellido = verificar_apellido()
                dni_pasaporte = verificar_dni_pasaporte()
                acompanante = { #Diccionario del acompaniante.
                    'nombre': nombre,
                    'apellido': apellido,
                    'documento': dni_pasaporte,
                }

                acompanantes.append(acompanante) #Se va agregando a la lista.

            bandera = False #Sale de la bandera.
        else:
            print("x Por favor, ingrese un número válido de acompañantes (1 a 3) x") 

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

    print("No hay habitaciones disponibles en este rango de fechas. :( ") #Else. Si no encuentra una reserva en la lista de reserva devuelve.
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
