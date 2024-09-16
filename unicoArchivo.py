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

habitaciones = { #Vamos a tener 12 habitaciones ()
    
    'normal_2': [{'capacidad': 2, 
                  'reservas': []} for _ in range(3)],
    'normal_4': [{'capacidad': 4, 
                  'reservas': []} for _ in range(3)],
    'premium_2': [{'capacidad': 2, 
                   'reservas': []} for _ in range(3)],
    'premium_4': [{'capacidad': 4, 
                   'reservas': []} for _ in range(3)],
}

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


def convertir_fecha(dia, mes):
    return datetime(2024, mes, dia)

# Ver habitaciones disponibles y ocupadas
def verHabitaciones():
    print("======================================================")
    print("┇          LISTADO DE HABITACIONES DISPONIBLES        ┇")
    print("======================================================")
    
    for tipo, lista_habitaciones in habitaciones.items():
        for i, habitacion in enumerate(lista_habitaciones):
            if len(habitacion['reservas']) == 0:
                estado = "Disponible"
            else:
                estado = "Ocupada"
                
            print(f"Habitación tipo: {tipo}, Número: {i + 1}")
            print(f"   Capacidad: {habitacion['capacidad']} personas")
            print(f"   Estado: {estado}")
            
            if estado == "Ocupada":
                for reserva in habitacion['reservas']:
                    huespedes = reserva.get('huespedes', {})
                    acompanantes = reserva.get('acompanantes', [])
                    nombre_huespedes = huespedes.get('nombre', 'Nombre no disponible')
                    apellido_huespedes = huespedes.get('apellido', 'Apellido no disponible')
                    print(f"   Titular: {nombre_huespedes} {apellido_huespedes}")
                    if acompanantes:
                        print("   Acompañantes:")
                        for acompanante in acompanantes:
                            nombre_acompanante = acompanante.get('nombre', 'Nombre no disponible')
                            apellido_acompanante = acompanante.get('apellido', 'Apellido no disponible')
                            print(f"      - {nombre_acompanante} {apellido_acompanante}")
            print("------------------------------------------------------")
    
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
            for i in range(num_acompanantes):

                print(f" Ingresando datos del acompañante 【 {i + 1} 】")

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

    return acompanantes,num_acompanantes

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
                            ingreso = input(" • Ingreso separados por un espacio (DD-MM) ➞  ")
                            if ingreso.lower() == "salir":
                                print("Salir sin guardar datos.")
                                bandera = False
                            else:
                                dia, mes = map(int, ingreso.split())
                                fecha_ingreso = convertir_fecha(dia, mes)
                                bandera2 = True
                                while bandera2 :
                                    salida = input(" • Salida separados por un espacio (DD-MM) ➞  ")
                                    if salida.lower() == "salir":
                                        print("Salir sin guardar datos.")
                                        bandera = False
                                    else:                       
                                        diaSalida, mesSalida = map(int, salida.split())
                                        fecha_salida = convertir_fecha(diaSalida, mesSalida)

                                        if fecha_salida <= fecha_ingreso:
                                            print("✕ La fecha de salida no puede ser menor o igual a la fecha de ingreso. Inténtelo de nuevo. ✕")
                                        else:
                                            bandera2 = False

                                #Asignacion de numero de cliente
                                print(f"Día de salida: {diaSalida}, Mes de salida: {mesSalida}")
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
                                        
                                    acompanantes , num_acompanantes = ingresar_acompanantes()
                                    huesped['acompanantes'] = acompanantes
                                    print("Se ingreso correctamente los acompañantes ✔ ")
      
                                    
                                elif option == "no" or option == "n":
                                    acompanantes = []
                                    huesped['acompanantes'] = acompanantes
                                
                                bandera = False

                                huespedes.append(huesped)    
                                asignar_habitacion(huespedes, acompanantes, num_acompanantes, fecha_ingreso, fecha_salida)
            
                                #Llamar a que habitacion se va a ingresar

                print(huespedes) #Para que se vea momentanamente los datos almacenados en el diccionario
    return huespedes

                                
def asignar_habitacion(titular, acompanantes, num_acompanantes, fecha_ingreso, fecha_salida):

    seleccion_tipo = input("Seleccione que tipo de habitacion quiere, normal o premium : ").lower()

    if num_acompanantes  <= 1:
        
        if seleccion_tipo == "normal":
            tipos = ['normal_2']
        elif seleccion_tipo == "premium":
            tipos = ['premium_2']
        else:
            print("Seleccion invalida.")
    else:
        if seleccion_tipo == "normal":
            tipos = ['normal_4']
        elif seleccion_tipo == "premium":
            tipos = ['premium_4']
        else:
            print("Seleccion invalida.")

    
    for tipo in tipos:
        for habitacion in habitaciones[tipo]:
            if esta_disponible(fecha_ingreso, fecha_salida, habitacion['reservas']):
                habitacion['reservas'].append({
                    'ingreso': fecha_ingreso,
                    'salida': fecha_salida,
                    'titular': titular,
                    'acompanantes': acompanantes
                })
                print(f"Habitación asignada: {tipo}")
                return tipo
    print("No hay habitaciones disponibles en este rango de fechas.")
    
    return

    
def esta_disponible(fecha_ingreso, fecha_salida, reservas):
    for reserva in reservas:
        # Si el rango de la nueva reserva se solapa con alguna existente
        if (fecha_salida > reserva['ingreso'] or fecha_ingreso < reserva['salida']):
            return False
    return True                               
    

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


# menu(funcionIngreso)
menu()