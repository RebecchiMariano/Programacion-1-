from datetime import datetime
import random

#Habitaciones
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

#Costos de Habitaciones
HabitacionPremium = 5000

HabitacionNormal = 2500

def menu():
    print("=====================================================================")
    print("Bienvenido que desea realizar?")
    print("1. Registrar Ingreso")
    print("2. Consultar habitaciones Disponibles")
    print("3. Check Out")
    print("4. Buscar reserva por nombre y apellido")
    print("5. Buscar reserva por numero de reserva")
    
    print("=====================================================================")
    respuesta = int(input("Ingrese accion:"))
    if respuesta == 1:
        funcionIngreso()
    elif respuesta == 2:
        print("#funcion habitaciones")
    elif respuesta ==3:
        print(funcionEgreso)

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

    return acompanantes

def funcionIngreso():
    global metodo_pago 
    huespedes = []
    #contador_personas = 0
    bandera = True
    while bandera:
        print("== Ingrese los datos del titular de la RESERVA ==")
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
    print(ingresar_acompanantes)
    
    
    
    #return huespedes, contador_personas

def verificar_disponibilidad(): #tiene que devolver que habitaciones estan disponibles hay que hacer la variable cantidad de acompa;antes global para poder usarla en esta funcion
    inicio_reserva = input("iniciar reserva : ")
    fin_reserva = input("Que dia quiere finalizar la reserva : ")
    fecha_inicio = datetime.strptime(inicio_reserva, "%d/%m/%Y")
    fecha_fin = datetime.strptime(fin_reserva, "%d/%m/%Y")

def funcionTotalpagar(): #con los valores de la funcion varificar_disponibilidad() darle las opciones a elegir con el costo de cada una de las variables globalesde habitaciones 
    print("Ingrese 1. Tarjeta (Dinero en cuenta) o 2. Pago en efectivo")
    metodo_pago = int(input(""))

def funcionNumerocliente(): #como ultimo paso de ingreso darle un valor de cuatri digitos con randint al usuario dependiendo del lugar que ocupe en el array es de decirr 1111= posicion ceor [mariano, etc]
    numeroCliente = .random(0001>9999)
    
def funcionEgreso(): # +1 al cuarto ocupado

def verHabitaciones(): #mostrar el array de cuartos de la funcion de habitaciones 

def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global

def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():

print(menu())

from datetime import datetime
import random

#Habitaciones
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

#Costos de Habitaciones
HabitacionPremium = 5000

HabitacionNormal = 2500

def menu():
    print("=====================================================================")
    print("Bienvenido que desea realizar?")
    print("1. Registrar Ingreso")
    print("2. Consultar habitaciones Disponibles")
    print("3. Check Out")
    print("4. Buscar reserva por nombre y apellido")
    print("5. Buscar reserva por numero de reserva")
    
    print("=====================================================================")
    respuesta = int(input("Ingrese accion:"))
    if respuesta == 1:
        funcionIngreso()
    elif respuesta == 2:
        print("#funcion habitaciones")
    elif respuesta ==3:
        print(funcionEgreso)

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

    return acompanantes

def funcionIngreso():
    global metodo_pago 
    huespedes = []
    #contador_personas = 0
    bandera = True
    while bandera:
        print("== Ingrese los datos del titular de la RESERVA ==")
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
    print(ingresar_acompanantes)
    
    
    
    #return huespedes, contador_personas

def verificar_disponibilidad(): #tiene que devolver que habitaciones estan disponibles hay que hacer la variable cantidad de acompa;antes global para poder usarla en esta funcion
    inicio_reserva = input("iniciar reserva : ")
    fin_reserva = input("Que dia quiere finalizar la reserva : ")
    fecha_inicio = datetime.strptime(inicio_reserva, "%d/%m/%Y")
    fecha_fin = datetime.strptime(fin_reserva, "%d/%m/%Y")

def funcionTotalpagar(): #con los valores de la funcion varificar_disponibilidad() darle las opciones a elegir con el costo de cada una de las variables globalesde habitaciones 
    print("Ingrese 1. Tarjeta (Dinero en cuenta) o 2. Pago en efectivo")
    metodo_pago = int(input(""))

def funcionNumerocliente(): #como ultimo paso de ingreso darle un valor de cuatri digitos con randint al usuario dependiendo del lugar que ocupe en el array es de decirr 1111= posicion ceor [mariano, etc]
    numeroCliente = .random(0001>9999)
    
def funcionEgreso(): # +1 al cuarto ocupado

def verHabitaciones(): #mostrar el array de cuartos de la funcion de habitaciones 

def buscarResarvaPorNombre(): #con metodos buscar simmilitudes de nombres en el array de huespedes hat que hacerlo global

def buscarReservaPorNumero(): #con la variable global de la funcion funcionNumerocliente():

print(menu())

