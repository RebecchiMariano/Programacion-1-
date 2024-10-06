import os
from datetime import datetime
def verificar_nombre():
    
    while True:
        nombre = input(" • Nombre ➞  ")
        if nombre.isalpha(): #Retorna tru si todos los caracteres utilizados son letras
            return nombre
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")

    

def verificar_apellido():
    
    while True:
        apellido = input(" • Apellido ➞  ")
        if apellido.isalpha(): #Retorna true si todos los caracteres utilizados son letras
            return apellido
        else:
            print(" ---------------------------------------  ")
            print("        Error - ingresó un número       . ")
            print(" ---------------------------------------  ")


def verificar_pais():

    while True:
        pais = input("Por favor, ingrese un país: ").capitalize() #La primera letra la pone en mayuscula.
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
        correo = input(" • DNI o Pasaporte ➞  ")
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

def convertir_fecha(dia, mes,anio): #Convertimos la fecha con esta funcion con la libreria DateTime. La utilizamos para la funcion ingreso
    return datetime(anio , mes, dia) 

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

    
nombre = verificar_nombre()
apellido = verificar_apellido()
pais = verificar_pais()
dni_pasaporte = verificar_dni_pasaporte()
correo = verificar_correo()
numero = verificar_numero()
fecha_ingreso = verificar_fecha_ingreso()
fecha_salida = verificar_fecha_salida(fecha_ingreso)



