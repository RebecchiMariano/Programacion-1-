#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random



#Tipo de habitacion

# habitacionesPremium = [premiumX4_playera,premium4_oceano,NormalX4,NormalX2]

#     premiumX4_playera = {
#         'capacidad': 4,
#         'valor': 10000,
#         'Estado' True # este valor tiene que ser pisado dependiendo la opcion que elija el chabon, cuando elije se pisa y se pone false
#     }
#     premiumX4_oceano = {
#         'capacidad': 4,
#         'valor': 15000,
#         'Estado' True
#     }
    
# }





def menu(): #Lista esta

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
            print(funcionIngreso())
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
            print()
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
    pass

def ingresar_acompanantes():
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

    print(verificar_disponibilidad())
    return acompanantes

def funcionIngreso():
    huespedes = []
    bandera = True

    while bandera:

        
        print("== Vas a ingresar un titular, antes del ingreso queres SALIR ? ==")

        opcion = str(input("== Si queres salir ingrese \" Salir \", si quieres seguir dale a \" Enter \" : "))

        if opcion == "":

            print("===========================================================")
            print("======= INGRESE LOS DATOS DEL TITULAR DE LA RESERVA =======")
            print("===========================================================")

            nombre = str(input(" • Nombre ➞  "))
            apellido = str(input(" • Apellido ➞  "))
            dni = int(input(" • DNI ➞  "))
            mail = str(input(" • Mail 📧 ➞  "))
            numero = int(input(" • Telefono 📞 ➞  "))  
            ingreso = input("Día y Mes de ingreso separados por un espacio (DD-MM) ➞  ")
            dia , mes = map(int, ingreso.split())
            salida = input("Ingrese el día y mes de salida separados por un espacio (DD-MM) ➞  ")
            diaSalida, mesSalida = map(int, salida.split())

            print(f"Día de ingreso: {dia}, Mes de ingreso: {mes}")
            print(f"Día de salida: {diaSalida}, Mes de salida: {mesSalida}")

            #fechaIngreso = datetime.now()
            #print(f"La fecha de ingreso del cliente {nombre} {apellido} es {fechaIngreso.strftime('%Y-%m-%d %H:%M:%S')}")
                
            # Crear el diccionario del huésped

            huesped = {
                'Nombre': nombre,
                'Apellido': apellido,
                'DNI': dni,
                'Mail': mail,
                'Número de teléfono': numero,
                'Dia de ingreso': dia,
                'Mes de ingreso': mes,
                'Dia de Salida': diaSalida,
                'Mes de Salida': mesSalida,
                }
                
            huespedes.append(huesped)

            return huespedes

        elif opcion.lower() == "salir":
            bandera = False

            return 
        
        # Llamar la función de acompañantes
    

    

# def verificar_disponibilidad():
#     #hay que importar las variantes de la funcion acompa;antes
#     a_pagar= 0
#     contador = 0
#     diaCuenta = dia
#     diaSalidaCuenta = diaSalida
#     while diaCuenta < diaSalidaCuenta:
#     diaCuenta += 1
#     contador += 1
#     #hay que hacer un filtro de si se pasa de mes es decir se queda del 30 del 5 al 5 del 6 serian solo 7 dias hay que poner limites
#     a_pagar= contador *

# def funcionTotalpagar(): #con los valores de la funcion varificar_disponibilidad() darle las opciones a elegir con el costo de cada una de las variables globalesde habitaciones 
#     print("Ingrese 1. Tarjeta (Dinero en cuenta) o 2. Pago en efectivo")
#     metodo_pago = int(input(""))

# def funcionNumerocliente(): #como ultimo paso de ingreso darle un valor de cuatri digitos con randint al usuario dependiendo del lugar que ocupe en el array es de decirr 1111= posicion ceor [mariano, etc]
#     numeroCliente = random.randint(0000>9999)
#     pass
    
# def funcionEgreso(): # +1 al cuarto ocupado
#     pass

# def verHabitaciones(): #mostrar el array de cuartos de la funcion de habitaciones 
#     pass

# def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global
#     pass

# def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():
#     pass


# menu(funcionIngreso)

menu()