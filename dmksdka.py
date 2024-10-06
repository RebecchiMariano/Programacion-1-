import os
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



    
nombre = verificar_nombre()
apellido = verificar_apellido()
pais = verificar_pais()
dni_pasaporte = verificar_dni_pasaporte()
correo = verificar_correo()
numero = verificar_numero()

