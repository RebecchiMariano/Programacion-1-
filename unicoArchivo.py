#IMPORTADA BIBLIOTECA DATETIME, con el fin de trabajar con fechas y horas.
from datetime import datetime
import random



# habitaciones = [
#     {'tipo': 
#      'Premium - Vista Playa', 
#      'capacidad': 4, 
#      'valor': 15000, 
#      'estado': True},
#     {'tipo': 
#      'Premium - Vista Oceano', 
#      'capacidad': 4, 
#      'valor': 18000, 
#      'estado': True}
    
    # ]

habitaciones = { #Vamos a tener 12 habitaciones ()
    
    'normal_2': [{'capacidad': 2, 
                  'reservas': []} for _ in range(1)],

    'normal_4': [{'capacidad': 4, 
                  'reservas': []} for _ in range(1)],

    'premium_2': [{'capacidad': 2, 
                   'reservas': []} for _ in range(1)],

    'premium_4': [{'capacidad': 4, 
                   'reservas': []} for _ in range(1)],
}

#Diccionario para poder hacer funcion verificar_disponibilidad

# diasPorMes = {
#     1: 31,  # Enero
#     2: 28,  # Febrero (Sin considerar los bisiestos)
#     3: 31,  # Marzo
#     4: 30,  # Abril
#     5: 31,  # Mayo
#     6: 30,  # Junio
#     7: 31,  # Julio
#     8: 31,  # Agosto
#     9: 30,  # Septiembre
#     10: 31,  # Octubre
#     11: 30,  # Noviembre
#     12: 31   # Diciembre
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
            funcionIngreso()
            while bandera2:
                volver = int(input("Para volver al menu ingrese ( 0 ) : "))
                if volver == 0:
                    bandera2 = False 
        elif respuesta == 2:
            verHabitaciones(habitaciones)
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

def verHabitaciones(habitaciones):
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
                    # Obtener los datos del huésped
                    huesped = reserva.get('huesped', {})
                    acompanantes = huesped.get('Acompanantes', [])
                    nombre_huesped = huesped.get('Nombre', 'Nombre no disponible')
                    apellido_huesped = huesped.get('Apellido', 'Apellido no disponible')
                    
                    print(f"   Titular: {nombre_huesped} {apellido_huesped}")
                    
                    # Imprimir los datos de los acompañantes
                    if acompanantes:  # Aquí se comprueba si hay acompañantes
                        print("   Acompañantes:")
                        for acompanante in acompanantes:
                            # Usar get() para manejar posibles claves faltantes
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

def funcionIngreso():
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
                                        bandera2 = False
                                    else:                       
                                        diaSalida, mesSalida = map(int, salida.split())
                                        fecha_salida = convertir_fecha(diaSalida, mesSalida)

                                        if fecha_salida <= fecha_ingreso:
                                            print("✕ La fecha de salida no puede ser menor o igual a la fecha de ingreso. Inténtelo de nuevo. ✕")
                                        else:
                                            bandera2 = False

                                if bandera and bandera2: # Se tienen que cumplir los 2 requisitos para que se ingrese un huesdep.
                                    #Asignacion de numero de cliente
                                    numeroCliente = funcionNumerocliente()

                                    print("Se ingreso correctamente el Titular ✔ ")

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
                                        'Numero de cliente' :numeroCliente,
                                        'Acompanantes' : []
                                        }
                                    
                                    huespedes = acompaniantes(huesped)

                                    tipo_habitacion = asignar_habitacion(len(huespedes['Acompanantes']), fecha_ingreso, fecha_salida,huespedes)

                                    if tipo_habitacion:
                                        print(f"Habitación asignada correctamente: {tipo_habitacion} ✔")
                                    else:
                                        print("No se pudo asignar una habitación.")

                                    return huesped
                                else:
                                    return

def acompaniantes(huesped):
    option = input("¿Vas a ir con algún acompañante? (Si/No) ➞  ").lower()

    if option == "si" or option == "s":
                                        
        acompaniantes = ingresar_acompanantes()
        huesped['Acompanantes'] = acompaniantes
        print("Se ingreso correctamente los acompañantes ✔ ")
    else:
        print("No se ingresaron acompaniantes")

    return huesped
    
def ingresar_acompanantes():
    bandera = True
    acompanantes = []
    max_acompanantes = 3

    while bandera:
        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
        print("===== INGRESE LOS DATOS DE LOS ACOMPANIANTES DE LA RESERVA =====")
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

    return acompanantes



                                
def asignar_habitacion(num_acompanantes, fecha_ingreso, fecha_salida, huespedes):
    seleccion_tipo = input("Seleccione qué tipo de habitación quiere, normal o premium: ").lower()
    
    # Determinar el tipo de habitación basado en el número de acompañantes
    if num_acompanantes <= 1:
        if seleccion_tipo == "normal":
            tipos = ['normal_2']
        elif seleccion_tipo == "premium":
            tipos = ['premium_2']
        else:
            print("Selección inválida.")
            return None
    else:
        if seleccion_tipo == "normal":
            tipos = ['normal_4']
        elif seleccion_tipo == "premium":
            tipos = ['premium_4']
        else:
            print("Selección inválida.")
            return None
    

    # Intentar asignar la habitación
    for tipo in tipos:
        for habitacion in habitaciones.get(tipo, []):  # Usa .get() para evitar KeyError si el tipo no existe
            if esta_disponible(fecha_ingreso, fecha_salida, habitacion['reservas']):
                habitacion['reservas'].append({
                    'ingreso': fecha_ingreso,
                    'salida': fecha_salida,
                    'huesped': huespedes,  # El diccionario contiene al titular y los acompañantes
                })
                print(f"Habitación asignada: {tipo}")
                return tipo

    print("No hay habitaciones disponibles en este rango de fechas.")
    return None



    
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
