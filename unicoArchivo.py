#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random


#Variables genelares

#Tipos de Habitaciones

habitacionesdupla = 2
habitacionescuatro = 3
#Tipo de habitacion

habitaciones = {
    "Premium": {
        "x4": 3,  # 3 habitaciones de 4 personas
        "x2": 3   # 3 habitaciones de 2 personas
    },
    "Normal": {
        "x4": 3,  # 3 habitaciones de 4 personas
        "x2": 3   # 3 habitaciones de 2 personas
    }
}

# Como acceder a las distintas habitaciones

# habitacionPremiumX4 = habitaciones["Premium"]["x4"]
# habitacionPremiumX2 = habitaciones["Premium"]["x2"]

# habitacionNormalX4 = habitaciones["Normal"]["x4"]
# habitacionNormalX2 = habitaciones["Normal"]["x2"]

#Costos de Habitaciones

HabitacionPremium = 5000

HabitacionNormal = 2500

#Cantidad de Huespedes (2 - 8)

#Cantidad de Habitaciones Disponibles

#CantidadDeHabitacionesDisponibles = habitacionPremiumX4[3]+habitacionPremiumX2[3]+habitacionNormalX4[3]+habitacionNormalX2 =[3]
#hay que hacer un contador para diferenciar las habitaciones es decir que devuelve la cantidad total 12 ej
#6 premium 6 normales
#HabitacionesOcupadas= CantidadDeHabitacionesDisponibles - #valor

# def funcionIngreso(): #Podemos hacer una funcion sobre todos los huespedes de la reserva o una funcion del titular y otra de las personas que los acompanian.
#     huespedes = []
#     contador_personas = 0
#     bandera = True
#     while bandera:
#         print("== Ingrese los datos del titular de la RESERVA ==")
#         nombre = str(input("Ingrese el nombre del Titular : "))
#         if nombre == "Salir" or nombre == "salir":
#             bandera = False
#         else:
#             contador_personas += 1
#             apellido = str(input("Ingrese el apellido del Titular : "))
#             dni = int(input("Ingrese el DNI del Titular : "))
#             mail = str(input("Ingrese el mail donde se enviaran los vaucher : "))
#             numero = int(input("Ingrese el numero de telefono : "))
#             print("Ingrese 1. Tarjeta(Dinero en cuenta) o 2.Pago en efectivo() ")
#             metodo_pago = int(input(""))
            
#             fechaIngreso = datetime.now()
#             print(f"La fecha de ingreso del cliente {nombre,apellido} es {fechaIngreso.strftime('%Y-%m-%d %H:%M:%S')}")
            
#             #POSIBLE DICCIONARIO A USAR
#             huesped = {
#                 "Nombre": nombre,
#                 "Apellido": apellido,
#                 "DNI": dni,
#                 "Mail": mail,
#                 "Telefono": numero,
#                 "MetodoPago": metodo_pago,
#                 "FechaIngreso": fechaIngreso
                
#             }
            
#             huespedes.append(huesped)
#     #Recorre el diccionario e imprime la info de los huespedes.
#     for huesped in huespedes:
#         print("\nInformación del huésped:")
#         for key, value in huesped.items():
#             print(f"{key}: {value}")
#     return huespedes, contador_personas


# def habitacion(clientes):

#     matriz = []

#     for f in range(clientes):
#         matriz.append([0]*6)

#     return print(matriz)

def menu():

    bandera = True
    while bandera:

        print("=====================================================================")
        print("Bienvenido que desea realizar?")
        print("1. Registrar Ingreso")
        print("2. Consultar habitaciones Disponibles")
        print("3. Check Out")
        print("4. Buscar reserva por nombre y apellido")
        print("5. Buscar reserva por numero de reserva")
        print("0. SALIR")
        print("=====================================================================")

        bandera2 = True

        respuesta = int(input("Ingrese accion: "))

        if respuesta == 1:
            print(funcionIngreso)
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 2:
            print("#funcion habitaciones")
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 3:
            print(funcionEgreso)
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 4:
            print("#funcion habitaciones")
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 5:
            print("#funcion habitaciones")
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:  
                    bandera2 = False 
        elif respuesta == 0:
            bandera = False  
        else:

            print("== El numero que ingresaste no esta en el rango de opciones. ==")
            print("== Por favor, Ingrese un numero del (0 - 5). ==")


