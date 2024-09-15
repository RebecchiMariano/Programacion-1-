#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random



habitaciones = [
    {'tipo': 
     'Premium - Vista Playa', 
     'capacidad': 4, 
     'valor': 15000, 
     'estado': True},
    {'tipo': 
     'Premium - Vista Oceano', 
     'capacidad': 4, 
     'valor': 18000, 
     'estado': True}
    
    ]

#Diccionario para poder hacer funcion verificar_disponibilidad

diasPorMes = {
    1: 31,  # Enero
    2: 28,  # Febrero (Sin considerar los bisiestos)
    3: 31,  # Marzo
    4: 30,  # Abril
    5: 31,  # Mayo
    6: 30,  # Junio
    7: 31,  # Julio
    8: 31,  # Agosto
    9: 30,  # Septiembre
    10: 31,  # Octubre
    11: 30,  # Noviembre
    12: 31   # Diciembre
}

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
            print(verHabitaciones())
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
    print("======================================================")
    print("┇          LISTADO DE HABITACIONES DISPONIBLES        ┇")
    print("======================================================")
    
    # Inicializar el contador manualmente
    contador = 1
    
    for habitacion in habitaciones:
        print(f"{contador}. Tipo: {habitacion['tipo']}")
        print(f"   Capacidad: {habitacion['capacidad']} personas")
        print(f"   Valor por noche: ${habitacion['valor']}")
        print(f"   Estado: {'Disponible' if habitacion['estado'] else 'No disponible'}")
        print("------------------------------------------------------")
        
        # Incrementar el contador
        contador += 1
    
    print("======================================================")

def funcionTotalpagar():
    pass

def funcionNumerocliente():
    numeroCliente = random.randint(1000, 9999)
    return numeroCliente

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

                                    #Asignacion de numero de cliente
                                    numeroCliente = funcionNumerocliente()

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
                                    'Numero de cliente' :numeroCliente
                                    }
                                
                                print("Se ingreso correctamente el Titular ✔ ")

                                option = input("¿Vas a ir con algún acompañante? (Si/No) ➞  ").lower()
                                if option == "si" or option == "s":
                                    acompanantes = ingresar_acompanantes()
                                    huesped['acompanantes'] = acompanantes
                                    huespedes.append(huesped)
                                elif option == "no" or option == "n":
                                    huespedes.append(huesped)

                                print(huesped) #Para que se vea momentanamente los datos almacenados en el diccionario

                                
                                # Llamar la función de acompañantes
    

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



    
# def funcionEgreso(): # +1 al cuarto ocupado
#     pass

# def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global
#     pass

# def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():
#     pass


# menu(funcionIngreso)
menu()