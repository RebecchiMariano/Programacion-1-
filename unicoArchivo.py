
#Variables genelares
#Tipos de Habitaciones

habitacionesdupla = 2
habitacionescuatro = 3

#Habitaciones Premium

#3 habitaciones de 4 personas 
#3 habitaciones de 2 personas

habitacionPremiumX4 = 3
habitacionPremiumX2 = 3


#Habitaciones Normal

#3 habitaciones de 4 personas 
#3 habitaciones de 2 personas

habitacionNormalX4 = 3
habitacionNormalX2 = 3

#Costos de Habitaciones

HabitacionPremium = 5000

HabitacionNormal = 2500

#Cantidad de Huespedes (2 - 8)

#Cantidad de Habitaciones Disponibles

#CantidadDeHabitacionesDisponibles = habitacionPremiumX4[3]+habitacionPremiumX2[3]+habitacionNormalX4[3]+habitacionNormalX2 =[3]
#hay que hacer un contador para diferenciar las habitaciones es decir que devuelve la cantidad total 12 ej
#6 premium 6 normales
#HabitacionesOcupadas= CantidadDeHabitacionesDisponibles - #valor

def funcionIngreso(): #Podemos hacer una fucion sobre todos los huespedes de la reserva o una funcion del titular y otra de las personas que los acompanian.
    contador_personas = 0
    bandera = True
    while bandera:
        print("== Ingrese los datos del titular de la RESERVA ==")
        nombre = str(input("Ingrese el nombre del Titular : "))
        if nombre == "Pedro":
            bandera = False
        else:
            contador_personas += 1
            apellido = str(input("Ingrese el apellido del Titular : "))
            dni = int(input("Ingrese el DNI del Titular : "))
            mail = str(input("Ingrese el mail donde se enviaran los vaucher : "))
            numero = int(input("Ingrese el numero de telefono : "))
            print("Ingrese 1. Tarjeta(Dinero en cuenta) o 2.Pago en efectivo() ")
            metodo_pago = int(input(""))

    return nombre,apellido,dni,mail,numero,metodo_pago,contador_personas


def habitacion(clientes):

    matriz = []

    for f in range(clientes):
        matriz.append([0]*6)

    return print(matriz)

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

nombre,apellido,dni,mail,numero,metodo_pago,contador_personas = funcionIngreso()
habitacion(contador_personas)