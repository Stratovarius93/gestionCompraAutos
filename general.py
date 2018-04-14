#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
#=====P E R S O N A S=====
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

#======VARIABLES CLASE AUTO=======
class Car:
    def __init__(self, mark, year, model, motor, km, cost):
        self.mark = mark
        self.year = year
        self.model = model
        self.motor = motor
        self.km = km
        self.cost = cost
Chevrolet = Car("Chevrolet", "2018", "Sail", "109 hp", "0 km", "45,000.00")
Toyota = Car("Toyota", "2018", "Fortuner", "163 hp", "0 km", "34,500.00")
Honda = Car("Honda", "2016", "HR-V", "141 hp", "100 km", "20,104.00")
Nissan = Car("Nissan", "2017", "SUV", "118 hp", "50 km", "26,700.00")

arrayChevrolet = []
arrayToyota = []
arrayHonda = []
arrayNissan = []
arrayCar = []

aprobacionCompra=0
posicionP=0
class Buy():
    def buying(self):
        print "============================================"
        print "Que marca de auto le gustaria adquirir"
        print "============================================"
        print ("\t1 - Chevrolet")
        print ("\t2 - Toyota")
        print ("\t3 - Honda")
        print ("\t4 - Nissan")
        print ("\t5 - Regresar al Menu principal")
class Pay():
    pass

