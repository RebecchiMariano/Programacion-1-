#Que hacemos?
#Funciones.
#Menu
#Iniciar Reserva
#Registrar Datos de Cliente
#Funcion Traer Habitacions (dependiendo cantidad de personas a reservar)
#Funcion Checkin y CheckOut

#Array
#Habitaciones Hotel (6,4,2)
#Precios por Habitacion (suit,familiar, temporada)

#Variables
#Precios (.global) 


#Funciones 

#Iniciar Reserva
bandera = True

def iniciarReserva():
    while bandera:
        cantidadDeMiembros = int(input("Cantidad de miembros:"))
        mismoGrupoFamiliar = input("Forman parte del mismo grupo familiar? 1.Si  2.No")
        if mismoGrupoFamiliar == 1:
            #mismo apellido para todos solo pregunta una vez (no se como hacerlo ahora)
            nombresDeLosIntegrantes = input("Nombre de los miembros de la reserva:")
            SumaIntegrantes= nombresDeLosIntegrantes + apellidoDeLosIntegrantes
            #deberia quedar algo asi:
            #sofi Sanchez
            #tomi sanchez 
            #luli Sanches
            
        elif mismoGrupoFamiliar ==2:
            while apellidoYnombres == cantidadDeMiembros:
                apellidoYnombres:apellidoDeLosIntegrantes = input("Apellido de los miembros") and nombresDeLosIntegrantes = input("Nombre de los miembros de la reserva:")
                apellidoYnombres +=1
                #hay que hacerlo romper cuando se iguales los ingresos totales tiene que quedar algo asi:
                #sofi Hernandez
                #sofi Sanchez
                #Mariano Rebecchi
                #Facundo Rebecchi 
        else:
            ("Ingrese un valor valido:")    
        mismoGrupoFamiliar = input("Forman parte del mismo grupo familiar? 1.Si  2.No")
        #volver al bucle hasta que ingrese valor valido 
        
        