def verHabitaciones():
    pass

def funcionTotalpagar():
    pass

def funcionNumerocliente():
    pass

def verificar_disponibilidad():
    inicio_reserva = input("iniciar reserva : ")
    fin_reserva = input("Que dia quiere finalizar la reserva : ")
    fecha_inicio = datetime.strptime(inicio_reserva, "%d/%m/%Y")
    fecha_fin = datetime.strptime(fin_reserva, "%d/%m/%Y")


    pass

def funcionIngreso():
    #global metodo_pago 
    huespedes = []
    #contador_personas = 0
    bandera = True
    while bandera:
        print("== Ingrese los datos del titular de la RESERVA ==")
        print("== Si quiere salir al menu ingrese ( salir ) en el nombre del titular ==")
        nombre = str(input("Ingrese el nombre del Titular : "))
        if nombre.lower() == "salir":
            bandera = False
        else:
            #contador_personas += 1
            apellido = str(input("Ingrese el apellido del Titular : "))
            dni = int(input("Ingrese el DNI del Titular : "))
            mail = str(input("Ingrese el mail donde se enviarán los vouchers : "))
            numero = int(input("Ingrese el número de teléfono : "))
            #print("Ingrese 1. Tarjeta (Dinero en cuenta) o 2. Pago en efectivo") esto lo quito va a ir en una funcion total a pagar luego de agregar a los acompa;antes tiene mas sentido despues 
            #metodo_pago = int(input(""))
            
            fechaIngreso = datetime.now()
            print(f"La fecha de ingreso del cliente {nombre} {apellido} es {fechaIngreso.strftime('%Y-%m-%d %H:%M:%S')}")
            if numero >=1:
                bandera=False
            # Crear el diccionario del huésped
            huesped = {
                'Nombre': nombre,
                'Apellido': apellido,
                'DNI': dni,
                'Mail': mail,
                'Número de teléfono': numero,
                #'Método de pago': metodo_pago,
                'Fecha de ingreso': fechaIngreso.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            huespedes.append(huesped)

def ingresar_acompanantes():
    bandera = True
    acompanantes = []
    max_acompanantes = 3
    num_acompanantes = int(input("¿Cuántas personas más harán la reserva junto a usted? (1 - 3 Personas): "))
    
    if 1 <= num_acompanantes <= max_acompanantes:
        for _ in range(num_acompanantes):
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            dni = int(input("Ingrese el DNI: "))

            acompanante = {
                'nombre': nombre,
                'apellido': apellido,
                'documento': dni,
            }

            acompanantes.append(acompanante)
    else:
        print("Por favor, ingrese un número válido de acompañantes (1 a 3).")

    return acompanantes   

def verificar_disponibilidad(): #tiene que devolver que habitaciones estan disponibles hay que hacer la variable cantidad de acompa;antes global para poder usarla en esta funcion
    inicio_reserva = input("iniciar reserva : ")
    fin_reserva = input("Que dia quiere finalizar la reserva : ")
    fecha_inicio = datetime.strptime(inicio_reserva, "%d/%m/%Y")
    fecha_fin = datetime.strptime(fin_reserva, "%d/%m/%Y")

def funcionTotalpagar(): #con los valores de la funcion varificar_disponibilidad() darle las opciones a elegir con el costo de cada una de las variables globalesde habitaciones 
    print("Ingrese 1. Tarjeta (Dinero en cuenta) o 2. Pago en efectivo")
    metodo_pago = int(input(""))

# def funcionNumerocliente(): #como ultimo paso de ingreso darle un valor de cuatri digitos con randint al usuario dependiendo del lugar que ocupe en el array es de decirr 1111= posicion ceor [mariano, etc]
#     numeroCliente = .random(0001>9999)
    
def funcionEgreso(): # +1 al cuarto ocupado
    pass

# def verHabitaciones(): #mostrar el array de cuartos de la funcion de habitaciones 

# def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global

# def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():


print(menu())