class persona():
    def menuP(self):
        print
        print "================================="
        print "\tGestión de personas"
        print "================================="
        print "\t1- Crear"
        print "\t2- Editar"
        print "\t3- Consultar"
        print "\t4- Eliminar"
        print "\t5- Regresar al Menú principal"
        print
    def menuEditar(self):
        print
        print "================================="
        print "Editar:"
        print "================================="
        print "\t1- Nombre"
        print "\t2- Edad"
        print "\t3- Nacionalidad"
        print "\t4- Genero"
        print "\t5- Regresar al menú"
        print
    #======METODOS======
    def calcularSalario():
        print "Salario"
    def calcularNumeroAutos():
        print "# Autos"
    def calcularValorAuto():
        print "Valor Auto"

    #======CRUD========
    def crear(self):
        print "================================="
        print "Crear:"
        print "================================="
        print
        nombre=raw_input("Ingrese su nombre: ")
        print
        identificacion=raw_input("Ingrese su identificación: ")
        print
        edad=raw_input("Ingrese su edad: ")
        print
        nacionalidad=raw_input("Ingrese su nacionalidad: ")
        print
        genero=raw_input("Ingrese su género: ")
        print
        registro=raw_input("¿Desea agregar su registro?(SI/NO) >> ")
        print
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
    def consultar(self):
        print
        print "================================="
        print "Consultar:"
        print "================================="
        print
        idConsulta=raw_input("Ingrese el número de identifiación: ")
        #print (idConsulta in arrayIdentificacion)
        if (idConsulta in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idConsulta)
            print "Datos encontrados: "
            print
            print "================================="
            print arrayPersona[posicion]
            print "================================="
        else:
            print "No se encontró resultados"
        print

    def eliminar(self):
        print
        print "================================="
        print "Eliminar:"
        print "================================="
        print
        idEliminar=raw_input("Ingrese el número de identifiación: ")
        if (idEliminar in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idEliminar)
            print "Datos encontrados: "
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="
            print
            respuesta=raw_input("¿Desea eliminarlo?(SI/NO) >>")
            if respuesta=="SI" or respuesta=="si" or respuesta=="Si":
                arrayPersona.pop(posicion)
                arrayIdentificacion.pop(posicion)
                arrayNombre.pop(posicion)
                arrayEdad.pop(posicion)
                arrayNacionalidad.pop(posicion)
                arrayGenero.pop(posicion)
                print
                print "Los datos se eliminaron correctamente."
            else:
                print
                print "Cancelado"
        print

    def editarNombre(self):
        print
        idNombre=raw_input("Ingrese el número de identifiación: ")
        if (idNombre in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idNombre)
            print "Datos encontrados: "
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="

            nuevoNombre=raw_input("Ingrese el nuevo nombre: ");
            arrayNombre[posicion]=nuevoNombre
            nuevaPersona=[nuevoNombre,arrayIdentificacion[posicion],arrayEdad[posicion],arrayNacionalidad[posicion],arrayGenero[posicion]]
            arrayPersona[posicion]=nuevaPersona

            print
            print arrayNombre[posicion]
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="
            print
            print "El nombre se cambió correctamente."
        else:
            print "No se pudo cambiar el nombre."
        print

    def editarEdad(self):
        print
        idEdad=raw_input("Ingrese el número de identifiación: ")
        if (idNombre in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idEdad)
            print "Datos encontrados: "
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="

            nuevaEdad=raw_input("Ingrese la nueva edad: ");
            arrayEdad[posicion]=nuevaEdad
            nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],nuevaEdad,arrayNacionalidad[posicion],arrayGenero[posicion]]
            arrayPersona[posicion]=nuevaPersona

            print
            print arrayEdad[posicion]
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="
            print
            print "La edad se cambió correctamente."
        else:
            print "No se pudo cambiar la edad."
        print

    def editarNacionalidad(self):
        print
        idNacionalidad=raw_input("Ingrese el número de identifiación: ")
        if (idNacionalidad in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idNacionalidad)
            print "Datos encontrados: "
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="

            nuevaNacionalidad=raw_input("Ingrese la nueva nacionalidad: ");
            arrayNacionalidad[posicion]=nuevaNacionalidad
            nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],arrayEdad[posicion],nuevaNacionalidad,arrayGenero[posicion]]
            arrayPersona[posicion]=nuevaPersona
            print
            print arrayNacionalidad[posicion]
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="
            print
            print "La nacionalidad se cambió correctamente."
        else:
            print "No se pudo cambiar la nacionalidad."
        print

    def editarGenero(self):
        print
        idGenero=raw_input("Ingrese el número de identifiación: ")
        if (idGenero in arrayIdentificacion)==True:
            posicion=arrayIdentificacion.index(idGenero)
            print "Datos encontrados: "
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="

            nuevoGenero=raw_input("Ingrese su nuevo género: ");
            arrayGenero[posicion]=nuevoGenero
            nuevaPersona=[arrayNombre[posicion],arrayIdentificacion[posicion],arrayEdad[posicion],arrayNacionalidad[posicion],nuevoGenero]
            arrayPersona[posicion]=nuevaPersona

            print
            print arrayGenero[posicion]
            print
            print "====================================="
            print arrayPersona[posicion]
            print "====================================="
            print
            print "Su género se cambió correctamente."
        else:
            print "No se pudo cambiar el género."
        print

    def editar(self):
        print
        while True:
            persona().menuEditar()
            opcion=input("Seleccione el elemento que desea editar >>")
            if (opcion==1):
                persona().editarNombre()
            elif (opcion==2):
                persona().editarEdad()
            elif (opcion==3):
                persona().editarNacionalidad()
            elif (opcion==4):
                persona().editarGenero()
            elif (opcion==5):
                break
            else:
                print "Opción incorrecta"
        print
    def menuPStart(self):
        while True:
            persona().menuP()
            opcion=input("Inserte un número >>")
            if (opcion==1):
                persona().crear()
            elif (opcion==2):
                persona().editar()
            elif (opcion==3):
                persona().consultar()
            elif (opcion==4):
                persona().eliminar()
            elif (opcion==5):
                break
            else:
                print "Opción incorrecta"
