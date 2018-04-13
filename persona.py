#!/usr/bin/python
# -*- coding: utf-8 -*-
def menu():
    print
    print "Gestión de personas"
    print "\t1- Crear"
    print "\t2- Editar"
    print "\t3- Consultar"
    print "\t4- Eliminar"
    print "\t5- Regresar al Menú principal"
    print "\t6- Salir"

def menuEditar():
    print
    print "Editar:"
    print "\t1- Nombre"
    print "\t2- Identificacion"
    print "\t3- Nacionalidad"
    print "\t4- Genero"
    print "\t5- Regresar al menú"

#====CREAR====
nombre=""
identificacion=""
edad=""
nacionalidad=""
genero=""

persona=[]
arrayPersona=[]

arrayNombre=[]
arrayIdentificacion=[]
arrayNacionalidad=[]
arrayGenero=[]
arrayEdad=[]

#====CONSULTAR====
idConsulta=""

#====ELIMINAR====
idEliminar=""

def crear():
    print
    nombre=raw_input("Ingrese su nombre: ")
    identificacion=raw_input("Ingrese su identificación: ")
    edad=raw_input("Ingrese su edad: ")
    nacionalidad=raw_input("Ingrese su nacionalidad: ")
    genero=raw_input("Ingrese su género: ")
    registro=raw_input("¿Desea agregar su registro?(SI/NO) >>")
    if registro=="Si" or registro=="SI" or registro=="si":
        persona=[nombre,identificacion,edad,nacionalidad,genero]
        arrayPersona.append(persona)
        arrayIdentificacion.append(identificacion)
        arrayNombre.append(nombre)
        arrayEdad.append(edad)
        arrayNacionalidad.append(nacionalidad)
        arrayGenero.append(genero)
        print arrayPersona
        print "Registro correcto"
        print
def consultar():
    print
    idConsulta=raw_input("Ingrese el número de identifiación: ")
    print (idConsulta in arrayIdentificacion)
    if (idConsulta in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idConsulta)
        print arrayPersona[posicion]
    else:
        print "No se encontró resultados"
    print

def eliminar():
    print
    idEliminar=raw_input("Ingrese el número de identifiación: ")
    if (idEliminar in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idEliminar)
        print "Datos encontrados: "
        print arrayPersona[posicion]
        print
        respuesta=raw_input("¿Desea eliminarlo?(SI/NO)")
        if respuesta=="SI" or respuesta=="si" or respuesta=="Si":
            arrayPersona.pop(posicion)
            arrayIdentificacion.pop(posicion)
            arrayNombre.pop(posicion)
            arrayEdad.pop(posicion)
            arrayNacionalidad.pop(posicion)
            arrayGenero.pop(posicion)
            print "Los datos se eliminaron correctamente."
        else:
            print "Cancelado"
    print

def editarNombre():
    print
    idNombre=raw_input("Ingrese el número de identifiación: ")
    if (idNombre in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idNombre)
        print "Datos encontrados: "
        print arrayPersona[posicion]

        nuevoNombre=raw_input("Ingrese el nuevo nombre: ");
        arrayNombre[posicion]=nuevoNombre
        nuevaPersona=[nuevoNombre,arrayIdentificacion[posicion],arrayEdad[posicion],arrayNacionalidad[posicion],arrayGenero[posicion]]
        arrayPersona[posicion]=nuevaPersona

        print arrayNombre[posicion]
        print arrayPersona[posicion]
        print "El nombre se cambió correctamente."
    else:
        print "No se pudo cambiar el nombre."
    print

def editarEdad():
    print
    idEdad=raw_input("Ingrese el número de identifiación: ")
    if (idNombre in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idEdad)
        print "Datos encontrados: "
        print arrayPersona[posicion]

        nuevaEdad=raw_input("Ingrese la nueva edad: ");
        arrayEdad[posicion]=nuevaEdad
        nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],nuevaEdad,arrayNacionalidad[posicion],arrayGenero[posicion]]
        arrayPersona[posicion]=nuevaPersona

        print arrayEdad[posicion]
        print arrayPersona[posicion]
        print "La edad se cambió correctamente."
    else:
        print "No se pudo cambiar la edad."
    print

def editarNacionalidad():
    print
    idNacionalidad=raw_input("Ingrese el número de identifiación: ")
    if (idNacionalidad in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idNacionalidad)
        print "Datos encontrados: "
        print arrayPersona[posicion]

        nuevaNacionalidad=raw_input("Ingrese la nueva nacionalidad: ");
        arrayNacionalidad[posicion]=nuevaNacionalidad
        nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],arrayEdad[posicion],nuevaNacionalidad,arrayGenero[posicion]]
        arrayPersona[posicion]=nuevaPersona

        print arrayNacionalidad[posicion]
        print arrayPersona[posicion]
        print "La nacionalidad se cambió correctamente."
    else:
        print "No se pudo cambiar la nacionalidad."
    print

def editarGenero():
    print
    idGenero=raw_input("Ingrese el número de identifiación: ")
    if (idGenero in arrayIdentificacion)==True:
        posicion=arrayIdentificacion.index(idGenero)
        print "Datos encontrados: "
        print arrayPersona[posicion]

        nuevoGenero=raw_input("Ingrese su nuevo género: ");
        arrayGenero[posicion]=nuevoGenero
        nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],arrayEdad[posicion],arrayNacionalidad[posicion],nuevoGenero]
        arrayPersona[posicion]=nuevaPersona

        print arrayGenero[posicion]
        print arrayPersona[posicion]
        print "Su género se cambió correctamente."
    else:
        print "No se pudo cambiar el género."
    print

def editar():
    print
    while True:
        menuEditar()
        opcion=input("Seleccione el elemento que desea editar >>")
        if (opcion==1):
            editarNombre()
        elif (opcion==2):
            editarEdad()
        elif (opcion==3):
            editarNacionalidad()
        elif (opcion==4):
            editarGenero()
        elif (opcion==5):
            break
        else:
            print "Opción incorrecta"
    print

def menuStart():
    while True:
        menu()
        opcion=input("Inserte un número >>")
        if (opcion==1):
            crear()
        elif (opcion==2):
            editar()
        elif (opcion==3):
            consultar()
        elif (opcion==4):
            eliminar()
        elif (opcion==5):
            print "Opción 5"
        elif (opcion==6):
            break
        else:
            print "Opción incorrecta"

menuStart()
