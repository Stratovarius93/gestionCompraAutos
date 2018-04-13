#!/usr/bin/python
# -*- coding: utf-8 -*-
def menu():
	print ("Menú de opciones")
	print ("\t1 - Gestión de personas")
	print ("\t2 - Gestión de autos")
	print ("\t3 - Gestión de compras")
	print ("\t4 - Salir")


while True:
	# Mostramos el menu
	menu()
	# solicituamos una opción al usuario
	opcionMenu = input("Inserte un numero valor >> ")
	if (opcionMenu==1):
		print ("Opcion 1")
	elif opcionMenu==2:
		print ("Opcion 2")
	elif opcionMenu==3:
		print ("Opcion 3")
	elif opcionMenu==4:
		break
	else:
		print ("Opción incorrecta")
