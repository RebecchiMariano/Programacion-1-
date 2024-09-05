#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime


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

def funcionMenu():
    pass

def funcionEgreso():
    
    pass

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

def ingresar_titular():
    print("=== Ingrese solo la informacion del titular  de la reserva ===")
    nombre = input(str("Ingrese su nombre : "))
    apellido = input(str("Ingrese su apellido : "))
    dni = int(input("Ingrese su DNI : "))
    mail = str(input("Ingrese su mail : "))
    telefono = int(input("Ingrese su numero de telefono : "))
    metodo_pago = int(input("Ingrese 1. Tarjeta(Dinero en cuenta) o 2.Pago en efectivo() : /n"))

    titular = {
        'nombre': nombre,
        'apellido': apellido,
        'documento': dni,
        'email': mail,
        'telefono': telefono,
        'metodo_pago': metodo_pago,
    }

    return titular

def ingresar_acompanantes(): #Funcion donde devuelve los acompaniantes del titular, su minimo sera 5 y su maximo sera 4
    
    acompanantes = []
    max_acompanantes = 3 #Maximo de personas que entrean en una habitacion
    num_acompanantes = int(input("¿Cuántas personas más harán la reserva junto a usted?( 1 - 3 Personas.)"))

    if num_acompanantes >= max_acompanantes or num_acompanantes <= 1:

        for i in range(num_acompanantes):

            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            dni = int(input("Ingrese el DNI: "))

        acompanante = {
            'nombre': nombre,
            'apellido': apellido,
            'documento': dni,
        }

        acompanantes.append(acompanante)

    return acompanantes


def reserva():

    print("Queremos informar que contamos con habitaciones disponibles únicamente para 2 y 4 personas.")

    titular = ingresar_titular()
    
    con_compania = str(input("Ademas de usted, reservara con alguien mas ? (s/n)"))

    if con_compania == "s":
        return ingresar_acompanantes()
    else:
        return titular
    
