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





def menu(): #Funcion del menu princial.

    bandera = True
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

        bandera2 = True

        respuesta = int(input("Seleccione una opción del menú ➡  "))

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

            print("✕ El numero que ingresaste no esta en el rango de opciones. ✕")
            print("✕✕ Por favor, Ingrese un numero del (0 - 5) ✕✕")


def verHabitaciones():
    pass

def funcionTotalpagar():
    pass

def funcionNumerocliente():
    pass

def verificar_disponibilidad():
    pass

def ingresar_acompanantes():
    bandera = True
    acompanantes = []
    max_acompanantes = 3
    
    
    while bandera:

        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("===== INGRESE LOS DATOS DE LOS ACOMPANIANTES DE LA RESERVA =====")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        num_acompanantes = int(input("¿Cuántas personas más harán la reserva junto a usted? (1 - 3 Personas): "))

        if 1 <= num_acompanantes <= max_acompanantes:
            for _ in range(num_acompanantes):
                nombre = str(input(" • Nombre ➞  "))
                apellido = str(input(" • Apellido ➞  "))
                dni = input(" • DNI ➞  ")

                acompanante = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'documento': dni,
                }

                acompanantes.append(acompanante)

            bandera = False
        else:
            print(" ╳  Por favor, ingrese un número válido de acompañantes (1 a 3) ╳ ")

    return acompanantes

def funcionIngreso():
    huespedes = []
    bandera = True

    while bandera:

        

        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("======= INGRESE LOS DATOS DEL TITULAR DE LA RESERVA =======")
        print("====== ☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰ =====")
        print("=========================================================== ")
        print("=== SI EN ALGUN MOMENTO QUERES SALIR INGRESE \" Salir \" ===")
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        
        nombre = str(input(" • Nombre ➞  "))
        if nombre.lower() == "salir":
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
                            ingreso = input("Día y Mes de ingreso separados por un espacio (DD-MM) ➞  ")
                            if ingreso.lower() == "salir":
                                print("Salir sin guardar datos.")
                                bandera = False
                            else:

                                dia, mes = map(int, ingreso.split())
                                salida = input("Ingrese el día y mes de salida separados por un espacio (DD-MM) ➞  ")
                                if salida.lower() == "salir":
                                    print("Salir sin guardar datos.")
                                    bandera = False
                                else:                       
                                    diaSalida, mesSalida = map(int, salida.split())

                                    print(f"Día de ingreso: {dia}, Mes de ingreso: {mes}")
                                    print(f"Día de salida: {diaSalida}, Mes de salida: {mesSalida}")

                                    # Crear el diccionario del huésped solo si no se eligió salir
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
                                
                                print("Se ingreso correctamente el Titular ✔ ")

                                option = input(" Vas a ir con algun acompaniante ? ")

                                if option.lower() == "Si" or "S":

                                    acompanantes = ingresar_acompanantes()
                                    huesped['acompanantes'] = acompanantes

                                    huespedes.append(huesped)

                                elif option.lower() == "No" or "N":


                                    huespedes.append(huesped)
    
                                
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