class auto():
    def menuAStart(self):
        while True:
            Buy().buying()
            options = input("Ingrese el numero de la opcion que desee >>\n")

            if options == 1:
                print "============================================"
                print "Lista de Autos disponibles Chevrolet"
                print "============================================"
                time.sleep(2)
                print Chevrolet.mark, "\nModelo: ", Chevrolet.model, "\nAnio: ", Chevrolet.year, "\nMotor: ", Chevrolet.motor, "\nKilometraje: ", Chevrolet.km, "\nPrecio: ", Chevrolet.cost
                time.sleep(1)
                print
                pay = raw_input("¿Desea comprar este auto?(si/no) >>")
                if pay == "si" or pay=="SI" or pay=="Si":
                    identidad=raw_input("Ingrese su número de identidad:")
                    if (identidad in arrayIdentificacion)==True:
                        posicion=arrayIdentificacion.index(identidad)
                        print "Datos encontrados: "
                        print
                        print "================================="
                        print arrayPersona[posicion]
                        print "================================="
                        print
                        opcionC=raw_input("¿Desea proceder con la compra?(Si/No) >>")
                        if opcionC=="si" or opcionC=="SI" or opcionC=="Si":
                            print "Procesando..."
                            time.sleep(1)
                            arrayChevrolet.append(Chevrolet.mark)
                            arrayChevrolet.append(Chevrolet.model)
                            arrayChevrolet.append(Chevrolet.year)
                            arrayChevrolet.append(Chevrolet.motor)
                            arrayChevrolet.append(Chevrolet.cost)
                            arrayCar.append(arrayChevrolet)
                            arrayPersona[posicion].append(arrayChevrolet)
                            print arrayPersona[posicion]
                            print "FELICIDADES:Su compra se ha realizado con éxito"
                            print "Regresando al menú de compra..."
                        elif opcionC=="no" or opcionC=="NO" or opcionC=="No":
                            print "Cancelado"
                    else:
                        print "No se encontró resultados"
                    print
                    time.sleep(2)

                elif pay == "no" or pay=="NO" or pay=="No":
                    print "Regresando al menu de seleccion"
                    time.sleep(2)
            elif options == 2:
                print "============================================"
                print "Lista de Autos disponibles Toyota"
                print "============================================"
                time.sleep(2)
                print Toyota.mark, "\nModelo: ", Toyota.model, "\nAnio: ", Toyota.year, "\nMotor: ", Toyota.motor, "\nKilometraje: ", Toyota.km, "\nPrecio: ", Toyota.cost
                time.sleep(1)
                print
                pay = raw_input("¿Desea comprar este auto?(si/no) >>")
                if pay == "si" or pay=="SI" or pay=="Si":
                    identidad=raw_input("Ingrese su número de identidad:")
                    if (identidad in arrayIdentificacion)==True:
                        posicion=arrayIdentificacion.index(identidad)
                        print "Datos encontrados: "
                        print
                        print "================================="
                        print arrayPersona[posicion]
                        print "================================="
                        print
                        opcionC=raw_input("¿Desea proceder con la compra?(Si/No) >>")
                        if opcionC=="si" or opcionC=="SI" or opcionC=="Si":
                            print "Procesando..."
                            time.sleep(1)
                            arrayToyota.append(Toyota.mark)
                            arrayToyota.append(Toyota.model)
                            arrayToyota.append(Toyota.year)
                            arrayToyota.append(Toyota.motor)
                            arrayToyota.append(Toyota.cost)
                            arrayCar.append(arrayToyota)
                            arrayPersona[posicion].append(arrayToyota)
                            print arrayPersona[posicion]
                            print "FELICIDADES:Su compra se ha realizado con éxito"
                            print "Regresando al menú de compra..."
                        elif opcionC=="no" or opcionC=="NO" or opcionC=="No":
                            print "Cancelado"
                    else:
                        print "No se encontró resultados"
                    print
                    time.sleep(2)

                elif pay == "no" or pay=="NO" or pay=="No":
                    print "Regresando al menu de seleccion"
                    time.sleep(2)
            elif options == 3:
                print "============================================"
                print "Lista de Autos disponibles Honda"
                print "============================================"
                time.sleep(2)
                print Honda.mark, "\nModelo: ", Honda.model, "\nAnio: ", Honda.year, "\nMotor: ", Honda.motor, "\nKilometraje: ", Honda.km, "\nPrecio: ", Honda.cost
                time.sleep(1)
                print
                pay = raw_input("¿Desea comprar este auto?(si/no) >>")
                if pay == "si" or pay=="SI" or pay=="Si":
                    identidad=raw_input("Ingrese su número de identidad:")
                    if (identidad in arrayIdentificacion)==True:
                        posicion=arrayIdentificacion.index(identidad)
                        print "Datos encontrados: "
                        print
                        print "================================="
                        print arrayPersona[posicion]
                        print "================================="
                        print
                        opcionC=raw_input("¿Desea proceder con la compra?(Si/No) >>")
                        if opcionC=="si" or opcionC=="SI" or opcionC=="Si":
                            print "Procesando..."
                            time.sleep(1)
                            arrayHonda.append(Honda.mark)
                            arrayHonda.append(Honda.model)
                            arrayHonda.append(Honda.year)
                            arrayHonda.append(Honda.motor)
                            arrayHonda.append(Honda.cost)
                            arrayCar.append(arrayHonda)
                            arrayPersona[posicion].append(arrayHonda)
                            print arrayPersona[posicion]
                            print "FELICIDADES:Su compra se ha realizado con éxito"
                            print "Regresando al menú de compra..."
                        elif opcionC=="no" or opcionC=="NO" or opcionC=="No":
                            print "Cancelado"
                    else:
                        print "No se encontró resultados"
                    print
                    time.sleep(2)

                elif pay == "no" or pay=="NO" or pay=="No":
                    print "Regresando al menu de seleccion"
                    time.sleep(2)
            elif options == 4:
                print "============================================"
                print "Lista de Autos disponibles Nissan"
                print "============================================"
                time.sleep(2)
                print Nissan.mark, "\nModelo: ", Nissan.model, "\nAnio: ", Nissan.year, "\nMotor: ", Nissan.motor, "\nKilometraje: ", Nissan.km, "\nPrecio: ", Nissan.cost
                time.sleep(1)
                print
                pay = raw_input("¿Desea comprar este auto?(si/no) >>")
                if pay == "si" or pay=="SI" or pay=="Si":
                    identidad=raw_input("Ingrese su número de identidad:")
                    if (identidad in arrayIdentificacion)==True:
                        posicion=arrayIdentificacion.index(identidad)
                        print "Datos encontrados: "
                        print
                        print "================================="
                        print arrayPersona[posicion]
                        print "================================="
                        print
                        opcionC=raw_input("¿Desea proceder con la compra?(Si/No) >>")
                        if opcionC=="si" or opcionC=="SI" or opcionC=="Si":
                            print "Procesando..."
                            time.sleep(1)
                            arrayNissan.append(Nissan.mark)
                            arrayNissan.append(Nissan.model)
                            arrayNissan.append(Nissan.year)
                            arrayNissan.append(Nissan.motor)
                            arrayNissan.append(Nissan.cost)
                            arrayCar.append(arrayNissan)
                            arrayPersona[posicion].append(arrayNissan)
                            print arrayPersona[posicion]
                            print "FELICIDADES:Su compra se ha realizado con éxito"
                            print "Regresando al menú de compra..."
                        elif opcionC=="no" or opcionC=="NO" or opcionC=="No":
                            print "Cancelado"
                    else:
                        print "No se encontró resultados"
                    print
                    time.sleep(2)

                elif pay == "no" or pay=="NO" or pay=="No":
                    print "Regresando al menu de seleccion"
                    time.sleep(2)
            elif options == 5:
                break
            else:
                print "Valor Incorrecto"

def menu():
    print "================================="
    print "\tMenú de opciones"
    print "================================="
    print "\t1 - Gestión de personas"
    print "\t2 - Gestión de autos"
    print "\t3 - Gestión de compras"
    print "\t4 - Salir"

while True:
    menu()
    opcionMenu = input("Inserte un valor >> ")
    if opcionMenu==1:
        p=persona()
        p.menuPStart()
    elif opcionMenu==2:
        a=auto()
        a.menuAStart()
    elif opcionMenu==3:
        print "Opcion 3"
    elif opcionMenu==4:
        break
    else:
        print "Opción incorrecta"
